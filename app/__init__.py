import os

from flask import Flask

here = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, static_folder=os.path.join(here, 'static'),
            template_folder=os.path.join(here, 'templates'))



from app import views
