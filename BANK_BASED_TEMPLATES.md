# 🏦 Bank-Based Template System

## Overview

Your Land Valuation System has been upgraded to use **bank-based templates** instead of property-based templates. Now, when creating a valuation, you select the bank/financial institution, and the appropriate report format is automatically applied!

## 🎯 What Changed

### Before (Property-Based)
```
User selects: "Residential Property Report"
                    ↓
            Generic residential template
```

### After (Bank-Based) ✅
```
User selects: "Ujjivan Small Finance Bank"
                    ↓
            Ujjivan-specific report format
```

## 🏦 Supported Banks

The system now includes templates for 11 banks:

1. **Ujjivan Small Finance Bank** ⭐
2. **Bank of Maharashtra** ⭐
3. **DCB Bank** ⭐
4. **State Bank of India**
5. **HDFC Bank**
6. **ICICI Bank**
7. **Axis Bank**
8. **Punjab National Bank**
9. **Bank of Baroda**
10. **Kotak Mahindra Bank**
11. **Other Banks** (Default)

## 📊 Database Changes

### New Fields

**ReportTemplate Table:**
- Added: `bank_name` - Name of the bank this template is for

**LandValuation Table:**
- Added: `bank_name` - Bank name selected for this valuation

### Updated Relationships
Templates are now uniquely identified by bank name rather than property type.

## 🚀 Migration Steps

### Step 1: Backup Database
```bash
cd /var/test-02jan2026/land-valuation
cp instance/land_valuation.db instance/land_valuation.db.backup_before_bank_based
```

### Step 2: Run Migration
```bash
python3 migrate_to_bank_based.py
```

Expected output:
```
🔄 Starting migration to bank-based template system...
✓ Database schema updated
✓ Removed X old templates
✓ 11 bank-specific templates initialized successfully!
✅ Migration to bank-based system completed successfully!
```

### Step 3: Start Application
```bash
python3 app.py
```

### Step 4: Test
1. Login to your account
2. Click "New Valuation"
3. See bank selection dropdown
4. Select a bank (e.g., "Ujjivan Small Finance Bank")
5. Fill valuation details
6. Submit and download PDF

## 📝 How It Works

### Creating a Valuation

```
1. User opens valuation form
   ↓
2. Selects bank from dropdown
   ↓
3. System finds matching template
   ↓
4. Saves valuation with bank_name
   ↓
5. PDF generated using bank's template
```

### Template Selection Logic

```python
# When user selects "Ujjivan Small Finance Bank"
bank_name = "Ujjivan Small Finance Bank"

# System finds template
template = ReportTemplate.query.filter_by(
    bank_name=bank_name,
    is_active=True
).first()

# Uses template: ujjivan_report.html
```

## 🎨 Customizing Bank Templates

### Option 1: Modify Existing Template

Edit the bank-specific template file:
```bash
nano templates/ujjivan_report.html
```

Make your changes (colors, layout, sections, etc.)

Restart the app - Done!

### Option 2: Create New Bank Template

1. **Create template file:**
```bash
cp templates/professional_report.html templates/my_bank_report.html
```

2. **Add to database:**
```python
from app import app, db, ReportTemplate

with app.app_context():
    template = ReportTemplate(
        name='My Bank Report',
        bank_name='My Bank Name',
        description='Custom template for My Bank',
        template_file='my_bank_report.html',
        is_active=True,
        is_default=False
    )
    db.session.add(template)
    db.session.commit()
```

3. **Restart app** - New bank appears in dropdown!

## 📁 Template Files

```
templates/
├── ujjivan_report.html              # Ujjivan Small Finance Bank
├── bank_of_maharashtra_report.html  # Bank of Maharashtra
├── dcb_bank_report.html             # DCB Bank
├── sbi_report.html                  # State Bank of India
├── hdfc_report.html                 # HDFC Bank
├── icici_report.html                # ICICI Bank
├── axis_report.html                 # Axis Bank
├── pnb_report.html                  # Punjab National Bank
├── bob_report.html                  # Bank of Baroda
├── kotak_report.html                # Kotak Mahindra Bank
└── professional_report.html         # Other Banks (Default)
```

## 🔍 Key Features

### Automatic Template Selection
✅ User selects bank → Template auto-selected  
✅ No need to remember which template to use  
✅ Consistent format for each bank  

### Bank-Specific Customization
✅ Each bank can have unique branding  
✅ Different sections/fields per bank  
✅ Custom calculations if needed  

### Easy Management
✅ Add new banks easily  
✅ Update templates independently  
✅ Deactivate banks if needed  

## 💡 Use Cases

### Use Case 1: Different Banks, Different Formats
```
Ujjivan Bank → Compact 2-page format
DCB Bank → Detailed 5-page format
SBI → Government-style format
```

### Use Case 2: Bank Branding
```
Each template can include:
- Bank-specific colors
- Bank logo requirements
- Specific terminology
- Required sections
```

### Use Case 3: Compliance
```
Different banks have different requirements:
- Specific disclaimers
- Required certifications
- Mandatory fields
- Format specifications
```

## 🎯 Benefits

### For Users
✅ **Simpler Selection** - Just pick the bank  
✅ **No Confusion** - Template auto-selected  
✅ **Faster Workflow** - One less decision to make  

### For Administrators
✅ **Easy Maintenance** - Update per bank  
✅ **Scalable** - Add banks as needed  
✅ **Flexible** - Different formats per bank  

### For Clients (Banks)
✅ **Consistent Reports** - Same format every time  
✅ **Brand Compliance** - Their requirements met  
✅ **Professional** - Tailored to their needs  

## 🔧 Troubleshooting

### Issue: Bank not showing in dropdown
**Check:**
```python
from app import app, ReportTemplate
with app.app_context():
    templates = ReportTemplate.query.all()
    for t in templates:
        print(f"{t.bank_name}: Active={t.is_active}")
```

### Issue: Wrong template being used
**Debug:**
```python
from app import app, LandValuation
with app.app_context():
    val = LandValuation.query.get(VALUATION_ID)
    print(f"Bank: {val.bank_name}")
    print(f"Template: {val.template.template_file if val.template else 'None'}")
```

### Issue: Need to change bank for existing valuation
**Solution:**
```python
from app import app, db, LandValuation, ReportTemplate

with app.app_context():
    val = LandValuation.query.get(VALUATION_ID)
    new_bank = "DCB Bank"
    
    # Update bank name
    val.bank_name = new_bank
    
    # Find and assign new template
    template = ReportTemplate.query.filter_by(bank_name=new_bank).first()
    if template:
        val.template_id = template.id
    
    db.session.commit()
```

## 📊 Migration Impact

### What Happens to Existing Data?

✅ **Existing valuations** - Assigned to "Other Banks" (default)  
✅ **Old templates** - Removed and replaced  
✅ **User data** - Completely safe  
✅ **Photos** - Unaffected  

### Rollback (If Needed)

```bash
# Stop the app
# Restore backup
cp instance/land_valuation.db.backup_before_bank_based instance/land_valuation.db
# Restart app
```

## 🎨 Customization Examples

### Example 1: Add Bank Logo to Template

Edit `templates/ujjivan_report.html`:
```html
<div class="header">
    <img src="data:image/png;base64,UJJIVAN_LOGO_BASE64" alt="Ujjivan Bank">
    <h1>Ujjivan Small Finance Bank</h1>
</div>
```

### Example 2: Bank-Specific Sections

```html
{% if valuation.bank_name == "Ujjivan Small Finance Bank" %}
    <div class="ujjivan-specific-section">
        <!-- Ujjivan-specific content -->
    </div>
{% elif valuation.bank_name == "DCB Bank" %}
    <div class="dcb-specific-section">
        <!-- DCB-specific content -->
    </div>
{% endif %}
```

### Example 3: Bank-Specific Colors

```css
/* In ujjivan_report.html */
:root {
    --bank-primary: #FF6B35;    /* Ujjivan orange */
    --bank-secondary: #004B87;   /* Ujjivan blue */
}

/* In dcb_bank_report.html */
:root {
    --bank-primary: #ED1C24;     /* DCB red */
    --bank-secondary: #000000;   /* DCB black */
}
```

## 📈 Future Enhancements

### Planned Features
- [ ] Bank-specific field requirements
- [ ] Bank logo upload interface
- [ ] Template versioning per bank
- [ ] Bank-specific calculations
- [ ] Multi-language support per bank
- [ ] Bank approval workflow

### Easy to Add
- New banks (just add template + DB entry)
- Bank categories (PSU, Private, NBFC)
- Regional bank support
- International banks

## 📞 Support

### Common Questions

**Q: Can I have multiple templates per bank?**  
A: Yes! Just create multiple ReportTemplate entries with the same bank_name but different template_file names.

**Q: Can I rename a bank?**  
A: Yes, update the bank_name in the ReportTemplate table and existing valuations will still work.

**Q: What if a bank is not listed?**  
A: Select "Other Banks" - it uses the default professional template.

**Q: Can I customize templates per branch?**  
A: Yes! Add branch name to bank_name field: "DCB Bank - Mumbai Branch"

## ✅ Verification Checklist

After migration, verify:

- [ ] All banks appear in dropdown
- [ ] Can create new valuation with bank selection
- [ ] PDF generates with correct template
- [ ] Existing valuations still work
- [ ] Dashboard shows bank names
- [ ] Templates page shows all banks
- [ ] Edit valuation preserves bank selection

## 🎉 Summary

Your system now uses **bank-based templates** which provides:

✅ **Better Organization** - Templates grouped by bank  
✅ **Easier Selection** - Just pick the bank  
✅ **More Flexible** - Different format per bank  
✅ **Scalable** - Easy to add new banks  
✅ **Professional** - Bank-specific branding  

---

**Migration Date**: January 2026  
**Version**: 2.0.0 (Bank-Based)  
**Status**: ✅ Production Ready

**Enjoy your new bank-based template system!** 🏦

