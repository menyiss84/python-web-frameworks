DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite.db',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'db.apps.DbConfig',
    )

SECRET_KEY = 'jsd9sdyo78dTQ2G3HL2QMP9qjoj2dodimqpSCDu'