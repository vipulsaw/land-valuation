#!/bin/bash

echo "================================================"
echo "  Land Valuation System - Troubleshooting"
echo "================================================"
echo ""

# Check Python version
echo "1. Checking Python version..."
python3 --version
echo ""

# Check if we're in the right directory
echo "2. Checking current directory..."
pwd
if [ -f "app.py" ]; then
    echo "✅ app.py found"
else
    echo "❌ app.py not found - are you in the right directory?"
    exit 1
fi
echo ""

# Check if virtual environment is activated
echo "3. Checking virtual environment..."
if [ -n "$VIRTUAL_ENV" ]; then
    echo "✅ Virtual environment active: $VIRTUAL_ENV"
else
    echo "⚠️  Virtual environment not active"
    echo "   Run: source venv/bin/activate"
fi
echo ""

# Check dependencies
echo "4. Checking dependencies..."
pip3 list | grep -E "Flask|SQLAlchemy|WeasyPrint" || echo "⚠️  Some dependencies missing"
echo ""

# Test imports
echo "5. Testing imports..."
python3 test_import.py
echo ""

# Check database
echo "6. Checking database..."
if [ -f "instance/land_valuation.db" ]; then
    echo "✅ Database file exists"
    ls -lh instance/land_valuation.db
else
    echo "⚠️  Database file not found (will be created on first run)"
fi
echo ""

echo "================================================"
echo "  Troubleshooting Complete"
echo "================================================"
echo ""
echo "Next steps:"
echo "  1. If imports passed: run 'python3 migrate_database.py'"
echo "  2. If migration passed: run 'python3 app.py'"
echo "  3. Open browser to http://your-server-ip:5000"
echo ""

