
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent

SECRET_KEY='django-insecure-change-me'
DEBUG=True
ALLOWED_HOSTS=[]

INSTALLED_APPS=[
 'django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 'rest_framework',
 'rest_framework_simplejwt',
 'core.apps.CoreConfig',
]

MIDDLEWARE=[
 'django.middleware.security.SecurityMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF='sghss_backend.urls'

TEMPLATES=[{
 'BACKEND':'django.template.backends.django.DjangoTemplates',
 'DIRS':[],
 'APP_DIRS':True,
 'OPTIONS':{
  'context_processors':[
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
  ],
 },
}]

WSGI_APPLICATION='sghss_backend.wsgi.application'

DATABASES={
 'default':{
  'ENGINE':'django.db.backends.postgresql',
  'NAME':'postgres',
  'USER':'postgres',
  'PASSWORD':'250250',
  'HOST':'localhost',
  'PORT':'5432',
 }
}

AUTH_PASSWORD_VALIDATORS=[]

LANGUAGE_CODE='pt-br'
TIME_ZONE='America/Sao_Paulo'
USE_I18N=True
USE_TZ=True

STATIC_URL='static/'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'

AUTH_USER_MODEL='core.User'

REST_FRAMEWORK={
 'DEFAULT_AUTHENTICATION_CLASSES':(
   'rest_framework_simplejwt.authentication.JWTAuthentication',
 ),
 'DEFAULT_PERMISSION_CLASSES':(
   'rest_framework.permissions.AllowAny',
 ),
}
