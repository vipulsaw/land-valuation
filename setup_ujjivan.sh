#!/bin/bash

# Ujjivan Small Finance Bank Setup Script
# This script will set up the Ujjivan custom template system

echo "=============================================="
echo "  Ujjivan Small Finance Bank Setup"
echo "=============================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo -e "${RED}❌ Error: app.py not found. Please run this script from the land-valuation directory.${NC}"
    exit 1
fi

echo -e "${YELLOW}📋 Pre-flight Checks${NC}"
echo "-------------------------------------------"

# Check if Python is available
if command -v python3 &> /dev/null; then
    echo -e "${GREEN}✓${NC} Python3 is installed"
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    echo -e "${GREEN}✓${NC} Python is installed"
    PYTHON_CMD="python"
else
    echo -e "${RED}❌ Python is not installed${NC}"
    exit 1
fi

# Check if virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo -e "${YELLOW}⚠${NC}  Virtual environment not activated"
    echo "   Attempting to activate..."
    if [ -d "venv" ]; then
        source venv/bin/activate
        echo -e "${GREEN}✓${NC} Virtual environment activated"
    else
        echo -e "${RED}❌ Virtual environment not found. Please activate it manually.${NC}"
        exit 1
    fi
else
    echo -e "${GREEN}✓${NC} Virtual environment is active"
fi

# Check if database exists
if [ -f "land_valuation.db" ]; then
    echo -e "${GREEN}✓${NC} Database file found"
else
    echo -e "${YELLOW}⚠${NC}  Database file not found. It will be created."
fi

echo ""
echo -e "${YELLOW}📦 Backing Up Database${NC}"
echo "-------------------------------------------"

# Backup database if it exists
if [ -f "land_valuation.db" ]; then
    BACKUP_FILE="land_valuation.db.backup.$(date +%Y%m%d_%H%M%S)"
    cp land_valuation.db "$BACKUP_FILE"
    echo -e "${GREEN}✓${NC} Database backed up to: $BACKUP_FILE"
else
    echo -e "${YELLOW}⚠${NC}  No database to backup"
fi

echo ""
echo -e "${YELLOW}🔄 Running Migration${NC}"
echo "-------------------------------------------"

# Run the migration script
$PYTHON_CMD migrate_ujjivan_fields.py

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓${NC} Migration completed successfully"
else
    echo -e "${RED}❌ Migration failed${NC}"
    echo "Please check the error messages above and try again."
    exit 1
fi

echo ""
echo -e "${YELLOW}🔍 Verifying Installation${NC}"
echo "-------------------------------------------"

# Check if template files exist
if [ -f "templates/ujjivan_valuation_form.html" ]; then
    echo -e "${GREEN}✓${NC} Ujjivan form template found"
else
    echo -e "${RED}❌ Ujjivan form template not found${NC}"
fi

if [ -f "templates/ujjivan_report.html" ]; then
    echo -e "${GREEN}✓${NC} Ujjivan report template found"
else
    echo -e "${RED}❌ Ujjivan report template not found${NC}"
fi

echo ""
echo "=============================================="
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo "=============================================="
echo ""
echo "Next Steps:"
echo "1. Start your Flask application:"
echo "   $PYTHON_CMD app.py"
echo ""
echo "2. Access the Ujjivan form at:"
echo "   http://localhost:5000/valuation/new?bank=ujjivan"
echo ""
echo "3. Or select 'Ujjivan Small Finance Bank' from the"
echo "   bank dropdown in the regular form"
echo ""
echo "📚 For detailed documentation, see:"
echo "   UJJIVAN_SETUP_GUIDE.md"
echo ""
echo "=============================================="

