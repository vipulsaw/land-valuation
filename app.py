from flask import Flask, render_template, request, redirect, url_for, flash, send_file, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
import json
from datetime import datetime, date
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///land_valuation.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['STATIC_FOLDER'] = 'static'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['STATIC_FOLDER'], exist_ok=True)

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    valuations = db.relationship('LandValuation', backref='user', lazy=True)

class LandValuation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Client/Request Information
    valuation_purpose = db.Column(db.String(200), nullable=False)
    inspection_date = db.Column(db.Date, nullable=False)
    valuation_date = db.Column(db.Date, nullable=False)
    valuation_requested_by = db.Column(db.String(100), nullable=False)
    client_name = db.Column(db.String(100), nullable=False)
    case_number = db.Column(db.String(50))
    loan_type = db.Column(db.String(100))
    project_name = db.Column(db.String(100))

    # Property Details
    property_owner = db.Column(db.String(100), nullable=False)
    property_address = db.Column(db.String(500), nullable=False)
    property_description = db.Column(db.Text)
    property_type = db.Column(db.String(50), nullable=False)
    access_road_name = db.Column(db.String(100))
    survey_number = db.Column(db.String(100))
    plot_number = db.Column(db.String(100))
    cts_number = db.Column(db.String(100))
    locality_classification = db.Column(db.String(50))

    # Location Details
    railway_distance = db.Column(db.String(50))
    bus_stand_distance = db.Column(db.String(50))
    hospital_distance = db.Column(db.String(50))
    branch_distance = db.Column(db.String(50))
    property_identifiable = db.Column(db.Boolean, default=True)
    geo_latitude = db.Column(db.String(50))
    geo_longitude = db.Column(db.String(50))

    # Land Details
    land_ownership = db.Column(db.String(50))  # Freehold/Leasehold
    municipal_jurisdiction = db.Column(db.String(200))
    approvals_status = db.Column(db.String(100))

    # Boundaries
    east_boundary = db.Column(db.String(100))
    west_boundary = db.Column(db.String(100))
    north_boundary = db.Column(db.String(100))
    south_boundary = db.Column(db.String(100))

    # Structure Details
    construction_year = db.Column(db.Integer)
    property_age = db.Column(db.Integer)
    estimated_future_life = db.Column(db.Integer)
    present_condition = db.Column(db.String(50))
    repairs_required = db.Column(db.String(500))
    construction_type = db.Column(db.String(200))
    permitted_use = db.Column(db.String(50))
    actual_use = db.Column(db.String(50))
    no_of_floors = db.Column(db.Integer)
    compound_wall = db.Column(db.Boolean, default=False)
    other_amenities = db.Column(db.Text)

    # Specifications
    walls_plaster_painting = db.Column(db.String(200))
    doors_windows = db.Column(db.String(200))
    flooring_type = db.Column(db.String(100))
    toilet_finishing = db.Column(db.String(100))
    kitchen_platform = db.Column(db.String(100))
    plumbing_fittings = db.Column(db.String(100))
    electrical_fittings = db.Column(db.String(100))
    demolition_risk = db.Column(db.String(50))
    currently_occupied_by = db.Column(db.String(100))

    # Accommodation Details
    ground_floor_area = db.Column(db.Float, default=0)
    first_floor_area = db.Column(db.Float, default=0)
    second_floor_area = db.Column(db.Float, default=0)
    third_floor_area = db.Column(db.Float, default=0)
    basement_area = db.Column(db.Float, default=0)

    # Plot and Building Areas
    plot_area_sqm = db.Column(db.Float, nullable=False)
    plot_area_sqft = db.Column(db.Float, nullable=False)
    built_up_area = db.Column(db.Float)
    carpet_area = db.Column(db.Float)
    permissible_area = db.Column(db.Float)
    plot_coverage = db.Column(db.Float)
    fsi_used = db.Column(db.Float)

    # Market Rates
    market_rate_min = db.Column(db.Float)
    market_rate_max = db.Column(db.Float)
    rate_adopted = db.Column(db.Float)

    # Valuation Calculations
    land_value = db.Column(db.Float, nullable=False)
    building_value = db.Column(db.Float, default=0)
    repairs_deduction = db.Column(db.Float, default=0)
    total_value = db.Column(db.Float, nullable=False)
    insurance_value = db.Column(db.Float)
    distress_sale_value = db.Column(db.Float)

    # Construction Stage
    construction_stage = db.Column(db.String(50))
    percentage_completion = db.Column(db.Float, default=100)

    # Marketability
    sale_marketability = db.Column(db.String(50))
    lease_marketability = db.Column(db.String(50))

    # Additional Fields
    additional_notes = db.Column(db.Text)
    photos_path = db.Column(db.Text)  # Store multiple photo paths as JSON
    submission_date = db.Column(db.DateTime, default=datetime.utcnow)

    # Declarations
    structural_survey_done = db.Column(db.Boolean, default=False)
    report_validity_days = db.Column(db.Integer, default=90)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# Helper function for Indian currency formatting
def format_indian_currency(amount):
    """Format number as Indian currency with commas"""
    if amount is None:
        return "₹ 0"
    amount = float(amount)
    s = str(amount)
    parts = s.split('.')
    integer_part = parts[0]
    decimal_part = parts[1] if len(parts) > 1 else '00'

    # Format integer part with Indian comma style
    result = ''
    count = 0
    for digit in reversed(integer_part):
        if count == 3:
            result = ',' + result
            count = 0
        result = digit + result
        count += 1

    # Add decimal part
    if len(decimal_part) == 1:
        decimal_part += '0'
    result = '₹ ' + result + '.' + decimal_part[:2]
    return result

# Template filters
@app.template_filter('from_json')
def from_json_filter(value):
    """Convert JSON string to Python object in templates"""
    if value:
        try:
            return json.loads(value)
        except:
            return []
    return []

@app.template_filter('format_date')
def format_date_filter(value, format='%d-%m-%Y'):
    """Format date in templates"""
    if isinstance(value, str):
        try:
            value = datetime.strptime(value, '%Y-%m-%d').date()
        except:
            return value
    if isinstance(value, date):
        return value.strftime(format)
    return value

@app.template_filter('format_number')
def format_number_filter(value):
    """Format number with commas"""
    if value is None:
        return "0"
    try:
        return "{:,.2f}".format(float(value))
    except:
        return str(value)

# Helper function to convert images to base64 for PDF
def convert_photos_to_base64(photo_paths):
    """Convert photo file paths to base64 encoded strings"""
    encoded_photos = []
    if not photo_paths:
        return encoded_photos

    for photo_path in photo_paths:
        try:
            if os.path.exists(photo_path):
                with open(photo_path, 'rb') as f:
                    encoded_string = base64.b64encode(f.read()).decode('utf-8')
                    # Determine MIME type
                    if photo_path.lower().endswith('.jpg') or photo_path.lower().endswith('.jpeg'):
                        mime_type = 'image/jpeg'
                    elif photo_path.lower().endswith('.png'):
                        mime_type = 'image/png'
                    elif photo_path.lower().endswith('.gif'):
                        mime_type = 'image/gif'
                    elif photo_path.lower().endswith('.webp'):
                        mime_type = 'image/webp'
                    else:
                        mime_type = 'image/jpeg'

                    encoded_photos.append(f'data:{mime_type};base64,{encoded_string}')
            else:
                app.logger.warning(f"Photo not found: {photo_path}")
        except Exception as e:
            app.logger.error(f"Error encoding photo {photo_path}: {str(e)}")
    return encoded_photos

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('register'))

        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    valuations = LandValuation.query.filter_by(user_id=current_user.id).order_by(LandValuation.submission_date.desc()).all()
    return render_template('dashboard.html', valuations=valuations)

@app.route('/valuation/new', methods=['GET', 'POST'])
@login_required
def new_valuation():
    if request.method == 'POST':
        photos = request.files.getlist('land_photos')
        photo_paths = []

        # Handle multiple photo uploads
        for photo in photos:
            if photo and photo.filename:
                filename = secure_filename(f"{current_user.id}_{datetime.now().timestamp()}_{photo.filename}")
                photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                photo.save(photo_path)
                photo_paths.append(photo_path)

        # Convert date strings to date objects
        inspection_date = datetime.strptime(request.form.get('inspection_date'), '%Y-%m-%d').date()
        valuation_date = datetime.strptime(request.form.get('valuation_date'), '%Y-%m-%d').date()

        # Calculate total built up area
        ground_floor = float(request.form.get('ground_floor_area') or 0)
        first_floor = float(request.form.get('first_floor_area') or 0)
        second_floor = float(request.form.get('second_floor_area') or 0)
        third_floor = float(request.form.get('third_floor_area') or 0)
        basement = float(request.form.get('basement_area') or 0)

        built_up_area = ground_floor + first_floor + second_floor + third_floor + basement

        # If built_up_area not provided, calculate from form
        if not request.form.get('built_up_area'):
            built_up_area = built_up_area
        else:
            built_up_area = float(request.form.get('built_up_area') or 0)

        valuation = LandValuation(
            user_id=current_user.id,

            # Client/Request Information
            valuation_purpose=request.form.get('valuation_purpose'),
            inspection_date=inspection_date,
            valuation_date=valuation_date,
            valuation_requested_by=request.form.get('valuation_requested_by'),
            client_name=request.form.get('client_name'),
            case_number=request.form.get('case_number'),
            loan_type=request.form.get('loan_type'),
            project_name=request.form.get('project_name'),

            # Property Details
            property_owner=request.form.get('property_owner'),
            property_address=request.form.get('property_address'),
            property_description=request.form.get('property_description'),
            property_type=request.form.get('property_type'),
            access_road_name=request.form.get('access_road_name'),
            survey_number=request.form.get('survey_number'),
            plot_number=request.form.get('plot_number'),
            cts_number=request.form.get('cts_number'),
            locality_classification=request.form.get('locality_classification'),

            # Location Details
            railway_distance=request.form.get('railway_distance'),
            bus_stand_distance=request.form.get('bus_stand_distance'),
            hospital_distance=request.form.get('hospital_distance'),
            branch_distance=request.form.get('branch_distance'),
            property_identifiable=True,
            geo_latitude=request.form.get('geo_latitude'),
            geo_longitude=request.form.get('geo_longitude'),

            # Land Details
            land_ownership=request.form.get('land_ownership') or 'Freehold',
            municipal_jurisdiction=request.form.get('municipal_jurisdiction'),
            approvals_status=request.form.get('approvals_status') or 'Yes',

            # Boundaries
            east_boundary=request.form.get('east_boundary'),
            west_boundary=request.form.get('west_boundary'),
            north_boundary=request.form.get('north_boundary'),
            south_boundary=request.form.get('south_boundary'),

            # Structure Details
            construction_year=int(request.form.get('construction_year') or 0),
            property_age=int(request.form.get('property_age') or 0),
            estimated_future_life=int(request.form.get('estimated_future_life') or 0),
            present_condition=request.form.get('present_condition') or 'Good',
            repairs_required=request.form.get('repairs_required') or 'No',
            construction_type=request.form.get('construction_type') or 'Load Bearing structure',
            permitted_use=request.form.get('permitted_use') or 'Residential',
            actual_use=request.form.get('actual_use') or 'Residential',
            no_of_floors=int(request.form.get('no_of_floors') or 1),
            compound_wall=bool(request.form.get('compound_wall')),
            other_amenities=request.form.get('other_amenities'),

            # Specifications
            walls_plaster_painting=request.form.get('walls_plaster_painting') or 'Internal & External Completed',
            doors_windows=request.form.get('doors_windows') or 'Solid Flush Doors And Al Section Window',
            flooring_type=request.form.get('flooring_type') or 'Vitrified Tiles',
            toilet_finishing=request.form.get('toilet_finishing') or 'Ceramic',
            kitchen_platform=request.form.get('kitchen_platform') or 'Granite & Stainless Steel Sink',
            plumbing_fittings=request.form.get('plumbing_fittings') or 'Concealed Plumbing Fitting',
            electrical_fittings=request.form.get('electrical_fittings') or 'Concealed Electrical Fitting',
            demolition_risk=request.form.get('demolition_risk') or 'Low',
            currently_occupied_by=request.form.get('currently_occupied_by') or 'Owner',

            # Accommodation Details
            ground_floor_area=ground_floor,
            first_floor_area=first_floor,
            second_floor_area=second_floor,
            third_floor_area=third_floor,
            basement_area=basement,

            # Plot and Building Areas
            plot_area_sqm=float(request.form.get('plot_area_sqm') or 0),
            plot_area_sqft=float(request.form.get('plot_area_sqft') or 0),
            built_up_area=built_up_area,
            carpet_area=float(request.form.get('carpet_area') or (built_up_area * 0.85)),
            permissible_area=float(request.form.get('permissible_area') or built_up_area),
            plot_coverage=float(request.form.get('plot_coverage') or 0),
            fsi_used=float(request.form.get('fsi_used') or 0),

            # Market Rates
            market_rate_min=float(request.form.get('market_rate_min') or 0),
            market_rate_max=float(request.form.get('market_rate_max') or 0),
            rate_adopted=float(request.form.get('rate_adopted') or 0),

            # Valuation Calculations
            land_value=float(request.form.get('land_value') or 0),
            building_value=float(request.form.get('building_value') or 0),
            repairs_deduction=float(request.form.get('repairs_deduction') or 0),
            total_value=float(request.form.get('total_value') or 0),
            insurance_value=float(request.form.get('insurance_value') or 0),
            distress_sale_value=float(request.form.get('distress_sale_value') or 0),

            # Construction Stage
            construction_stage=request.form.get('construction_stage') or 'Completed',
            percentage_completion=float(request.form.get('percentage_completion') or 100),

            # Marketability
            sale_marketability=request.form.get('sale_marketability') or 'Good',
            lease_marketability=request.form.get('lease_marketability') or 'Average',

            # Additional Fields
            additional_notes=request.form.get('additional_notes'),
            photos_path=json.dumps(photo_paths) if photo_paths else None,

            # Declarations
            structural_survey_done=False,
            report_validity_days=90
        )

        db.session.add(valuation)
        db.session.commit()

        flash('Valuation submitted successfully! Report is ready for download.', 'success')
        return redirect(url_for('dashboard'))

    return render_template('valuation_form.html')

@app.route('/valuation/<int:valuation_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_valuation(valuation_id):
    valuation = LandValuation.query.get_or_404(valuation_id)

    if valuation.user_id != current_user.id:
        flash('Unauthorized access', 'error')
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        photos = request.files.getlist('land_photos')
        photo_paths = []

        # Handle photo updates - keep old photos if new ones not uploaded
        if photos and photos[0].filename:
            # Delete old photos
            if valuation.photos_path:
                try:
                    old_photos = json.loads(valuation.photos_path)
                    for old_photo in old_photos:
                        if os.path.exists(old_photo):
                            os.remove(old_photo)
                except:
                    pass

            # Save new photos
            for photo in photos:
                if photo and photo.filename:
                    filename = secure_filename(f"{current_user.id}_{datetime.now().timestamp()}_{photo.filename}")
                    photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    photo.save(photo_path)
                    photo_paths.append(photo_path)

            if photo_paths:
                valuation.photos_path = json.dumps(photo_paths)

        # Update dates
        if request.form.get('inspection_date'):
            valuation.inspection_date = datetime.strptime(request.form.get('inspection_date'), '%Y-%m-%d').date()
        if request.form.get('valuation_date'):
            valuation.valuation_date = datetime.strptime(request.form.get('valuation_date'), '%Y-%m-%d').date()

        # Update all other fields
        valuation.valuation_purpose = request.form.get('valuation_purpose')
        valuation.valuation_requested_by = request.form.get('valuation_requested_by')
        valuation.client_name = request.form.get('client_name')
        valuation.case_number = request.form.get('case_number')
        valuation.loan_type = request.form.get('loan_type')
        valuation.project_name = request.form.get('project_name')
        valuation.property_owner = request.form.get('property_owner')
        valuation.property_address = request.form.get('property_address')
        valuation.property_type = request.form.get('property_type')
        valuation.access_road_name = request.form.get('access_road_name')
        valuation.survey_number = request.form.get('survey_number')
        valuation.plot_number = request.form.get('plot_number')
        valuation.cts_number = request.form.get('cts_number')
        valuation.locality_classification = request.form.get('locality_classification')
        valuation.railway_distance = request.form.get('railway_distance')
        valuation.bus_stand_distance = request.form.get('bus_stand_distance')
        valuation.hospital_distance = request.form.get('hospital_distance')
        valuation.branch_distance = request.form.get('branch_distance')
        valuation.geo_latitude = request.form.get('geo_latitude')
        valuation.geo_longitude = request.form.get('geo_longitude')
        valuation.land_ownership = request.form.get('land_ownership')
        valuation.municipal_jurisdiction = request.form.get('municipal_jurisdiction')
        valuation.approvals_status = request.form.get('approvals_status')
        valuation.east_boundary = request.form.get('east_boundary')
        valuation.west_boundary = request.form.get('west_boundary')
        valuation.north_boundary = request.form.get('north_boundary')
        valuation.south_boundary = request.form.get('south_boundary')
        valuation.construction_year = int(request.form.get('construction_year') or 0)
        valuation.property_age = int(request.form.get('property_age') or 0)
        valuation.estimated_future_life = int(request.form.get('estimated_future_life') or 0)
        valuation.present_condition = request.form.get('present_condition')
        valuation.repairs_required = request.form.get('repairs_required')
        valuation.construction_type = request.form.get('construction_type')
        valuation.permitted_use = request.form.get('permitted_use')
        valuation.actual_use = request.form.get('actual_use')
        valuation.no_of_floors = int(request.form.get('no_of_floors') or 1)
        valuation.compound_wall = bool(request.form.get('compound_wall'))
        valuation.other_amenities = request.form.get('other_amenities')
        valuation.walls_plaster_painting = request.form.get('walls_plaster_painting')
        valuation.doors_windows = request.form.get('doors_windows')
        valuation.flooring_type = request.form.get('flooring_type')
        valuation.toilet_finishing = request.form.get('toilet_finishing')
        valuation.kitchen_platform = request.form.get('kitchen_platform')
        valuation.plumbing_fittings = request.form.get('plumbing_fittings')
        valuation.electrical_fittings = request.form.get('electrical_fittings')
        valuation.demolition_risk = request.form.get('demolition_risk')
        valuation.currently_occupied_by = request.form.get('currently_occupied_by')
        valuation.ground_floor_area = float(request.form.get('ground_floor_area') or 0)
        valuation.first_floor_area = float(request.form.get('first_floor_area') or 0)
        valuation.second_floor_area = float(request.form.get('second_floor_area') or 0)
        valuation.third_floor_area = float(request.form.get('third_floor_area') or 0)
        valuation.basement_area = float(request.form.get('basement_area') or 0)
        valuation.plot_area_sqm = float(request.form.get('plot_area_sqm') or 0)
        valuation.plot_area_sqft = float(request.form.get('plot_area_sqft') or 0)
        valuation.built_up_area = float(request.form.get('built_up_area') or 0)
        valuation.carpet_area = float(request.form.get('carpet_area') or 0)
        valuation.permissible_area = float(request.form.get('permissible_area') or 0)
        valuation.plot_coverage = float(request.form.get('plot_coverage') or 0)
        valuation.fsi_used = float(request.form.get('fsi_used') or 0)
        valuation.market_rate_min = float(request.form.get('market_rate_min') or 0)
        valuation.market_rate_max = float(request.form.get('market_rate_max') or 0)
        valuation.rate_adopted = float(request.form.get('rate_adopted') or 0)
        valuation.land_value = float(request.form.get('land_value') or 0)
        valuation.building_value = float(request.form.get('building_value') or 0)
        valuation.repairs_deduction = float(request.form.get('repairs_deduction') or 0)
        valuation.total_value = float(request.form.get('total_value') or 0)
        valuation.insurance_value = float(request.form.get('insurance_value') or 0)
        valuation.distress_sale_value = float(request.form.get('distress_sale_value') or 0)
        valuation.construction_stage = request.form.get('construction_stage')
        valuation.percentage_completion = float(request.form.get('percentage_completion') or 100)
        valuation.sale_marketability = request.form.get('sale_marketability')
        valuation.lease_marketability = request.form.get('lease_marketability')
        valuation.additional_notes = request.form.get('additional_notes')
        valuation.structural_survey_done = bool(request.form.get('structural_survey_done'))
        valuation.report_validity_days = int(request.form.get('report_validity_days') or 90)

        db.session.commit()
        flash('Valuation updated successfully!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('edit_valuation.html', valuation=valuation)

@app.route('/valuation/<int:valuation_id>/delete', methods=['POST'])
@login_required
def delete_valuation(valuation_id):
    valuation = LandValuation.query.get_or_404(valuation_id)

    if valuation.user_id != current_user.id:
        flash('Unauthorized access', 'error')
        return redirect(url_for('dashboard'))

    # Delete associated photos
    if valuation.photos_path:
        try:
            photo_paths = json.loads(valuation.photos_path)
            for photo_path in photo_paths:
                if os.path.exists(photo_path):
                    os.remove(photo_path)
        except:
            pass

    db.session.delete(valuation)
    db.session.commit()

    flash('Valuation deleted successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/download/<int:valuation_id>')
@login_required
def download_pdf(valuation_id):
    # Fetch valuation from database
    valuation = LandValuation.query.get_or_404(valuation_id)

    # Check if user has permission
    if valuation.user_id != current_user.id:
        flash('Unauthorized access', 'error')
        return redirect(url_for('dashboard'))

    try:
        # Get photo paths and convert to base64
        photo_paths = []
        if valuation.photos_path:
            try:
                photo_paths = json.loads(valuation.photos_path)
            except:
                pass

        # Convert photos to base64 for embedding in PDF
        encoded_photos = convert_photos_to_base64(photo_paths)

        # Render HTML template with base64 encoded photos
        html_content = render_template(
            'professional_report.html',
            valuation=valuation,
            encoded_photos=encoded_photos
        )

        # Generate PDF using WeasyPrint - SIMPLIFIED VERSION
        # Import weasyprint directly
        import weasyprint
        
        # Create PDF from HTML
        pdf_document = weasyprint.HTML(string=html_content)
        pdf_bytes = pdf_document.write_pdf()
        
        # Create response with proper headers for download
        response = make_response(pdf_bytes)
        filename = f"Land_Valuation_Report_{valuation.case_number or valuation_id}_{valuation.client_name.replace(' ', '_')}.pdf"
        filename = secure_filename(filename)
        
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename="{filename}"'
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        
        return response

    except Exception as e:
        # Any other error
        app.logger.error(f"PDF generation error: {str(e)}")
        # Fallback to HTML download
        flash(f'Error generating PDF. Downloading HTML version instead.', 'warning')
        return download_html_fallback(valuation_id, valuation)

def download_html_fallback(valuation_id, valuation):
    """Fallback function to download HTML version when PDF generation fails"""
    # Get photo paths and convert to base64
    photo_paths = []
    if valuation.photos_path:
        try:
            photo_paths = json.loads(valuation.photos_path)
        except:
            pass

    encoded_photos = convert_photos_to_base64(photo_paths)
    
    # Render HTML template
    html_content = render_template(
        'professional_report.html',
        valuation=valuation,
        encoded_photos=encoded_photos
    )
    
    # Create response with HTML content
    filename = f"Land_Valuation_Report_{valuation.case_number or valuation_id}_{valuation.client_name.replace(' ', '_')}.html"
    filename = secure_filename(filename)
    
    response = make_response(html_content)
    response.headers['Content-Type'] = 'text/html'
    response.headers['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

@app.route('/view-report/<int:valuation_id>')
@login_required
def view_report(valuation_id):
    """View report in browser (HTML version)"""
    valuation = LandValuation.query.get_or_404(valuation_id)

    if valuation.user_id != current_user.id:
        flash('Unauthorized access', 'error')
        return redirect(url_for('dashboard'))

    # Get photo paths and convert to base64 for HTML viewing
    photo_paths = []
    if valuation.photos_path:
        try:
            photo_paths = json.loads(valuation.photos_path)
        except:
            pass

    encoded_photos = convert_photos_to_base64(photo_paths)

    return render_template(
        'professional_report.html',
        valuation=valuation,
        encoded_photos=encoded_photos
    )

@app.route('/check-images/<int:valuation_id>')
@login_required
def check_images(valuation_id):
    valuation = LandValuation.query.get_or_404(valuation_id)

    if valuation.user_id != current_user.id:
        return "Unauthorized", 403

    result = f"""
    <h1>Image Debug for Valuation #{valuation_id}</h1>
    <p>Client: {valuation.client_name}</p>
    <p>Photos Path: {valuation.photos_path}</p>
    """

    if valuation.photos_path:
        try:
            photos = json.loads(valuation.photos_path)
            result += f"<p>Number of photos: {len(photos)}</p>"
            result += "<ul>"
            for i, photo_path in enumerate(photos):
                exists = "✅ EXISTS" if os.path.exists(photo_path) else "❌ MISSING"
                result += f"<li>Photo {i+1}: {photo_path} - {exists}</li>"
            result += "</ul>"
        except Exception as e:
            result += f"<p>Error parsing photos: {str(e)}</p>"
    else:
        result += "<p>No photos found</p>"

    return result

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False, host='0.0.0.0', port=5000)
