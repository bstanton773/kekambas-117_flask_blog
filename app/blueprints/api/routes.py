from flask import request
from . import api
from app import db
from app.models import Post, User
from .auth import basic_auth

@api.route('/token')
@basic_auth.login_required
def get_token():
    user = basic_auth.current_user()
    token = user.get_token()
    return {'token': token, 'token_expiration': user.token_expiration}


@api.route('/posts', methods=["GET"])
def get_posts():
    posts = db.session.execute(db.select(Post)).scalars().all()
    return [p.to_dict() for p in posts]


@api.route('/users', methods=['POST'])
def create_user():
    # Check to see that the request body is JSON
    if not request.is_json:
        return {'error': 'Your request content-type must be application/json'}, 400
    # Get the data from the request body
    data = request.json
    # Validate the incoming data
    required_fields = ['firstName', 'lastName', 'email', 'username', 'password']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            # if the field is not in the request body, add to missing fields
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)} must be in the request body"}, 400

    # Get the data from the request body
    first = data.get('firstName')
    last = data.get('lastName')
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    # Check to see if there is already a user with email and/or username
    check_user = db.session.execute(db.select(User).where((User.username==username)|(User.email==email))).scalars().all()
    if check_user:
        return {'error': 'User with that username and/or email already exists'}, 400
    # Create a new user instance with the request data
    new_user = User(first_name=first, last_name=last, email=email, username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict()
