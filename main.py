from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(80), unique=True)
    pw_hash = db.Column(db.String(80))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(27), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Post(title={title}, body={body}, likes={likes})"


db.create_all()


args = {}

post_put_args = reqparse.RequestParser()
post_put_args.add_argument("title", type=str, help="Title can't be unfilled", required=True)
post_put_args.add_argument("body", type=str, help="Body can't be unfilled", required=True)
post_put_args.add_argument("likes", type=int, help="Put a like if you like")

resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'body': fields.String,
    'likes': fields.Integer
}


class Posts(Resource):
    @marshal_with(resource_fields)
    def get(self, post_id):
        result = Post.query.get(id=post_id)
        return result

    def put(self, post_id):
        args = post_put_args.parse_args()
        post = Post(id=post_id, title=args['title'], body=args['body'], likes=args['likes'])
        db.session.add(post)
        db.session.commit()
        return post, 201

    def delete(self, post_id):
        del posts[post_id]
        return "", 204


#api.add_resource(Posts, "/getrequest")
api.add_resource(Posts, "/getrequest/<int:post_id>")
#api.add_resource(Posts, "/putrequest")

if __name__ == "__main__":
    app.run(debug=True)

