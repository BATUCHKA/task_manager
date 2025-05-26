from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import os
from config import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = Config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{Config.DB_USERNAME}:{Config.DB_PASSWORD}@{Config.DB_LOCATION}/{Config.DB_DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.Date, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Task {self.title}>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks')
def tasks():
    all_tasks = Task.query.all()
    return render_template('tasks.html', tasks=all_tasks)

@app.route('/tasks/create', methods=['POST'])
def create_task():
    title = request.form.get('title')
    description = request.form.get('description')
    due_date_str = request.form.get('due_date')
    
    if not title:
        flash('Title is required!')
        return redirect(url_for('tasks'))
    
    due_date = None
    if due_date_str:
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
    
    new_task = Task(
        title=title,
        description=description,
        due_date=due_date
    )
    
    db.session.add(new_task)
    db.session.commit()
    
    flash('Task created successfully!')
    return redirect(url_for('tasks'))

@app.route('/tasks/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = True
    db.session.commit()
    
    flash('Task marked as complete!')
    return redirect(url_for('tasks'))

@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    
    flash('Task deleted!')
    return redirect(url_for('tasks'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')