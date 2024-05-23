from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from db import session
from models.post import Post

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/', methods=['POST'])
@jwt_required()
def create_post():
    data = request.json
    user_id = get_jwt_identity()
    content = data.get('content')
    image = data.get('image')
    
    if not content:
        return jsonify({'message': 'Content is required'}), 400
    
    post = Post(user_id=user_id, content=content, image=image)
    session.add(post)
    session.commit()
    return jsonify({'message': 'Post successfully created', 'post': post.to_dict()}), 201

@post_bp.route('/<int:post_id>', methods=['GET'])
@jwt_required()
def get_post(post_id):
    post = session.query(Post).get(post_id)
    if post:
        return jsonify(post.to_dict()), 200
    return jsonify({'message': 'Post not found'}), 404

@post_bp.route('/<int:post_id>', methods=['PUT'])
@jwt_required()
def update_post(post_id):
    data = request.json
    post = session.query(Post).get(post_id)
    if post:
        post.content = data.get('content', post.content)
        post.image = data.get('image', post.image)
        session.commit()
        return jsonify({'message': 'Post successfully updated', 'post': post.to_dict()}), 201
    return jsonify({'message': 'Post not found'}), 404