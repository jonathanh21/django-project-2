from email.policy import default
from .base import *
from .base import env

DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default='django-insecure-$b7tu+2nhw-^f41aw6b2fro2@nk*m=ge=_s3zxwu=-95zcmezd',
)


ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
