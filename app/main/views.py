from flask import render_template
from flask_login import login_required
from . import main
from app import engine





@main.route('/')
@login_required
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('/profile/profile.html')