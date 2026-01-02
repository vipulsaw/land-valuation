# Fix for "NOT NULL constraint failed: valuation_requested_by" Error

## Problem
When submitting the Ujjivan Small Finance Bank form, you get this error:
```
NOT NULL constraint failed: land_valuation.valuation_requested_by
```

## Cause
The `valuation_requested_by` field was missing from the Ujjivan form template.

## Solution Applied
Added the missing field to `templates/ujjivan_valuation_form.html`:

```html
<div class="form-group">
    <label for="valuation_requested_by">
        <i class="fas fa-building"></i> Valuation Requested By <span style="color: red;">*</span>
    </label>
    <input type="text" 
           id="valuation_requested_by" 
           name="valuation_requested_by" 
           value="Ujjivan Small Finance Bank" 
           required>
</div>
```

## How to Deploy on Ubuntu Server

### Step 1: Upload the Fixed File

**Option A: Using SCP (from your local machine)**
```bash
scp land-valuation/templates/ujjivan_valuation_form.html root@your-server-ip:/var/test-02jan2026/land-valuation/templates/
```

**Option B: Using Git (if you have a repository)**
```bash
# On your local machine
cd land-valuation
git add templates/ujjivan_valuation_form.html
git commit -m "Fix: Add missing valuation_requested_by field to Ujjivan form"
git push

# On your Ubuntu server
cd /var/test-02jan2026/land-valuation
git pull
```

**Option C: Manual Edit on Server**
```bash
# SSH into your server
ssh root@your-server-ip

# Navigate to directory
cd /var/test-02jan2026/land-valuation

# Edit the file
nano templates/ujjivan_valuation_form.html

# Find the line with "Purpose of Valuation" (around line 35-38)
# Replace the section as shown in the solution above
# Press Ctrl+X, then Y, then Enter to save
```

### Step 2: Restart Flask Application

```bash
# If Flask is running, stop it (Ctrl+C)
# Then restart
cd /var/test-02jan2026/land-valuation
source venv/bin/activate
python3 app.py
```

### Step 3: Clear Browser Cache

On your browser:
- Press `Ctrl+Shift+Delete`
- Clear cached images and files
- Or do a hard refresh: `Ctrl+F5`

### Step 4: Test the Form

1. Go to: `http://your-server-ip:5000/valuation/new?bank=ujjivan`
2. You should now see the "Valuation Requested By" field
3. It should be pre-filled with "Ujjivan Small Finance Bank"
4. Fill out the form and submit
5. Should work without errors!

## Verification

After deploying, verify the field exists:

```bash
# On your server
cd /var/test-02jan2026/land-valuation
grep -n "valuation_requested_by" templates/ujjivan_valuation_form.html

# Should show the line number where the field appears
```

## What Changed

**Before:**
- Form was missing the `valuation_requested_by` field
- Database requires this field (NOT NULL constraint)
- Form submission failed

**After:**
- Field added with default value "Ujjivan Small Finance Bank"
- Field is marked as required (*)
- Form submission will succeed

## Testing Checklist

After deploying:
- [ ] File uploaded to server
- [ ] Flask app restarted
- [ ] Browser cache cleared
- [ ] Form loads at `/valuation/new?bank=ujjivan`
- [ ] "Valuation Requested By" field is visible
- [ ] Field shows "Ujjivan Small Finance Bank"
- [ ] Form submits successfully
- [ ] No error messages
- [ ] Valuation appears in dashboard

## If Still Having Issues

Check these:
1. File was uploaded correctly
2. Flask app was restarted
3. Browser cache was cleared
4. No typos in the field name
5. Check Flask terminal for other errors

## Quick Deploy Commands

```bash
# Complete deployment in one go:

# SSH into server
ssh root@your-server-ip

# Navigate to directory
cd /var/test-02jan2026/land-valuation

# Backup current file
cp templates/ujjivan_valuation_form.html templates/ujjivan_valuation_form.html.backup

# Upload new file (from your local machine in another terminal)
# scp land-valuation/templates/ujjivan_valuation_form.html root@your-server-ip:/var/test-02jan2026/land-valuation/templates/

# Restart Flask
# Press Ctrl+C to stop current app
source venv/bin/activate
python3 app.py

# Test in browser
# http://your-server-ip:5000/valuation/new?bank=ujjivan
```

---

**Status**: ✅ Fixed  
**Date**: January 2, 2026  
**Issue**: Missing required field  
**Solution**: Added valuation_requested_by field to Ujjivan form

