# Troubleshooting Ujjivan Form Submission Errors

## Quick Diagnostic

Run this command first to check your setup:

```bash
python3 check_ujjivan_setup.py
```

This will tell you exactly what's missing.

---

## Common Errors and Solutions

### Error 1: "Column not found" or "no such column"

**Example Error:**
```
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such column: land_valuation.vendor_name
```

**Cause:** The Ujjivan database fields haven't been added yet.

**Solution:**
```bash
# Stop your Flask app first (Ctrl+C)

# Backup database
cp land_valuation.db land_valuation.db.backup

# Run migration
python3 migrate_ujjivan_fields.py

# Restart app
python3 app.py
```

---

### Error 2: "NOT NULL constraint failed"

**Example Error:**
```
sqlite3.IntegrityError: NOT NULL constraint failed: land_valuation.plot_area_sqm
```

**Cause:** A required field is empty in the form.

**Required Fields:**
- Valuation Purpose
- Inspection Date
- Valuation Date
- Valuation Requested By
- Client Name
- Property Owner
- Property Address
- Property Type
- Plot Area (Sqm)
- Plot Area (Sqft)
- Land Value
- Total Value

**Solution:** Make sure all required fields (marked with *) are filled in the form.

---

### Error 3: "Invalid date format"

**Example Error:**
```
ValueError: time data '01-01-2026' does not match format '%Y-%m-%d'
```

**Cause:** Date fields are in wrong format.

**Solution:** Dates should be in YYYY-MM-DD format (e.g., 2026-01-02).

---

### Error 4: "Template not found"

**Example Error:**
```
jinja2.exceptions.TemplateNotFound: ujjivan_valuation_form.html
```

**Cause:** Template files are missing.

**Solution:**
```bash
# Check if files exist
ls -la templates/ujjivan*.html

# If missing, the files should be in templates folder:
# - templates/ujjivan_valuation_form.html
# - templates/ujjivan_report.html
```

---

### Error 5: Form doesn't redirect to Ujjivan

**Cause:** JavaScript not loading or bank name mismatch.

**Solution:**
1. Clear browser cache (Ctrl+Shift+Delete)
2. Hard refresh (Ctrl+F5)
3. Check browser console (F12 → Console) for errors
4. Ensure bank name is exactly "Ujjivan Small Finance Bank"

---

### Error 6: "Error processing dates or photos"

**Cause:** Date format issue or photo upload problem.

**Solution:**
1. Check date format is YYYY-MM-DD
2. Ensure photos are valid image files (JPG, PNG)
3. Check photo file size (should be < 16MB total)
4. Verify uploads folder has write permissions

---

### Error 7: "Error saving valuation"

**Cause:** Database constraint violation or missing required field.

**Solution:**
1. Check all required fields are filled
2. Verify numeric fields have valid numbers
3. Check database migration completed successfully
4. Look at the specific error message for details

---

## Step-by-Step Troubleshooting

### Step 1: Run Diagnostic

```bash
cd land-valuation
python3 check_ujjivan_setup.py
```

This will show you:
- ✓ Template files exist
- ✓ Database columns exist
- ✗ What's missing

### Step 2: If Database Columns Missing

```bash
# Backup first!
cp land_valuation.db land_valuation.db.backup

# Run migration
python3 migrate_ujjivan_fields.py

# Should see output like:
# ✓ Added column: vendor_name
# ✓ Added column: borrower_name
# ...
# ✅ Migration completed successfully!
```

### Step 3: If Template Files Missing

Check that these files exist:
- `templates/ujjivan_valuation_form.html` (49 KB)
- `templates/ujjivan_report.html` (33 KB)

If missing, they need to be recreated.

### Step 4: Restart Application

```bash
# Stop app (Ctrl+C)
# Start app
python3 app.py

# Should see:
# * Running on http://127.0.0.1:5000
```

### Step 5: Test Form

```bash
# Open browser
http://localhost:5000/valuation/new?bank=ujjivan

# Fill out form
# Submit
# Check for errors
```

---

## Viewing Detailed Errors

### In Browser

1. Open Developer Tools (F12)
2. Go to Console tab
3. Look for red error messages
4. Copy the full error message

### In Flask Terminal

Look at the terminal where Flask is running:
```
[2026-01-02 15:18:00,207] ERROR in app: Exception on /valuation/new [POST]
Traceback (most recent call last):
  ...
  [Full error message here]
```

### In Browser Flash Messages

After submitting, look for red error messages at the top of the page.

---

## Manual Database Check

To manually verify database columns:

```bash
# Open database
sqlite3 land_valuation.db

# List all columns in land_valuation table
.schema land_valuation

# Check for specific column
PRAGMA table_info(land_valuation);

# Exit
.quit
```

Look for columns like:
- vendor_name
- borrower_name
- developer_name
- etc.

---

## Getting Help

When asking for help, provide:

1. **Error Message**: Full error from browser or terminal
2. **Diagnostic Output**: Result of `check_ujjivan_setup.py`
3. **Steps Taken**: What you've tried so far
4. **Browser Console**: Any JavaScript errors (F12 → Console)
5. **Flask Version**: Output of `python3 --version`

### Example Help Request:

```
I'm getting an error when submitting the Ujjivan form:

Error Message:
[paste full error here]

Diagnostic Output:
[paste output of check_ujjivan_setup.py]

Steps Taken:
1. Ran migration script
2. Restarted Flask app
3. Cleared browser cache

Browser Console:
[paste any JavaScript errors]

Flask Version: Python 3.12
```

---

## Prevention Checklist

Before using Ujjivan form:

- [ ] Run `check_ujjivan_setup.py` - all checks pass
- [ ] Database backup created
- [ ] Migration script completed successfully
- [ ] Flask app restarted
- [ ] Template files exist
- [ ] Browser cache cleared
- [ ] Test form loads at `/valuation/new?bank=ujjivan`
- [ ] All required fields visible
- [ ] Test submission with dummy data

---

## Quick Fixes

### Reset Everything

If nothing works, reset:

```bash
# 1. Stop Flask app
# Ctrl+C

# 2. Restore backup
cp land_valuation.db.backup land_valuation.db

# 3. Run migration again
python3 migrate_ujjivan_fields.py

# 4. Restart app
python3 app.py

# 5. Clear browser cache
# Ctrl+Shift+Delete

# 6. Test again
http://localhost:5000/valuation/new?bank=ujjivan
```

### Force Recreate Database Columns

If migration says columns exist but form still fails:

```bash
# Check current schema
sqlite3 land_valuation.db "PRAGMA table_info(land_valuation);" > schema_before.txt

# Run migration
python3 migrate_ujjivan_fields.py

# Check schema again
sqlite3 land_valuation.db "PRAGMA table_info(land_valuation);" > schema_after.txt

# Compare
diff schema_before.txt schema_after.txt
```

---

## Contact Information

If you continue to have issues:

1. Check all documentation files
2. Review error messages carefully
3. Run diagnostic script
4. Check database schema
5. Verify template files exist

---

**Last Updated**: January 2, 2026  
**Version**: 1.0

