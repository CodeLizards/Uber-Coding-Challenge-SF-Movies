# """
# WSGI config for testsite project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testsite.settings")

# application = get_wsgi_application()

 # +++++++++++ DJANGO +++++++++++
    import os
    import sys

    ## assuming your Django settings file is at '/home/my_username/projects/my_project/settings.py'
     path = '/Users/elizabethharris/Desktop/testsite'
     if path not in sys.path:
          sys.path.append(path)
  
      os.environ['DJANGO_SETTINGS_MODULE'] = 'testsite.settings'
  
      from django.core.wsgi import get_wsgi_application
      application = get_wsgi_application()
