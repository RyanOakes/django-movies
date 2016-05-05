# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!s@liqi8smlyswah^d)tbgleax6yri6*cb03gsp0zy33su%23$'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movielens',
        'USER': 'Oakes',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
