# 🚀 Quick Start: Multi-Template System

## ⚡ 3-Minute Setup

### Step 1: Backup Your Database (30 seconds)

```bash
cd land-valuation
# Backup your database
copy instance\land_valuation.db instance\land_valuation.db.backup
```

### Step 2: Run Migration (1 minute)

```bash
python migrate_database.py
```

You should see:
```
✓ Database schema updated
✓ Default templates initialized successfully!
✓ Updated X valuations with default template
✅ Migration completed successfully!
```

### Step 3: Start Application (30 seconds)

```bash
python app.py
```

### Step 4: Test It! (1 minute)

1. Open browser → `http://localhost:5000`
2. Login to your account
3. Click **"Templates"** in navigation
4. See 5 available templates!
5. Click **"Preview"** on any template
6. Create a **New Valuation** and select a template

## ✅ You're Done!

Your system now supports multiple templates!

## 🎯 What You Get

### 5 Ready-to-Use Templates:

1. **Professional Banking Report** ⭐ (Default)
   - Multi-page comprehensive format
   - Perfect for banks and financial institutions

2. **Compact Report** 📄
   - Single-page quick format
   - Great for preliminary assessments

3. **Residential Property Report** 🏠
   - Specialized for homes and apartments
   - Modern colorful design

4. **Detailed Technical Report** 🔧
   - Extended technical specifications
   - For complex properties

5. **Commercial Property Report** 🏢
   - Business property focused
   - Commercial metrics

## 📝 How to Use

### Creating New Valuation with Template:

```
1. Dashboard → New Valuation
2. [NEW!] Select template from dropdown
3. Fill valuation details
4. Submit
5. Download PDF in selected format!
```

### Viewing All Templates:

```
Navigation Bar → Templates
OR
Visit: http://localhost:5000/templates
```

### Preview Before Using:

```
Templates Page → Click "Preview" button
See sample report with dummy data
```

## 🎨 Customize Your Own Template

### Create `templates/my_template.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Custom Report</title>
    <style>
        @page { size: A4; margin: 1.5cm; }
        body { font-family: Arial; font-size: 11pt; }
    </style>
</head>
<body>
    <h1>{{ valuation.client_name }}</h1>
    <p>Property: {{ valuation.property_address }}</p>
    <p>Value: ₹{{ "{:,.2f}".format(valuation.total_value) }}</p>
    
    {% for photo in encoded_photos %}
        <img src="{{ photo }}" style="max-width: 400px;">
    {% endfor %}
</body>
</html>
```

### Add to Database (Python shell):

```python
from app import app, db, ReportTemplate

with app.app_context():
    template = ReportTemplate(
        name='My Custom Template',
        description='My special format',
        template_file='my_template.html',
        is_active=True,
        is_default=False
    )
    db.session.add(template)
    db.session.commit()
    print("✓ Template added!")
```

Restart app → New template appears!

## 🔍 Quick Reference

### Available Template Variables:

```python
valuation.client_name
valuation.property_address
valuation.property_type
valuation.total_value
valuation.plot_area_sqft
valuation.built_up_area
# ... and 50+ more fields!

encoded_photos  # List of base64 images
logo_base64     # Company logo
current_user    # Logged-in user
```

### Template Styling Tips:

```css
/* PDF-friendly styles */
@page { size: A4; margin: 1.5cm; }
body { font-size: 10pt; line-height: 1.4; }

/* Avoid complex CSS */
/* ✓ Good: Simple borders, basic layouts */
/* ✗ Avoid: Flexbox, Grid, Transform, Animation */
```

## 🐛 Troubleshooting

### Migration Failed?
```bash
# Check if app is running (close it first)
# Verify Python version: python --version
# Check dependencies: pip list | findstr Flask
```

### Template Not Showing?
```python
# Check in Python shell:
from app import app, ReportTemplate
with app.app_context():
    templates = ReportTemplate.query.all()
    for t in templates:
        print(f"{t.name}: Active={t.is_active}")
```

### PDF Not Generating?
```
1. Test HTML version first: /view-report/<id>
2. Check WeasyPrint: pip show weasyprint
3. Simplify CSS (remove complex styles)
4. Check Flask logs for errors
```

## 📚 Learn More

- Full documentation: `MULTI_TEMPLATE_GUIDE.md`
- Template examples: `templates/` folder
- Database schema: Check migration script

## 💡 Pro Tips

1. **Always preview** templates before using
2. **Test with sample data** using preview feature
3. **Keep backups** of your database
4. **Start simple** when creating custom templates
5. **Use existing templates** as reference

## 🎉 Next Steps

- [ ] Create a custom template for your specific needs
- [ ] Set up templates for different clients
- [ ] Customize template colors and branding
- [ ] Add your company logo to reports
- [ ] Share templates with team members

---

**Need Help?** Check `MULTI_TEMPLATE_GUIDE.md` for detailed documentation!

**Questions?** Review the template examples in `templates/` folder!

