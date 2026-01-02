# 🚀 Quick Start: Bank-Based Templates

## ⚡ 2-Minute Setup

### Step 1: Backup (30 seconds)
```bash
cd /var/test-02jan2026/land-valuation
cp instance/land_valuation.db instance/land_valuation.db.backup
```

### Step 2: Migrate (1 minute)
```bash
python3 migrate_to_bank_based.py
```

Expected output:
```
✅ Migration to bank-based system completed successfully!
```

### Step 3: Start App (30 seconds)
```bash
python3 app.py
```

## ✅ Done!

Your system now uses bank-based templates!

---

## 🎯 How to Use

### Creating a Valuation

1. Login to your account
2. Click **"New Valuation"**
3. **NEW!** Select bank from dropdown:
   - Ujjivan Small Finance Bank
   - Bank of Maharashtra
   - DCB Bank
   - etc.
4. Fill valuation details
5. Submit
6. Download PDF in bank-specific format!

---

## 🏦 Available Banks

1. **Ujjivan Small Finance Bank** ⭐
2. **Bank of Maharashtra** ⭐
3. **DCB Bank** ⭐
4. State Bank of India
5. HDFC Bank
6. ICICI Bank
7. Axis Bank
8. Punjab National Bank
9. Bank of Baroda
10. Kotak Mahindra Bank
11. Other Banks (Default)

---

## 💡 Key Changes

### What's Different?

**BEFORE:**
```
Select: "Residential Property Report"
```

**NOW:**
```
Select: "Ujjivan Small Finance Bank"
```

### Why Better?

✅ **Simpler** - Just pick the bank  
✅ **Automatic** - Template auto-selected  
✅ **Professional** - Bank-specific format  

---

## 🔧 Troubleshooting

### Migration Error?
```bash
# Make sure app is not running
# Check you're in correct directory
pwd  # Should show: /var/test-02jan2026/land-valuation
```

### App Won't Start?
```bash
# Test imports
python3 test_import.py

# Check logs
python3 app.py 2>&1 | tee app.log
```

### Bank Not Showing?
```python
# Check templates
python3 -c "from app import app, ReportTemplate; \
with app.app_context(): \
    print([t.bank_name for t in ReportTemplate.query.all()])"
```

---

## 📚 Documentation

- **Quick Start:** This file
- **Full Guide:** `BANK_BASED_TEMPLATES.md`
- **Changes:** `CHANGES_SUMMARY.md`

---

## 🎉 Success!

Your system is now using bank-based templates!

**Test it:**
1. Create new valuation
2. Select "Ujjivan Small Finance Bank"
3. Generate PDF
4. See bank-specific format!

---

**Need Help?** Check `BANK_BASED_TEMPLATES.md` for detailed documentation.

