import secrets, os

WTF_CSRF_ENABLED = True
SECRET_KEY = secrets.token_hex()
SECURITY_PASSWORD_SALT = secrets.token_hex()
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False

#if deployed keep session_cookie_secure as True
SESSION_COOKIE_SECURE = True

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
