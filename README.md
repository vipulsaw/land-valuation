# land-valuation

root@ip-172-31-83-97:/home/ubuntu# history
    1  cd
    2  sudo apt update
    3  sudo apt upgrade
    4  cd /var/ww
    5  cd /var/
    6  ls
    7  mkdir www
    8  cd www/
    9  mkdir services
   10  cd services/
   11  mkdir land-valuation
   12  cd land-valuation/
   13  vim app.py
   14  mkdir templates
   15  cd templates/
   16  vim base.html
   17  vim index.html
   18  vim register.html
   19  vim login.html
   20  vim dashboard.html
   21  vim valuation_form.html
   22  sudo apt install python3 python3-pip python3-venv -y
   23  pip3 --version
   24  cd ..
   25  cat > requirements.txt << 'EOF'
   26  Flask==3.0.0
   27  Flask-SQLAlchemy==3.1.1
   28  Flask-Login==0.6.3
   29  reportlab==4.0.7
   30  Werkzeug==3.0.1
   31  EOF
   32  ll
   33  python3 -m venv venv
   34  ll
   35  pip install --upgrade pip
   36  pip install --break-system-packages
   37  pip install --upgrade pip --break-system-packages
   38  pip install -r requirements.txt
   39  pip install --break-system-packages -r requirements.txt
   40  python3 app.py
   41  vim app.py
   42  python3 app.py --host=0.0.0.0 --port=5000
   43  vim app.py
   44  python3 app.py
   45  ll
   46  cd ..
   47  ls
   48  cd land-valuation/ land-valuation-bkp-testing-fine-witout-fr
   49  cp -rp land-valuation/ land-valuation-bkp-testing-fine-witout-fr
   50  ll
   51  cd land-valuation
   52  ll
   53  cd templates/
   54  ll
   55  vim base.html
   56  vim dashboard.html
   57  vim index.html
   58  vim login.html
   59  vim register.html
   60  vim dashboard.html
   61  vim valuation_form.html
   62  vim base.html
   63  cd ..
   64  python3 app.py
   65  history
   66  cd
   67  cd /var/www/services/
   68  ls
   69  cp -rp land-valuation land-valuation-test-2-before-form-update
   70  cd land-valuation
   71  ll
   72  nohup pythno3 app.py &
   73  nohup python3 app.py &
   74  ll
   75  cd ..
   76  du -sh * | grep G
   77  du -sh * | grep M
   78  cd land-valuation
   79  ll
   80  rm -rf nohup.out
   81  apt install zip
   82  ll
   83  cd ..
   84  zip -r land-valuation.zip land-valuation
   85  cd land-valuation
   86  ll
   87  cd templates/
   88  ll
   89  vim base.html
   90  vim dashboard.html
   91  vim index.html
   92  vim login.html
   93  vim register.html
   94  vim valuation_form.html
   95  cd ..
   96  ls
   97  ll
   98  cat requirements.txt
   99  vim app.py
  100  cat requirements.txt
  101  ls
  102  python3 app.py
  103  apt install net-tools
  104  netstat -tulpn
  105  kill -9 19590
  106  python3 app.py
  107  netstat -tulpn
  108  cd ..
  109  ls
  110  cd land-valuation-test-2-before-form-update
  111  ll
  112  cat app.py
  113  cd templates/
  114  ll
  115  cat base.html
  116  ll
  117  cat dashboard.html
  118  ll
  119  cat index.html
  120  ll
  121  cat login.html
  122  ll
  123  cat register.html
  124  ll
  125  cat valuation_form.html
  126  cd ..
  127  cat requirements.txt
  128  vim app.py
  129  ll
  130  cd ..
  131  ll
  132  cd land-valuation
  133  vim app.py
  134  cd ..
  135  mv land-valuation land-valuation-usless
  136  cp -r land-valuation-test-2-before-form-update/ land-valuation
  137  ll
  138  cd land-valuation
  139  ll
  140  vim app.py
  141  cd templates/
  142  ll
  143  vim valuation_form.html
  144  cd ..
  145  python3 app.py
  146  vim app.py
  147  python3 app.py
  148  # 1. Stop the Flask application if it's running (Ctrl+C)
  149  # 2. Navigate to your project directory
  150  cd /var/www/services/land-valuation
  151  # 3. Backup old database (optional)
  152  cp land_valuation.db land_valuation.db.backup
  153  # 4. Delete the old database
  154  rm land_valuation.db
  155  ll
  156  cd instance/
  157  ll
  158  cp land_valuation.db land_valuation.db.backup
  159  rm land_valuation.db
  160  cd ..
  161  python3 app.py
  162  cd ..
  163  ll
  164  cp -r land-valuation land-valuation-before-redir-edit-del-working
  165  ll
  166  cd land-valuation
  167  ll
  168  vim edit_valuation.py
  169  cd templates/
  170  cat dashboard.html
  171  vim dashboard.html
  172  cd ..
  173  vim app.py
  174  python3 app.py
  175  ll
  176  mv edit_valuation.py /var/www/services/land-valuation/templates/
  177  python3 app.py
  178  ll
  179  cd templates/
  180  ll
  181  mv edit_valuation.py edit_valuation.html
  182  cd ..
  183  python3 app.py
  184  ll
  185  cd ..
  186  ll
  187  cp -r land-valuation land-valuation-3-before-pdf-sorting-working
  188  cd land-valuation
  189  ll
  190  cd templates/
  191  ll
  192  vim
  193  ll
  194  vim professional_report.html
  195  cd ..
  196  vim app.py
  197  python3 app.py
  198  cat app.py
  199  cd templates/
  200  ll
  201  cat professional_report.html
  202  ll
  203  cd ..
  204  cat app.py
  205  cd templates/
  206  cat professional_report.html
  207  cd ..
  208  vim app.py
  209  cd templates/
  210  cd ..
  211  pip install weasyprint
  212  # Create a virtual environment
  213  python3 -m venv venv
  214  # Activate it
  215  source venv/bin/activate
  216  # Now install weasyprint
  217  pip install weasyprint
  218  cd templates/
  219  vim professional_report.html
  220  cd ..
  221  python3 app.py
  222  exit
  223  cd /var/www/services/land-valuation
  224  python3 app.py
  225  sudo apt-get install -y libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
  226  pip install weasyprint
  227  pip install weasyprint --break-system-packages
  228  python3 app.py
  229  ll
  230  cd v
  231  cd venv/
  232  ll
  233  cd ..
  234  ll
  235  vim requirements.txt
  236  pip install -r requirements.txt
  237  source venv/bin/activate
  238  pip install -r requirements.txt
  239  python3 app.py
  240  cd templates/
  241  ll
  242  cat professional_report.html
  243  vim professional_report.html
  244  cd ..
  245  python3 app.py
  246  cat app.py
  247  vim app.py
  248  python3 app.py
  249  cat > test_weasyprint.py << 'EOF'
  250  try:
  251      from weasyprint import HTML
  252      print("✓ WeasyPrint is installed and working!")
  253
  254      # Test PDF generation
  255      html = "<h1>Test PDF</h1><p>If you can read this, PDF generation works!</p>"
  256      pdf = HTML(string=html).write_pdf()
  257      print("✓ PDF generation test successful!")
  258      print(f"✓ Generated PDF size: {len(pdf)} bytes")
  259
  260  except ImportError as e:
  261      print("✗ WeasyPrint not installed. Install with: pip install weasyprint")
  262      print(f"Error: {e}")
  263  except Exception as e:
  264      print(f"✗ WeasyPrint error: {e}")
  265  EOF
  266  ll
  267  python3 test_weasyprint.py
  268  pip show weasyprint
  269  cat > test_weasyprint2.py << 'EOF'
  270  import weasyprint
  271  print(f"WeasyPrint version: {weasyprint.__version__}")
  272  # Test 1: Check available methods
  273  print("\nTesting HTML class...")
  274  html_class = weasyprint.HTML
  275  print(f"HTML class: {html_class}")
  276  # Test 2: Simple PDF generation
  277  try:
  278      print("\nTesting simple PDF generation...")
  279      html = weasyprint.HTML(string='<h1>Test</h1><p>Hello PDF</p>')
  280      pdf_bytes = html.write_pdf()
  281      print(f"✓ Success! Generated {len(pdf_bytes)} bytes")
  282
  283      # Save test PDF
  284      with open('test_output.pdf', 'wb') as f:
  285          f.write(pdf_bytes)
  286      print("✓ Saved as test_output.pdf")
  287
  288  except Exception as e:
  289      print(f"✗ Error: {type(e).__name__}: {e}")
  290      import traceback
  291      traceback.print_exc()
  292  EOF
  293  python3 test_weasyprint2.py
  294  pip uninstall weasyprint pydyf -y
  295  vim requirements.txt
  296  pip install -r requirements.txt
  297  python3 test_weasyprint2.py
  298  pip show weasyprint
  299  python3 test_weasyprint.py
  300  cat > test_weasyprint60.py << 'EOF'
  301  try:
  302      from weasyprint import HTML
  303      from weasyprint.text.fonts import FontConfiguration
  304
  305      print("Testing WeasyPrint 60+ API...")
  306
  307      # Create font config (required for WeasyPrint 60+)
  308      font_config = FontConfiguration()
  309
  310      # Generate HTML
  311      html = HTML(string='<h1>Test PDF</h1><p>Testing WeasyPrint 60+</p>')
  312
  313      # Generate PDF with font config
  314      pdf_bytes = html.write_pdf(font_config=font_config)
  315
  316      print(f"✓ Success! Generated {len(pdf_bytes)} bytes")
  317
  318      # Save to file
  319      with open('test60.pdf', 'wb') as f:
  320          f.write(pdf_bytes)
  321      print("✓ Saved as test60.pdf")
  322
  323  except Exception as e:
  324      print(f"✗ Error: {type(e).__name__}: {e}")
  325      import traceback
  326      traceback.print_exc()
  327  EOF
  328  python3 test_weasyprint60.py
  329  cd /var/www/services/land-valuation
  330  ll
  331  cat app.py
  332  cd templates/
  333  ll
  334  cat professional_report.html
  335  cd ..
  336  cat app.py
  337  source venv/bin/activate
  338  python -c "from weasyprint import HTML; print('OK')"
  339  ll
  340  vim app.py
  341  python3 app.py
  342  vim app.py
  343  python3 app.py
  344  vim app.py
  345  python3 app.py
  346  vim app.py
  347  python3 app.py
  348  vim app.py
  349  python3 app.py
  350  vim app.py
  351  python3 app.py
  352  cat app.py
  353  vim app.py
  354  python3 app.py
  355  cp -r app.py /var/app.py-woring-with-html-pdf-failing
  356  vim app.py
  357  python3 app.py
  358  vim app.py
  359  python3 app.py
  360  cd templates/
  361  ll
  362  cp -r professional_report.html /var/
  363  vim professional_report.html
  364  cd ..
  365  ll
  366  python3 app.py
  367  cd templates/
  368  ll
  369  rm -rf professional_report.html
  370  cp -r /var/professional_report.html /var/www/services/land-valuation/templates/
  371  ll
  372  cd ..
  373  ll
  374  zip -r new-land-val.zip
  375  zip -r new-land-val.zip land-valuation
  376  cd ..
  377  cd services/land-valuation
  378  ll
  379  pip install -r requirements.txt
  380  cd ..
  381  ll
  382  exit
  383  cd /var/www/
  384  git clone https://github.com/vipulsaw/land-valuation.git
  385  ls
  386  cd land-valuation/
  387  ll
  388  # Create a virtual environment
  389  python3 -m venv venv
  390  # Activate it
  391  source venv/bin/activate
  392  pip install -r requirements.txt
  393  cat requirements.txt
  394  git pull
  395  cat requirements.txt
  396  pip install -r requirements.txt
  397  python3 app.py
  398  git pull
  399  python3 app.py
  400  git pull
  401  python3 app.py
  402  git pull
  403  python3 app.py
  404  git pull
  405  python3 app.py
  406  git pull
  407  python3 app.py
  408  git pull
  409  python3 app.py
  410  git pull
  411  python3 app.py
  412  systemctl restart nginx
  413  ls -la /etc/nginx/sites-enabled/
  414  sudo ln -sf /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
  415  sudo nginx -t  # Test configuration first
  416  sudo systemctl reload nginx
  417  # or
  418  sudo systemctl restart nginx
  419  sudo unlink /etc/nginx/sites-enabled/default
  420  sudo systemctl restart nginx
  421  history
