import weasyprint
print(f"WeasyPrint version: {weasyprint.__version__}")

# Test 1: Check available methods
print("\nTesting HTML class...")
html_class = weasyprint.HTML
print(f"HTML class: {html_class}")

# Test 2: Simple PDF generation
try:
    print("\nTesting simple PDF generation...")
    html = weasyprint.HTML(string='<h1>Test</h1><p>Hello PDF</p>')
    pdf_bytes = html.write_pdf()
    print(f"✓ Success! Generated {len(pdf_bytes)} bytes")
    
    # Save test PDF
    with open('test_output.pdf', 'wb') as f:
        f.write(pdf_bytes)
    print("✓ Saved as test_output.pdf")
    
except Exception as e:
    print(f"✗ Error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
