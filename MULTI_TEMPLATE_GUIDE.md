# 📄 Multi-Template System Guide

## Overview

Your Land Valuation System now supports **multiple report templates**! Users can choose from different report formats based on their specific needs, client requirements, or property types.

## 🎯 Features

### Available Templates

1. **Professional Banking Report** (Default)
   - Comprehensive multi-page format
   - Suitable for banking and financial institutions
   - Includes detailed specifications and declarations
   - File: `professional_report.html`

2. **Compact Report**
   - Single-page format
   - Quick valuation overview
   - Perfect for preliminary assessments
   - File: `compact_report.html`

3. **Residential Property Report**
   - Specialized for residential properties
   - Emphasis on living amenities and specifications
   - Modern gradient design
   - File: `residential_report.html`

4. **Detailed Technical Report**
   - Comprehensive technical analysis
   - Extended specifications section
   - File: `detailed_report.html`

5. **Commercial Property Report**
   - Tailored for commercial properties
   - Business-focused valuation metrics
   - File: `commercial_report.html`

## 🚀 Getting Started

### Step 1: Run Database Migration

Before using the multi-template feature, you need to migrate your existing database:

```bash
cd land-valuation
python migrate_database.py
```

This will:
- Add the `template_id` column to existing valuations
- Create the `ReportTemplate` table
- Initialize 5 default templates
- Assign the default template to existing valuations

### Step 2: Start Your Application

```bash
python app.py
```

### Step 3: Access Templates

- **View all templates**: Navigate to `/templates` or click "Preview Templates" in the valuation form
- **Create valuation**: Select a template from the dropdown in the valuation form
- **Preview template**: Click "Preview" on any template to see a sample report

## 📝 How to Use

### Creating a New Valuation with Template Selection

1. Go to Dashboard → New Valuation
2. **First Section**: Select your preferred report template
3. View the template description to understand its purpose
4. Fill in the valuation details
5. Submit the form

The generated PDF will use your selected template!

### Viewing Available Templates

1. From Dashboard, click on your username dropdown
2. Select "Report Templates" (or navigate to `/templates`)
3. Browse all available templates
4. Click "Preview" to see sample reports
5. Click "Use Template" to create a valuation with that template

### Editing Existing Valuations

- Existing valuations will continue to use their assigned template
- The template cannot be changed after creation (to maintain consistency)
- Create a new valuation if you need a different template

## 🎨 Customizing Templates

### Creating a New Template

1. **Create the HTML file** in `templates/` folder:
   ```html
   <!-- templates/my_custom_report.html -->
   <!DOCTYPE html>
   <html>
   <head>
       <title>My Custom Report</title>
       <style>
           /* Your custom styles */
       </style>
   </head>
   <body>
       <!-- Use valuation object: {{ valuation.client_name }} -->
       <!-- Use photos: {% for photo in encoded_photos %} -->
       <!-- Use logo: {{ logo_base64 }} -->
   </body>
   </html>
   ```

2. **Add template to database** (in `app.py` or via admin panel):
   ```python
   custom_template = ReportTemplate(
       name='My Custom Template',
       description='Description of what makes this template special',
       template_file='my_custom_report.html',
       is_active=True,
       is_default=False
   )
   db.session.add(custom_template)
   db.session.commit()
   ```

3. **Restart your application** and the new template will appear in the list!

### Template Variables Available

All templates have access to:

- `valuation` - The LandValuation object with all fields
- `encoded_photos` - List of base64-encoded photo strings
- `logo_base64` - Base64-encoded company logo
- `current_user` - Current logged-in user
- `preview_mode` - Boolean (True when previewing)

### Example Template Structure

```html
<!DOCTYPE html>
<html>
<head>
    <title>Valuation Report</title>
    <style>
        @page { size: A4; margin: 1.5cm; }
        body { font-family: Arial; font-size: 10pt; }
        /* Add your styles */
    </style>
</head>
<body>
    <!-- Header -->
    <div class="header">
        <img src="{{ logo_base64 }}" alt="Logo">
        <h1>{{ valuation.client_name }}</h1>
    </div>

    <!-- Property Details -->
    <h2>Property Information</h2>
    <p>Address: {{ valuation.property_address }}</p>
    <p>Type: {{ valuation.property_type }}</p>
    <p>Value: ₹{{ "{:,.2f}".format(valuation.total_value) }}</p>

    <!-- Photos -->
    {% if encoded_photos %}
        <h2>Property Images</h2>
        {% for photo in encoded_photos %}
            <img src="{{ photo }}" style="max-width: 300px;">
        {% endfor %}
    {% endif %}

    <!-- Signature -->
    <div class="signature">
        <p>Valuer: {{ current_user.username }}</p>
        <p>Date: {{ valuation.valuation_date.strftime('%d/%m/%Y') }}</p>
    </div>
</body>
</html>
```

## 🔧 Advanced Configuration

### Setting a Different Default Template

```python
# In Python shell or migration script
from app import app, db, ReportTemplate

with app.app_context():
    # Remove default from current default
    current_default = ReportTemplate.query.filter_by(is_default=True).first()
    if current_default:
        current_default.is_default = False
    
    # Set new default
    new_default = ReportTemplate.query.filter_by(name='Compact Report').first()
    new_default.is_default = True
    
    db.session.commit()
```

### Deactivating a Template

```python
template = ReportTemplate.query.filter_by(name='Old Template').first()
template.is_active = False
db.session.commit()
```

### Template-Specific Custom Fields

You can store template-specific configuration in the `custom_fields` JSON column:

```python
import json

template = ReportTemplate.query.filter_by(name='Commercial Report').first()
template.custom_fields = json.dumps({
    'show_rental_analysis': True,
    'include_roi_calculation': True,
    'commercial_specific_sections': ['Tenant Details', 'Lease Terms']
})
db.session.commit()
```

Then in your template:
```html
{% set custom = template.custom_fields|from_json %}
{% if custom.show_rental_analysis %}
    <!-- Show rental analysis section -->
{% endif %}
```

## 📊 Database Schema

### ReportTemplate Table

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| name | String(100) | Template name |
| description | String(500) | Template description |
| template_file | String(200) | HTML filename |
| is_active | Boolean | Active status |
| is_default | Boolean | Default template flag |
| created_date | DateTime | Creation timestamp |
| custom_fields | Text | JSON for custom config |

### LandValuation Table (Updated)

Added column:
- `template_id` - Foreign key to ReportTemplate

## 🎯 Best Practices

1. **Always backup your database** before running migrations
2. **Test new templates** using the preview feature before using them
3. **Keep template names descriptive** and purpose-clear
4. **Use the default template** for general-purpose valuations
5. **Create specialized templates** for specific property types or clients
6. **Document custom fields** if using template-specific configuration

## 🐛 Troubleshooting

### Template not appearing in dropdown

- Check if `is_active` is set to `True`
- Verify the template file exists in `templates/` folder
- Restart the Flask application

### PDF generation fails with new template

- Ensure all required variables are used correctly
- Check for syntax errors in the HTML/CSS
- Verify WeasyPrint compatibility (avoid complex CSS)
- Test with the HTML preview first (`/view-report/<id>`)

### Existing valuations showing wrong template

- Run the migration script again
- Check the `template_id` in the database
- Verify the template file still exists

### Images not showing in PDF

- Ensure `encoded_photos` is being passed to the template
- Verify base64 encoding is correct
- Check image src format: `<img src="{{ photo }}">`

## 📞 Support

For issues or questions:
1. Check the Flask application logs
2. Verify database schema with `python -c "from app import db, inspect; print(inspect(db.engine).get_columns('land_valuation'))"`
3. Test template rendering in HTML mode first
4. Review WeasyPrint documentation for PDF-specific issues

## 🎉 What's Next?

- Create custom templates for specific banks or clients
- Add template categories (Banking, Legal, Insurance, etc.)
- Implement template versioning
- Add template import/export functionality
- Create a template editor interface

---

**Version**: 1.0.0  
**Last Updated**: January 2026  
**Compatibility**: Flask 3.0.0, WeasyPrint 67.0

