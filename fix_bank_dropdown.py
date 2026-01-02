"""
Fix bank names in dropdown - Ensure all banks are properly set up
"""

from app import app, db, ReportTemplate

with app.app_context():
    print("🔧 Fixing bank names in templates...")
    print()
    
    # Check current templates
    templates = ReportTemplate.query.all()
    print(f"Current templates: {len(templates)}")
    
    if len(templates) == 0:
        print("⚠️  No templates found. Creating bank templates...")
        
        # Create bank templates
        banks = [
            ('Ujjivan Small Finance Bank', 'ujjivan_report.html', 'Professional report format for Ujjivan Small Finance Bank'),
            ('Bank of Maharashtra', 'bank_of_maharashtra_report.html', 'Standard report format for Bank of Maharashtra'),
            ('DCB Bank', 'dcb_bank_report.html', 'Professional report format for DCB Bank'),
            ('State Bank of India', 'sbi_report.html', 'Comprehensive report format for State Bank of India'),
            ('HDFC Bank', 'hdfc_report.html', 'Professional report format for HDFC Bank'),
            ('ICICI Bank', 'icici_report.html', 'Standard report format for ICICI Bank'),
            ('Axis Bank', 'axis_report.html', 'Professional report format for Axis Bank'),
            ('Punjab National Bank', 'pnb_report.html', 'Standard report format for Punjab National Bank'),
            ('Bank of Baroda', 'bob_report.html', 'Professional report format for Bank of Baroda'),
            ('Kotak Mahindra Bank', 'kotak_report.html', 'Standard report format for Kotak Mahindra Bank'),
            ('Other Banks', 'professional_report.html', 'Generic professional report for other banks'),
        ]
        
        for idx, (bank_name, template_file, description) in enumerate(banks):
            template = ReportTemplate(
                name=f"{bank_name} Report",
                bank_name=bank_name,
                description=description,
                template_file=template_file,
                is_active=True,
                is_default=(bank_name == 'Other Banks')
            )
            db.session.add(template)
            print(f"  ✓ Created: {bank_name}")
        
        db.session.commit()
        print(f"\n✅ Created {len(banks)} bank templates!")
        
    else:
        # Check if templates have bank_name
        templates_without_bank = [t for t in templates if not hasattr(t, 'bank_name') or not t.bank_name]
        
        if templates_without_bank:
            print(f"⚠️  Found {len(templates_without_bank)} templates without bank_name")
            print("These templates need bank_name field. Run migration script.")
        else:
            print("✅ All templates have bank names!")
    
    # Display final list
    print("\n" + "="*70)
    print("📋 BANKS IN DROPDOWN")
    print("="*70)
    
    templates = ReportTemplate.query.filter_by(is_active=True).order_by(ReportTemplate.bank_name).all()
    
    for template in templates:
        marker = " ⭐ (Default)" if template.is_default else ""
        print(f"  • {template.bank_name}{marker}")
    
    print("="*70)
    print(f"\n✅ Total: {len(templates)} banks available in dropdown")
    print("\n💡 Restart your Flask app to see the changes!")

