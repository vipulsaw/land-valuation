# Quick Start Guide - Ujjivan Small Finance Bank

## 🚀 Setup in 3 Steps

### Step 1: Backup Database
```bash
cd land-valuation
cp land_valuation.db land_valuation.db.backup
```

### Step 2: Run Migration
```bash
# Linux/Mac
python3 migrate_ujjivan_fields.py

# Windows
python migrate_ujjivan_fields.py
```

### Step 3: Restart App
```bash
# Linux/Mac
python3 app.py

# Windows
python app.py
```

## 🎯 Quick Access

### Direct URL
```
http://localhost:5000/valuation/new?bank=ujjivan
```

### Or Use Dropdown
1. Go to `/valuation/new`
2. Select "Ujjivan Small Finance Bank"
3. Auto-redirects to Ujjivan form

## 📋 Key Features

✅ **100+ Fields** - Comprehensive property details  
✅ **Custom PDF** - Ujjivan-branded report  
✅ **Auto-Redirect** - Seamless bank selection  
✅ **Backward Compatible** - Other banks unaffected  

## 🔧 Automated Setup

### Linux/Mac
```bash
chmod +x setup_ujjivan.sh
./setup_ujjivan.sh
```

### Windows
```cmd
setup_ujjivan.bat
```

## 📁 New Files Created

- `templates/ujjivan_valuation_form.html` - Custom form
- `templates/ujjivan_report.html` - Custom PDF template
- `migrate_ujjivan_fields.py` - Database migration
- `UJJIVAN_SETUP_GUIDE.md` - Full documentation

## 🎨 Ujjivan Branding

- **Primary Color**: #FF6B35 (Orange-Red)
- **Layout**: Professional tabular format
- **Sections**: 10 major sections
- **Fields**: 45 new database fields

## ⚡ Quick Test

```bash
# 1. Run migration
python3 migrate_ujjivan_fields.py

# 2. Start app
python3 app.py

# 3. Open browser
http://localhost:5000/valuation/new?bank=ujjivan

# 4. Fill form and submit

# 5. Download PDF
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Migration fails | Stop Flask app first |
| Form doesn't load | Clear browser cache |
| PDF generation fails | Install weasyprint |
| Fields not saving | Verify migration success |

## 📚 Full Documentation

See `UJJIVAN_SETUP_GUIDE.md` for complete details.

## ✅ Verification

After setup, verify:
- [ ] Migration completed without errors
- [ ] Ujjivan form loads at `/valuation/new?bank=ujjivan`
- [ ] Form submission works
- [ ] PDF generates with Ujjivan template
- [ ] Other banks still use default template

## 🎉 You're Ready!

Your Ujjivan Small Finance Bank custom template is now active and ready to use!

---

**Need Help?** Check `UJJIVAN_SETUP_GUIDE.md` for detailed instructions.

