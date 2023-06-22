from flask import Blueprint 


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
def index():
    return [
        {
            'id': 1,
            'firstName': 'Brian',
            'lastName': 'Stanton'
        },
        {
            'id': 2,
            'firstName': 'Kevin',
            'lastName': 'Beier'
        },
    ]
