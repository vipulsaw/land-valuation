"""
Database Migration Script for Bank-Based Template System
This script migrates from property-based templates to bank-based templates.

Run this script ONCE after updating your code.
"""

from app import app, db, LandValuation, ReportTemplate, initialize_default_templates
from sqlalchemy import inspect

def migrate_to_bank_based():
    """Perform database migration to bank-based system"""
    with app.app_context():
        print("🔄 Starting migration to bank-based template system...")
        
        # Create all tables (this will add new columns)
        db.create_all()
        print("✓ Database schema updated")
        
        # Delete old templates (property-based)
        print("\n🗑️  Removing old property-based templates...")
        old_templates = ReportTemplate.query.all()
        for template in old_templates:
            db.session.delete(template)
        db.session.commit()
        print(f"✓ Removed {len(old_templates)} old templates")
        
        # Initialize new bank-based templates
        print("\n📝 Initializing bank-based templates...")
        initialize_default_templates()
        
        # Get the default template
        default_template = ReportTemplate.query.filter_by(is_default=True).first()
        
        if default_template:
            print(f"✓ Default template found: {default_template.name} ({default_template.bank_name})")
            
            # Update existing valuations without a template
            valuations_without_template = LandValuation.query.filter_by(template_id=None).all()
            
            if valuations_without_template:
                print(f"\n🔧 Updating {len(valuations_without_template)} existing valuations...")
                for valuation in valuations_without_template:
                    valuation.template_id = default_template.id
                    if not valuation.bank_name:
                        valuation.bank_name = default_template.bank_name
                
                db.session.commit()
                print(f"✓ Updated {len(valuations_without_template)} valuations with default template")
            else:
                print("✓ All valuations already have templates assigned")
                
            # Update valuations that have old template_id but no bank_name
            valuations_without_bank = LandValuation.query.filter(
                LandValuation.bank_name.is_(None)
            ).all()
            
            if valuations_without_bank:
                print(f"\n🔧 Assigning bank names to {len(valuations_without_bank)} valuations...")
                for valuation in valuations_without_bank:
                    if valuation.template_id:
                        template = ReportTemplate.query.get(valuation.template_id)
                        if template:
                            valuation.bank_name = template.bank_name
                        else:
                            valuation.bank_name = default_template.bank_name
                            valuation.template_id = default_template.id
                    else:
                        valuation.bank_name = default_template.bank_name
                        valuation.template_id = default_template.id
                
                db.session.commit()
                print(f"✓ Assigned bank names to {len(valuations_without_bank)} valuations")
        else:
            print("⚠ Warning: No default template found. Please check template initialization.")
        
        # Display summary
        print("\n" + "="*70)
        print("📊 MIGRATION SUMMARY")
        print("="*70)
        
        template_count = ReportTemplate.query.count()
        valuation_count = LandValuation.query.count()
        
        print(f"Total Bank Templates: {template_count}")
        print(f"Total Valuations: {valuation_count}")
        
        print("\n📋 Available Bank Templates:")
        templates = ReportTemplate.query.order_by(ReportTemplate.bank_name).all()
        for template in templates:
            status = "✓ DEFAULT" if template.is_default else "  Active" if template.is_active else "  Inactive"
            print(f"  {status} | {template.bank_name}")
            print(f"           {template.description}")
            print(f"           File: {template.template_file}")
            print()
        
        print("="*70)
        print("✅ Migration to bank-based system completed successfully!")
        print("="*70)
        print("\n💡 Next Steps:")
        print("   1. Start your Flask application: python3 app.py")
        print("   2. Create a new valuation and select a bank")
        print("   3. The appropriate template will be auto-selected")
        print("   4. Existing valuations have been assigned default bank")
        print()
        print("🏦 Supported Banks:")
        print("   • Ujjivan Small Finance Bank")
        print("   • Bank of Maharashtra")
        print("   • DCB Bank")
        print("   • State Bank of India")
        print("   • HDFC Bank")
        print("   • ICICI Bank")
        print("   • Axis Bank")
        print("   • Punjab National Bank")
        print("   • Bank of Baroda")
        print("   • Kotak Mahindra Bank")
        print("   • Other Banks (Default)")
        print()

if __name__ == '__main__':
    try:
        migrate_to_bank_based()
    except Exception as e:
        print(f"\n❌ Migration failed with error:")
        print(f"   {str(e)}")
        print("\n💡 Troubleshooting:")
        print("   1. Make sure your Flask app is not running")
        print("   2. Backup your database before running migration")
        print("   3. Check if all dependencies are installed")
        print("   4. Verify app.py has been updated with bank_name fields")
        import traceback
        traceback.print_exc()

