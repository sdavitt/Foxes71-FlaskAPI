from flask import Blueprint
from flask.templating import render_template

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signin', methods=['Get'])
def signin():
    return render_template('signin.html')

