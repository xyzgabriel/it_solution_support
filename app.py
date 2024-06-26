from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bd_tutopia.db'

db = SQLAlchemy(app)
app.config['SECRET_KEY'] = "AppTeste"

from views import *

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, host='0.0.0.0')
