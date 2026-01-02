"""
Quick script to check and fix bank names in templates
"""

from app import app, db, ReportTemplate

with app.app_context():
    print("Checking templates...")
    templates = ReportTemplate.query.all()
    
    print(f"\nFound {len(templates)} templates:")
    print("-" * 70)
    
    for template in templates:
        bank_name = template.bank_name if hasattr(template, 'bank_name') else 'N/A'
        print(f"ID: {template.id}")
        print(f"  Name: {template.name}")
        print(f"  Bank Name: {bank_name}")
        print(f"  Template File: {template.template_file}")
        print(f"  Active: {template.is_active}")
        print(f"  Default: {template.is_default}")
        print()
    
    # Check if bank_name column exists
    from sqlalchemy import inspect
    inspector = inspect(db.engine)
    columns = [col['name'] for col in inspector.get_columns('report_template')]
    
    print("-" * 70)
    print(f"Columns in report_template table: {columns}")
    print(f"Has bank_name column: {'bank_name' in columns}")
    print()
    
    if 'bank_name' not in columns:
        print("❌ ERROR: bank_name column is missing!")
        print("Run: python3 migrate_to_bank_based.py")
    elif len(templates) == 0:
        print("⚠️  No templates found!")
        print("Run: python3 migrate_to_bank_based.py")
    else:
        # Check if any template has null bank_name
        null_banks = [t for t in templates if not t.bank_name]
        if null_banks:
            print(f"⚠️  Found {len(null_banks)} templates with null bank_name")
            print("Run: python3 migrate_to_bank_based.py")
        else:
            print("✅ All templates have bank names!")
            print("\nBank names in dropdown will be:")
            for template in sorted(templates, key=lambda x: x.bank_name):
                marker = " (Default)" if template.is_default else ""
                print(f"  • {template.bank_name}{marker}")

