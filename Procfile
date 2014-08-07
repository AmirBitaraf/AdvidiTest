web: gunicorn AdvidiTest.wsgi --workers 3 --log-file -
setup: python manage.py syncdb && python manage.py flush
migrate: python migratedb.py
