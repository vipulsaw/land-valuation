"""
Database Migration Script for Ujjivan-specific Fields
This script adds the Ujjivan-specific columns to the LandValuation table.
Run this script ONCE after updating your code to add Ujjivan support.
"""

from app import app, db
from sqlalchemy import inspect, text

def check_column_exists(table_name, column_name):
    """Check if a column exists in a table"""
    inspector = inspect(db.engine)
    columns = [col['name'] for col in inspector.get_columns(table_name)]
    return column_name in columns

def migrate_database():
    """Perform database migration for Ujjivan fields"""
    with app.app_context():
        print("🔄 Starting Ujjivan fields migration...")
        
        # List of new columns to add
        new_columns = [
            ("vendor_name", "VARCHAR(200)"),
            ("borrower_name", "VARCHAR(200)"),
            ("developer_name", "VARCHAR(200)"),
            ("contact_person", "VARCHAR(200)"),
            ("property_demarcated", "VARCHAR(50)"),
            ("place", "VARCHAR(100)"),
            ("nearest_landmark", "VARCHAR(200)"),
            ("zonal_classification", "VARCHAR(100)"),
            ("habitation", "VARCHAR(50)"),
            ("water_facility", "VARCHAR(50)"),
            ("underground_drainage", "VARCHAR(50)"),
            ("tar_roads", "VARCHAR(50)"),
            ("electricity", "VARCHAR(50)"),
            ("surrounding_locality", "VARCHAR(200)"),
            ("nearby_amenities", "VARCHAR(500)"),
            ("site_dimension_ew", "VARCHAR(50)"),
            ("site_dimension_ns", "VARCHAR(50)"),
            ("sanitary_fittings", "VARCHAR(100)"),
            ("lifts", "VARCHAR(50)"),
            ("super_structure", "VARCHAR(500)"),
            ("roof_type", "VARCHAR(200)"),
            ("elevation_quality", "VARCHAR(50)"),
            ("interiors_quality", "VARCHAR(50)"),
            ("total_plot_area_schedule", "VARCHAR(50)"),
            ("buildup_area_schedule_sqm", "FLOAT"),
            ("buildup_area_schedule_sqft", "FLOAT"),
            ("statutory_approval", "VARCHAR(500)"),
            ("approval_number", "VARCHAR(200)"),
            ("fsi_permitted", "VARCHAR(100)"),
            ("occupation_certificate", "VARCHAR(200)"),
            ("land_area_valuation", "FLOAT"),
            ("gf_rate", "FLOAT"),
            ("gf_value", "FLOAT"),
            ("ff_rate", "FLOAT"),
            ("ff_value", "FLOAT"),
            ("depreciation_percentage", "FLOAT"),
            ("net_construction_value", "FLOAT"),
            ("documents_provided", "TEXT"),
            ("plinth_level_status", "VARCHAR(50)"),
            ("framed_structure_status", "VARCHAR(50)"),
            ("super_structure_status", "VARCHAR(50)"),
            ("plastering_status", "VARCHAR(50)"),
            ("flooring_status", "VARCHAR(50)"),
            ("civil_progress", "VARCHAR(50)"),
            ("interiors_progress", "VARCHAR(50)"),
            ("report_prepared_by", "VARCHAR(200)")
        ]
        
        added_count = 0
        skipped_count = 0
        
        for column_name, column_type in new_columns:
            if not check_column_exists('land_valuation', column_name):
                try:
                    # Add the column
                    with db.engine.connect() as conn:
                        conn.execute(text(f"ALTER TABLE land_valuation ADD COLUMN {column_name} {column_type}"))
                        conn.commit()
                    print(f"✓ Added column: {column_name}")
                    added_count += 1
                except Exception as e:
                    print(f"✗ Error adding column {column_name}: {str(e)}")
            else:
                print(f"⊘ Column already exists: {column_name}")
                skipped_count += 1
        
        print("\n" + "="*60)
        print("📊 MIGRATION SUMMARY")
        print("="*60)
        print(f"Columns Added: {added_count}")
        print(f"Columns Skipped (already exist): {skipped_count}")
        print(f"Total Columns Processed: {len(new_columns)}")
        print("="*60)
        print("✅ Migration completed successfully!")
        print("="*60)
        print("\n💡 Next Steps:")
        print(" 1. Restart your Flask application")
        print(" 2. Go to /valuation/new?bank=ujjivan to use the Ujjivan form")
        print(" 3. Create a new Ujjivan valuation report")
        print()

if __name__ == '__main__':
    try:
        migrate_database()
    except Exception as e:
        print(f"\n❌ Migration failed with error:")
        print(f" {str(e)}")
        print("\n💡 Troubleshooting:")
        print(" 1. Make sure your Flask app is not running")
        print(" 2. Backup your database before running migration")
        print(" 3. Check if all dependencies are installed")
        import traceback
        traceback.print_exc()

