from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    due_date = db.Column(db.DateTime, nullable=True)
    completed = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'GET':
        tasks = Task.query.all()
        task_list = [{'id': task.id, 'title': task.title, 'due_date': task.due_date.strftime('%Y-%m-%d'), 'completed': task.completed} for task in tasks]
        return jsonify(task_list)
    elif request.method == 'POST':
        data = request.json
        new_task = Task(title=data['title'], due_date=datetime.strptime(data['due_date'], '%Y-%m-%d'), completed=False)
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task created successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
