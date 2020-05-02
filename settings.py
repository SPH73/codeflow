import os

MONGO_URI = os.environ.get("CODEFLOW_MONGO_URI")
MONGO_DBNAME = os.environ.get("MONGO_DBNAME")
SECRET_KEY = os.environ.get("CODEFLOW_SECRET_KEY")


RECAPTCHA_PUBLIC_KEY = os.environ.get("CODEFLOW_RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.environ.get("CODEFLOW_RECAPTCHA_PRIVATE_KEY")
RECAPTCHA_USE_SSL = False
RECAPTCHA_OPTIONS = {'theme': 'white'}
