"""
Quick test to verify app.py imports correctly
"""

try:
    print("Testing imports...")
    from app import app, db, User, LandValuation, ReportTemplate, initialize_default_templates
    print("✅ All imports successful!")
    
    print("\nTesting model relationships...")
    print(f"✅ User model: {User}")
    print(f"✅ LandValuation model: {LandValuation}")
    print(f"✅ ReportTemplate model: {ReportTemplate}")
    
    print("\nTesting database context...")
    with app.app_context():
        print("✅ App context works!")
        
    print("\n🎉 All tests passed! You can now run the migration.")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()

