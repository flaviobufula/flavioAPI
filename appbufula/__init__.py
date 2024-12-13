from flask import Flask

app = Flask(__name__)

from appbufula.views import homepage
