from flask import Flask
from flask_restful import Api
from extensions import db, migrate
from routes.agBp import agBp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agenda.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

'''
@app.route('/agenda')
def agenda_list():
    db.create_all()
'''

db.init_app(app)
migrate.init_app(app)
app.register_blueprint(agBp)

if __name__ == '__main__':
    app.run()