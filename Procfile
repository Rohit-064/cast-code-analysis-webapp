release: python manage.py migrate
web: gunicorn CAST_codeAnalyser.wsgi --log-file -
web: node index.js