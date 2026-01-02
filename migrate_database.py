"""
Database Migration Script for Multi-Template Support
This script adds the template_id column to existing LandValuation records
and ensures all templates are properly initialized.

Run this script ONCE after updating your code to add multi-template support.
"""

from app import app, db, LandValuation, ReportTemplate, initialize_default_templates
from sqlalchemy import inspect

def check_column_exists(table_name, column_name):
    """Check if a column exists in a table"""
    inspector = inspect(db.engine)
    columns = [col['name'] for col in inspector.get_columns(table_name)]
    return column_name in columns

def migrate_database():
    """Perform database migration"""
    with app.app_context():
        print("🔄 Starting database migration...")
        
        # Create all tables (this will add new tables and columns)
        db.create_all()
        print("✓ Database schema updated")
        
        # Initialize default templates
        print("\n📝 Initializing default templates...")
        initialize_default_templates()
        
        # Get the default template
        default_template = ReportTemplate.query.filter_by(is_default=True).first()
        
        if default_template:
            print(f"✓ Default template found: {default_template.name}")
            
            # Update existing valuations without a template
            valuations_without_template = LandValuation.query.filter_by(template_id=None).all()
            
            if valuations_without_template:
                print(f"\n🔧 Updating {len(valuations_without_template)} existing valuations...")
                for valuation in valuations_without_template:
                    valuation.template_id = default_template.id
                
                db.session.commit()
                print(f"✓ Updated {len(valuations_without_template)} valuations with default template")
            else:
                print("✓ All valuations already have templates assigned")
        else:
            print("⚠ Warning: No default template found. Please check template initialization.")
        
        # Display summary
        print("\n" + "="*60)
        print("📊 MIGRATION SUMMARY")
        print("="*60)
        
        template_count = ReportTemplate.query.count()
        valuation_count = LandValuation.query.count()
        
        print(f"Total Templates: {template_count}")
        print(f"Total Valuations: {valuation_count}")
        
        print("\n📋 Available Templates:")
        templates = ReportTemplate.query.all()
        for template in templates:
            status = "✓ DEFAULT" if template.is_default else "  Active" if template.is_active else "  Inactive"
            print(f"  {status} | {template.name}")
            print(f"           {template.description}")
            print(f"           File: {template.template_file}")
            print()
        
        print("="*60)
        print("✅ Migration completed successfully!")
        print("="*60)
        print("\n💡 Next Steps:")
        print("   1. Start your Flask application")
        print("   2. Go to /templates to view all available templates")
        print("   3. Create a new valuation and select a template")
        print("   4. Existing valuations will use the default template")
        print()

if __name__ == '__main__':
    try:
        migrate_database()
    except Exception as e:
        print(f"\n❌ Migration failed with error:")
        print(f"   {str(e)}")
        print("\n💡 Troubleshooting:")
        print("   1. Make sure your Flask app is not running")
        print("   2. Backup your database before running migration")
        print("   3. Check if all dependencies are installed")
        import traceback
        traceback.print_exc()

