from flask import Blueprint
from comment_app.controller.comment_controller import CommentController

comment_bp = Blueprint('comment_bp', __name__)

# Add a comment to a post
@comment_bp.route('/api/posts/<int:post_id>/comments', methods=['POST'])
def add_comment(post_id):
    return CommentController.add_comment(post_id)

# Get all comments for a specific post
@comment_bp.route('/api/posts/<int:post_id>/comments', methods=['GET'])
def get_comments(post_id):
    return CommentController.get_comments(post_id)

# Add a reply to a specific comment
@comment_bp.route('/api/comments/<int:comment_id>/replies', methods=['POST'])
def add_reply(comment_id):
    return CommentController.add_reply(comment_id)

# Get all replies for a specific comment
@comment_bp.route('/api/comments/<int:comment_id>/replies', methods=['GET'])
def get_replies(comment_id):
    return CommentController.get_replies(comment_id)

# from flask import Blueprint
# from comment_app.controller.comment_controller import CommentController

# comment_bp = Blueprint('comment_bp', __name__)

# @comment_bp.route('/api/posts/<int:post_id>/comments', methods=['POST'])
# def add_comment(post_id):
#     return CommentController.add_comment(post_id)

# @comment_bp.route('/api/posts/<int:post_id>/comments', methods=['GET'])
# def get_comments(post_id):
#     return CommentController.get_comments(post_id)

# @comment_bp.route('/api/comments/<int:comment_id>/replies', methods=['POST'])
# def add_reply(comment_id):
#     return CommentController.add_reply(comment_id)

# @comment_bp.route('/api/comments/<int:comment_id>/replies', methods=['GET'])
# def get_replies(comment_id):
#     return CommentController.get_replies(comment_id)

# from flask import Blueprint
# from comment_app.controllers.comment_controller import CommentController

# comment_bp = Blueprint('comment_bp',__name__)

# @comment_bp.route('/api/posts/<int:post_id>/comment',method=['POST'])
# def add_comment(post_id):
#     return CommentController.add_comment(post_id)


# @comment_bp.route('/api/posts/<int:post_id>/comment',method=['GET'])
# def get_comments(post_id):
#     return CommentController.get_comments(post_id)


# @comment_bp.route('/api/posts/<int:post_id>/replies',method=['POST'])
# def add_reply(comment_id):
#     return CommentController.add_reply(comment_id)


# @comment_bp.route('/api/posts/<int:post_id>/comment',method=['GET'])
# def get_replies(comment_id):
#     return CommentController.get_replies(comment_id)
