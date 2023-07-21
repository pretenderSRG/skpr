from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from data import users

users_bp = Blueprint("users_bp" ,__name__, url_prefix='/users')
db = SQLAlchemy(users_bp)

