try:
    from weasyprint import HTML
    print("✓ WeasyPrint is installed and working!")
    
    # Test PDF generation
    html = "<h1>Test PDF</h1><p>If you can read this, PDF generation works!</p>"
    pdf = HTML(string=html).write_pdf()
    print("✓ PDF generation test successful!")
    print(f"✓ Generated PDF size: {len(pdf)} bytes")
    
except ImportError as e:
    print("✗ WeasyPrint not installed. Install with: pip install weasyprint")
    print(f"Error: {e}")
except Exception as e:
    print(f"✗ WeasyPrint error: {e}")
