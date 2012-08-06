import os, sys
sys.path.append('/Users/hristoforrusev/Documents/djangoProjects/BowlingFed')
sys.path.append('/Users/hristoforrusev/Documents/djangoProjects/BowlingFed/BowlingFed')
os.environ['DJANGO_SETTINGS_MODULE'] = 'BowlingFed.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
