from flask import Flask,render_template
from datetime import datetime
app = Flask(__name__)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/todo.db'
db = SQLAlchemy(app)
# Define a function to create database tables
def create_tables():
    with app.app_context():
        db.create_all()
create_tables()
class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
def __repr__(self) -> str:
    return f"{self.sno},{self.title}"

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/product')
def product():
    return 'This is the product page'
if __name__=="__main__":
    app.run(debug=True)