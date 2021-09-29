from threading import current_thread
from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_migrate import current
from app.forms import signInForm, signUpForm, updateUser
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, current_user, login_required

# database related imports
from app.models import db, User

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = signUpForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # go about creating a user
            new_user = User(form.username.data, form.email.data, form.password.data, form.first_name.data, form.last_name.data)
            # utilize a try/except block to handle our unique username/email constraints
            # add the newly created user to our database
            try:
                db.session.add(new_user)
                db.session.commit()
            except:
                flash('Username or email already exists. Please try again.', category='alert-danger')
                return redirect(url_for('auth.signup'))

            flash(f'You have successfully signed up with the username: {form.username.data}. You have been automatically logged in.', category='alert-success')
            login_user(new_user)
            return redirect(url_for('home'))
        
        else: # if form input was invalid, tell them to try again
            flash('Invalid input, please try again.', category='alert-danger')
            return redirect(url_for('auth.signup'))
    return render_template('signup.html', form=form)


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = signInForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            usernamedata = form.username.data
            passworddata = form.password.data

            # if the form is valid, and we have a username - we need to determine what the correct password is for that username
            # query the database for our user
            user = User.query.filter_by(username=usernamedata).first()
            # we need to check does a user with that username exist, and if so, does their password match
            if user is None or not check_password_hash(user.password, passworddata):
                flash('Incorrect username or password. Please try again.', category='alert-danger')
                return redirect(url_for('auth.signin'))
            
            # implied else -> the user's username and password matched
            login_user(user)
            flash(f'You have successfully logged in! Welcome {usernamedata} {current_user}.', category='alert-success')
            return redirect(url_for('home'))
        else: # if the form didn't validate
            flash('Invalid form input. Please try again.', category='alert-danger')
            return redirect(url_for('auth.signin'))
    return render_template('signin.html', form=form)

@auth.route('/signout')
def signout():
    logout_user()
    flash('You have successfully signed out.', category='alert-info')
    return redirect(url_for('auth.signin'))


@auth.route('/profile')
@login_required
def profile():
    context = current_user.to_dict()
    print(context)
    # make use of **kwargs using the conventional context dictionary
    return render_template('profile.html', **context)

@auth.route('/updateuser', methods=['GET', 'POST'])
@login_required
def updateuser():
    form = updateUser()
    if request.method == 'POST':
        if form.validate_on_submit() and check_password_hash(current_user.password, form.oldpassword.data):
            if form.newpassword.data and form.newusername.data:
                current_user.password = generate_password_hash(form.newpassword.data)
                current_user.username = form.newusername.data
                db.session.commit()
            elif form.newusername.data:
                current_user.username = form.newusername.data
                db.session.commit()
            elif form.newpassword.data:
                current_user.password = generate_password_hash(form.newpassword.data)
                db.session.commit()
            flash('User information updated!', category='alert-info')
            return redirect(url_for('auth.profile'))
        else:
            flash('Invalid form input. Please try again.', category='alert-danger')
            return redirect(url_for('auth.profile'))
    return render_template('updateuser.html', form=form)