"""
Quick diagnostic script to check if Ujjivan setup is complete
"""

from app import app, db
from sqlalchemy import inspect
import os

def check_setup():
    """Check if Ujjivan setup is complete"""
    with app.app_context():
        print("="*60)
        print("UJJIVAN SETUP DIAGNOSTIC")
        print("="*60)
        print()
        
        # Check template files
        print("📁 Checking Template Files:")
        print("-" * 60)
        ujjivan_form = os.path.exists('templates/ujjivan_valuation_form.html')
        ujjivan_report = os.path.exists('templates/ujjivan_report.html')
        
        print(f"{'✓' if ujjivan_form else '✗'} ujjivan_valuation_form.html {'EXISTS' if ujjivan_form else 'MISSING'}")
        print(f"{'✓' if ujjivan_report else '✗'} ujjivan_report.html {'EXISTS' if ujjivan_report else 'MISSING'}")
        print()
        
        # Check database columns
        print("🗄️  Checking Database Columns:")
        print("-" * 60)
        inspector = inspect(db.engine)
        columns = [col['name'] for col in inspector.get_columns('land_valuation')]
        
        ujjivan_fields = [
            'vendor_name', 'borrower_name', 'developer_name', 'contact_person',
            'property_demarcated', 'place', 'nearest_landmark', 'zonal_classification',
            'habitation', 'water_facility', 'underground_drainage', 'tar_roads',
            'electricity', 'surrounding_locality', 'nearby_amenities',
            'site_dimension_ew', 'site_dimension_ns', 'sanitary_fittings',
            'lifts', 'super_structure', 'roof_type', 'elevation_quality',
            'interiors_quality', 'total_plot_area_schedule',
            'buildup_area_schedule_sqm', 'buildup_area_schedule_sqft',
            'statutory_approval', 'approval_number', 'fsi_permitted',
            'occupation_certificate', 'land_area_valuation', 'gf_rate',
            'gf_value', 'ff_rate', 'ff_value', 'depreciation_percentage',
            'net_construction_value', 'documents_provided',
            'plinth_level_status', 'framed_structure_status',
            'super_structure_status', 'plastering_status', 'flooring_status',
            'civil_progress', 'interiors_progress', 'report_prepared_by'
        ]
        
        missing_fields = []
        for field in ujjivan_fields:
            if field in columns:
                print(f"✓ {field}")
            else:
                print(f"✗ {field} - MISSING!")
                missing_fields.append(field)
        
        print()
        print("="*60)
        print("SUMMARY")
        print("="*60)
        
        if ujjivan_form and ujjivan_report and not missing_fields:
            print("✅ ALL CHECKS PASSED!")
            print("Your Ujjivan setup is complete and ready to use.")
        else:
            print("⚠️  SETUP INCOMPLETE!")
            print()
            if not ujjivan_form or not ujjivan_report:
                print("Missing template files. Please ensure:")
                print("  - templates/ujjivan_valuation_form.html exists")
                print("  - templates/ujjivan_report.html exists")
            
            if missing_fields:
                print(f"\n{len(missing_fields)} database fields are missing!")
                print("\n🔧 ACTION REQUIRED:")
                print("Run the migration script:")
                print("  python3 migrate_ujjivan_fields.py")
                print("\nOr use the automated setup:")
                print("  Windows: setup_ujjivan.bat")
                print("  Linux/Mac: ./setup_ujjivan.sh")
        
        print()
        print("="*60)

if __name__ == '__main__':
    try:
        check_setup()
    except Exception as e:
        print(f"\n❌ Error running diagnostic:")
        print(f"   {str(e)}")
        print("\nMake sure your Flask app is properly configured.")
        import traceback
        traceback.print_exc()

