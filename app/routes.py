from flask import Flask, render_template, Blueprint
from flask_login import login_user, login_required, logout_user

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return "Hello World!"

@bp.route('/login', methods=['GET', 'POST'])
def login():
    return "Login"