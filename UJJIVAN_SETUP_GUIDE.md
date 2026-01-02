# Ujjivan Small Finance Bank - Custom Template Setup Guide

## Overview
This guide will help you set up and use the custom Ujjivan Small Finance Bank valuation form and report template.

## Features Added

### 1. Custom Ujjivan Form (`ujjivan_valuation_form.html`)
- Specialized form fields matching Ujjivan's requirements
- Additional fields for vendor information, borrower details, developer name
- Enhanced property identification fields
- Detailed technical specifications
- Construction stage tracking
- Work status monitoring

### 2. Custom Ujjivan Report Template (`ujjivan_report.html`)
- Professional report layout matching Ujjivan's format
- Orange/red color scheme (#FF6B35)
- Comprehensive property details table
- Technical details with checkbox options
- Statutory approval section
- Detailed valuation calculation tables
- Construction stage status tracking
- Declaration and signature sections

### 3. Additional Database Fields
45+ new fields added to support Ujjivan-specific requirements including:
- Vendor and borrower information
- Property demarcation details
- Zonal classification
- Amenities tracking
- Site dimensions
- Construction quality indicators
- Statutory approvals
- Detailed valuation breakdown

## Installation Steps

### Step 1: Stop Your Application
If your Flask application is running, stop it first:
```bash
# Press Ctrl+C in the terminal where the app is running
```

### Step 2: Backup Your Database
**IMPORTANT**: Always backup before running migrations!
```bash
cd land-valuation
cp land_valuation.db land_valuation.db.backup
```

### Step 3: Run the Migration
```bash
python3 migrate_ujjivan_fields.py
```

You should see output like:
```
🔄 Starting Ujjivan fields migration...
✓ Added column: vendor_name
✓ Added column: borrower_name
...
✅ Migration completed successfully!
```

### Step 4: Restart Your Application
```bash
python3 app.py
```

## How to Use

### Method 1: Direct URL Access
Navigate directly to the Ujjivan form:
```
http://your-server:5000/valuation/new?bank=ujjivan
```

### Method 2: Bank Selection (Auto-Redirect)
1. Go to the regular valuation form: `/valuation/new`
2. Select "Ujjivan Small Finance Bank" from the bank dropdown
3. You will be automatically redirected to the Ujjivan-specific form

### Method 3: From Dashboard
1. Click "New Valuation" from the dashboard
2. Select "Ujjivan Small Finance Bank" from the dropdown
3. Auto-redirect to Ujjivan form

## Form Sections

### Section 1: Basic Information
- Vendor Name
- Applicant/Client Name
- Purpose of Valuation
- Reference/Case Number
- Case Type/Loan Type
- Contact Person

### Section 2: Property Identification
- Inspection and Valuation Dates
- Property Owner
- Borrower Name
- Developer Name
- Project Name
- Site/Villa/CTS Number
- Property Address
- Property Demarcation Status
- Nearest Landmark

### Section 3: Location & Amenities
- Access Road Name
- Property Type
- Zonal Classification
- Habitation Percentage
- Water Facility
- Underground Drainage
- Tar Roads
- Electricity
- Locality Classification
- Surrounding Locality
- Nearby Amenities
- Distance from Branch

### Section 4: Property Boundaries
- East, West, North, South Boundaries
- Site Dimensions (E-W and N-S)

### Section 5: Technical Details
- Type of Construction (RCC Framed/Load Bearing/Composite/Pre Engineered)
- Quality of Construction (Very Good/Good/Average/Poor)
- Electrical Fittings (Standard/Superior)
- Sanitary Fittings (Standard/Superior)
- Lifts (Yes/No)
- Compound Wall (Yes/No)
- Super Structure
- Roof Type
- Doors & Windows
- Flooring
- Elevation Quality
- Interiors Quality
- Other Amenities
- Year of Construction
- Age of Building
- Future Life

### Section 6: Statutory Details
- Total Plot Area (Schedule)
- Applicant Plot Area
- Plot Area (Sqm and Sqft)
- Total Built-up Area (Schedule)
- Built-up Area (Actual)
- Carpet Area
- Statutory Approval Details
- Approval Number and Date
- FSI Permitted
- Occupation Certificate

### Section 7: Valuation Calculation
- Land Area for Valuation
- Rate per Sqft
- Land Value
- Ground Floor Area & Rate
- First Floor Area & Rate
- Depreciation Percentage
- Net Construction Value
- Total Fair Market Value
- Distress Sale Value (75%)

### Section 8: Construction Stage
- Plinth Level (To be Started/Under Progress/Completed)
- Framed Structure
- Super Structure
- Plastering and Finishing
- Flooring

### Section 9: Work Status
- Civil Progress Percentage
- Interiors Progress Percentage

### Section 10: Additional Information
- Documents Provided
- Geographical Location (Latitude/Longitude)
- Property Photos
- Additional Notes/Remarks
- Report Prepared By

## Report Output

The generated PDF will include:
- Professional header with Ujjivan branding
- Comprehensive property details in tabular format
- Technical specifications with visual checkboxes
- Detailed valuation breakdown
- Construction stage tracking
- Fair Market Value definition
- Declaration section
- Signature area with valuer details

## Color Scheme
- Primary Color: #FF6B35 (Orange-Red)
- Secondary Color: #E55A2B (Darker Orange)
- Background: White with light gray accents
- Text: Black (#000)

## Troubleshooting

### Issue: Migration fails
**Solution**: 
1. Make sure the Flask app is not running
2. Check database permissions
3. Verify you're in the correct directory

### Issue: Form doesn't redirect to Ujjivan
**Solution**:
1. Clear browser cache
2. Check that JavaScript is enabled
3. Verify the bank name is exactly "Ujjivan Small Finance Bank"

### Issue: Fields not saving
**Solution**:
1. Verify migration was successful
2. Check that all new columns exist in the database
3. Review browser console for JavaScript errors

### Issue: PDF generation fails
**Solution**:
1. Check WeasyPrint is installed: `pip install weasyprint`
2. Verify template file exists: `templates/ujjivan_report.html`
3. Check application logs for specific errors

## Database Schema

New columns added to `land_valuation` table:
```sql
vendor_name VARCHAR(200)
borrower_name VARCHAR(200)
developer_name VARCHAR(200)
contact_person VARCHAR(200)
property_demarcated VARCHAR(50)
place VARCHAR(100)
nearest_landmark VARCHAR(200)
zonal_classification VARCHAR(100)
habitation VARCHAR(50)
water_facility VARCHAR(50)
underground_drainage VARCHAR(50)
tar_roads VARCHAR(50)
electricity VARCHAR(50)
surrounding_locality VARCHAR(200)
nearby_amenities VARCHAR(500)
site_dimension_ew VARCHAR(50)
site_dimension_ns VARCHAR(50)
sanitary_fittings VARCHAR(100)
lifts VARCHAR(50)
super_structure VARCHAR(500)
roof_type VARCHAR(200)
elevation_quality VARCHAR(50)
interiors_quality VARCHAR(50)
total_plot_area_schedule VARCHAR(50)
buildup_area_schedule_sqm FLOAT
buildup_area_schedule_sqft FLOAT
statutory_approval VARCHAR(500)
approval_number VARCHAR(200)
fsi_permitted VARCHAR(100)
occupation_certificate VARCHAR(200)
land_area_valuation FLOAT
gf_rate FLOAT
gf_value FLOAT
ff_rate FLOAT
ff_value FLOAT
depreciation_percentage FLOAT
net_construction_value FLOAT
documents_provided TEXT
plinth_level_status VARCHAR(50)
framed_structure_status VARCHAR(50)
super_structure_status VARCHAR(50)
plastering_status VARCHAR(50)
flooring_status VARCHAR(50)
civil_progress VARCHAR(50)
interiors_progress VARCHAR(50)
report_prepared_by VARCHAR(200)
```

## Testing

### Test Checklist:
- [ ] Migration runs successfully
- [ ] Ujjivan form loads at `/valuation/new?bank=ujjivan`
- [ ] Auto-redirect works from bank dropdown
- [ ] All form fields are visible and functional
- [ ] Form submission saves data correctly
- [ ] PDF generates with Ujjivan template
- [ ] HTML preview shows correct template
- [ ] All Ujjivan-specific fields appear in report
- [ ] Other banks still use default template
- [ ] Existing valuations are not affected

## Support

If you encounter issues:
1. Check the application logs
2. Verify database migration completed
3. Ensure all template files exist
4. Review browser console for errors
5. Check that WeasyPrint is properly installed

## Notes

- The Ujjivan form and template are only used when "Ujjivan Small Finance Bank" is selected
- All other banks continue to use the existing default template
- Existing valuation records are not affected by this update
- The migration is backward compatible
- New fields are optional and won't break existing functionality

## Future Enhancements

Potential improvements:
- Add more bank-specific templates
- Implement template preview before submission
- Add field validation specific to Ujjivan requirements
- Create template comparison view
- Add bulk import for Ujjivan valuations
- Implement custom calculation rules per bank

---

**Version**: 1.0  
**Last Updated**: January 2, 2026  
**Author**: AI Assistant  
**Status**: Ready for Production

