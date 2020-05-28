from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, CreateQuizForm, AnswerQuizForm
from app.models import User, Quiz, Qanswers

# decorator for index page
@app.route('/')
@app.route('/index')
@login_required
def index():#main page
    Quiz_addresses = Quiz.query.all()
    return render_template('index.html', title='Home', Quiz_addresses=Quiz_addresses)

# decorator for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # checks username and password in sqllite database
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

# decorator for logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# decorator for registering
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    # add username and password to database
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/create_quiz', methods=['GET', 'POST'])
@login_required #user check
def createquiz(): #currently used
    form = CreateQuizForm() 
    #user check should go above form = 
    #if current_user.is_authenticated: # fix chekc for users
    #    return redirect(url_for('index'))
    if form.validate_on_submit():
        quiz = Quiz(quizname=form.quizname.data, q1=form.q1.data, q2=form.q1.data, q3=form.q1.data)
        db.session.add(quiz)
        db.session.commit()
        flash('Congratulations, you have made a quiz')
        return redirect(url_for('login'))
    return render_template('create_quiz.html', title='Create-Quiz', form=form)


@app.route('/quiz/<quiz_name>', methods=['GET', 'POST'])
#@login_required
def quizanswerer(quiz_name): #dont need to be logged in
    
    #form = AnswerQuizForm()
    # add check for quiz_name existing with a redirect
    quiz_items = Quiz.query.filter_by(quizname=quiz_name).first_or_404() #checks if quiz_name is a quiz
    q1_text = quiz_items.q1
    q2_text = quiz_items.q2
    q3_text = quiz_items.q3
    name_of_quiz = quiz_name

    form = AnswerQuizForm()
    if form.validate_on_submit():
        qanswers = Qanswers(quiz_name=name_of_quiz, submit_name=form.submit_name.data, a1=form.a1.data, a2=form.a2.data, a3=form.a3.data, q1copy=q1_text, q2copy=q2_text ,q3copy=q3_text)
        db.session.add(qanswers)
        db.session.commit()
        flash('Congratulations, you have answered a quiz')
        return redirect(url_for('login'))



    return render_template('answer_page.html', title='Answers', q1_t=q1_text, q2_t=q2_text, q3_t=q3_text, noq=name_of_quiz, form=form)
    #return render_template('answer_page.html', title='Answers', q1_t=q1_text, q2_t=q2_text, q3_t=q3_text, noq=name_of_quiz, form=form)
    #return render_template('answer_page.html', title='Answers', quiz_stuff=quiz_items, form=form)

@app.route('/results')
def Result():
    all_results = Qanswers.query.all()
    
    return render_template('results.html', title='Home', all_results=all_results)