heroku config:set DISABLE_COLLECTSTATIC=1

web: gunicorn --workers=2 test_rest.wsgi
