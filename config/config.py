import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = os.getenv("DEBUG")
SECRET_KEY = os.getenv("SECRET_KEY")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS",[])
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")