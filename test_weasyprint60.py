try:
    from weasyprint import HTML
    from weasyprint.text.fonts import FontConfiguration
    
    print("Testing WeasyPrint 60+ API...")
    
    # Create font config (required for WeasyPrint 60+)
    font_config = FontConfiguration()
    
    # Generate HTML
    html = HTML(string='<h1>Test PDF</h1><p>Testing WeasyPrint 60+</p>')
    
    # Generate PDF with font config
    pdf_bytes = html.write_pdf(font_config=font_config)
    
    print(f"✓ Success! Generated {len(pdf_bytes)} bytes")
    
    # Save to file
    with open('test60.pdf', 'wb') as f:
        f.write(pdf_bytes)
    print("✓ Saved as test60.pdf")
    
except Exception as e:
    print(f"✗ Error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
