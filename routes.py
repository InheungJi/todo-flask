from flask import render_template, request, url_for, redirect,flash
from flask_login import login_user, login_required, logout_user
from models import User, Todo
from forms import LoginForm, TodoForm, RegistrationForm
from app import db, app, login_manager


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    login_form = LoginForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return render_template('index.html', login=login_form)
    return render_template('registration.html', register_form=form)


@app.route('/', methods=["GET", "POST"])
def index():
    login_form = LoginForm()
    todo_form = TodoForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user and user.check_password(login_form.password.data):
            login_user(user)
            todos = Todo.query.filter_by(user_id=user.id)
            return render_template('login_index.html', current_user=user, user_id=user.id,
                                   template_todoForm=todo_form, template_todoData=todos)
        else:
            flash('you need to make account!!')
            form = RegistrationForm()
            return render_template('registration.html', register_form = form)
    return render_template('index.html', login=login_form)


@app.route('/user/<user_id>', methods=["GET", "POST"])
@login_required
def login_index(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    todo_form = TodoForm()
    if todo_form.validate_on_submit():
        todo = Todo(todo_text=todo_form.todo.data, user_id=user.id)
        db.session.add(todo)
        db.session.commit()

    return render_template('login_index.html', template_todoForm=todo_form, template_todoData=user.todos,
                           user_id=user.get_id())


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
