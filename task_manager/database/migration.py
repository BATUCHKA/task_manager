import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://task_user:task_password@mysql-db/task_manager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.Date, nullable=True)
    completed = db.Column(db.Boolean, default=False)

if __name__ == '__main__':
    # This script will initialize the database and create tables
    # Run this from the command line:
    # python -m database.migration
    
    # To run migrations, use these Flask CLI commands:
    # flask db init      # Only needed once to initialize migrations
    # flask db migrate   # Create migration files
    # flask db upgrade   # Apply migrations
    
    try:
        # Create all tables if they don't exist
        db.create_all()
        print("Database tables created successfully")
    except Exception as e:
        print(f"Error creating database tables: {str(e)}")