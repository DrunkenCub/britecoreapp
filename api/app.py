"""Main entrypint of the application."""
# Api factory import
from api import factory
from flask_sqlalchemy import SQLAlchemy

# Eventually force the environment
# factory.environment = 'default'

# Get flask instance
app = factory.flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:triolly123@localhost:5432/britecore'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == '__main__':
    # Actually run the application
    app.run()   