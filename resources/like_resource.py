from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from db import session
from models.like import Like

like_bp = Blueprint('like_bp', __name__)

@like_bp.route('/', methods=['POST'])
@jwt_required()
def create_like():
    data = request.json
    user_id = get_jwt_identity()
    post_id = data.get('post_id')
    
    if not post_id:
        return jsonify({'message': 'Post ID is required'}), 400
    
    like = Like(user_id=user_id, post_id=post_id)
    session.add(like)
    session.commit()
    return jsonify({'message': 'Like successfully created', 'like': like.to_dict()})

@like_bp.route('/<int:like_id>', methods=['GET'])
@jwt_required()
def get_like(like_id):
    like = session.query(Like).get(like_id)
    if like:
        return jsonify(like.to_dict()), 200
    return jsonify({'message': 'Like not found'}), 404

@like_bp.route('/<int:like_id>', methods=['DELETE'])
@jwt_required()
def delete_like(like_id):
    like = session.query(Like).get(like_id)
    if like:
        session.delete(like)
        session.commit()
        return jsonify({'message': 'Like successfully deleted'}), 200
    return jsonify({'message': 'Like not found'}), 404