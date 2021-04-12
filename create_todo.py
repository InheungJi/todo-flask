from app import db, Todo
import datetime

first_todo = Todo(todo_text="Learn Flask", date_info=datetime.datetime.now())
db.session.add(first_todo)
db.session.commit()
