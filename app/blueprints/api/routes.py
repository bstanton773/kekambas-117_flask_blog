from . import api
from app import db
from app.models import Post

@api.route('/')
def index():
    return {'test': 123}


@api.route('/posts', methods=["GET"])
def get_posts():
    posts = db.session.execute(db.select(Post)).scalars().all()
    return [p.to_dict() for p in posts]
