from flask import request, jsonify
from comment_app.services.comment_services import CommentService
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class CommentController:
    @staticmethod
    def add_comment(post_id):
        try:
            data = request.get_json()
            logger.debug(f"Received data for add_comment: {data}")

            if not data or not data.get('content'):
                return jsonify({"error": "Content is required"}), 400

            user_id = data.get('user_id')
            content = data.get('content')

            if not user_id:
                return jsonify({"error": "User ID is required"}), 400

            comment_service = CommentService()
            comment = comment_service.add_comment(user_id=user_id, post_id=post_id, content=content)
            
            if comment:
                return jsonify({"message": "Comment posted successfully"}), 201
            return jsonify({"error": "Failed to post comment"}), 500
        except Exception as e:
            logger.error(f"Error in add_comment: {e}")
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_comments(post_id):
        try:
            logger.debug(f"Fetching comments for post_id: {post_id}")

            comment_service = CommentService()
            comments = comment_service.get_comments_by_post(post_id)
            
            if comments:
                return jsonify(comments), 200
            return jsonify({"message": "No comments found"}), 404
        except Exception as e:
            logger.error(f"Error in get_comments: {e}")
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def add_reply(comment_id):
        try:
            data = request.get_json()
            logger.debug(f"Received data for add_reply: {data}")

            if not data or not data.get('content'):
                return jsonify({"error": "Content is required"}), 400

            user_id = data.get('user_id')
            content = data.get('content')

            if not user_id:
                return jsonify({"error": "User ID is required"}), 400

            comment_service = CommentService()
            reply = comment_service.add_reply(comment_id=comment_id, user_id=user_id, content=content)
            
            if reply:
                return jsonify({"message": "Reply posted successfully"}), 201
            return jsonify({"error": "Failed to post reply"}), 500
        except Exception as e:
            logger.error(f"Error in add_reply: {e}")
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_replies(comment_id):
        try:
            logger.debug(f"Fetching replies for comment_id: {comment_id}")

            comment_service = CommentService()
            replies = comment_service.get_replies_by_comment(comment_id)
            
            if replies:
                return jsonify(replies), 200
            return jsonify({"message": "No replies found"}), 404
        except Exception as e:
            logger.error(f"Error in get_replies: {e}")
            return jsonify({"error": str(e)}), 500

# from flask import request
# from comment_app.services.comment_service import CommentService
# from comment_app.views.comment_view import CommentView

# class CommentController:
#     comment_service = CommentService()

#     @staticmethod
#     def add_comment():
#         data = request.get_json()
#         if not data or not data.get('content'):
#             return {"error": "Content is required"}, 400

#         user_id = data.get('user_id')
#         post_id = data.get('post_id')
#         content = data.get('content')

#         comment = CommentController.comment_service.add_comment(user_id=user_id, post_id=post_id, content=content)
#         if comment:
#             return {"message": "Comment posted successfully"}, 201
#         return {"error": "Failed to post comment"}, 500

#     @staticmethod
#     def get_comments(post_id):
#         comments = CommentController.comment_service.get_comments(post_id)
#         if comments:
#             return jsonify(comments), 200
#         return {"message": "No comments found"}, 404

#     @staticmethod
#     def add_reply(comment_id):
#         data = request.get_json()
#         if not data or not data.get('content'):
#             return {"error": "Content is required"}, 400

#         user_id = data.get('user_id')
#         content = data.get('content')

#         reply = CommentController.comment_service.add_reply(comment_id=comment_id, user_id=user_id, content=content)
#         if reply:
#             return {"message": "Reply posted successfully"}, 201
#         return {"error": "Failed to post reply"}, 500

#     @staticmethod
#     def get_replies(comment_id):
#         replies = CommentController.comment_service.get_replies(comment_id)
#         if replies:
#             return jsonify(replies), 200
#         return {"message": "No replies found"}, 404


# # from flask import request
# # from comment_app.services.comment_service import commentService
# # from comment_app.views.comment_view import commentView

# # class comment_controller:
# #     @staticmethod
# #     def add_comment(post_id):
# #         data = request.get_json()
# #         user_id = data.get('user_id')
# #         post_id = data.get('post_id')
# #         content = data.get('content')
        
# #         comment = comment_service.add_comment(user_id=user_id, post_id=post_id, content=content)
# #         return {"comment posted"}, 201
    
# #     @staticmethod
# #     def get_comments(post_id):
# #         comments = comment_service.get_comments(post_id)
# #         return {"comment found.."} ,200
    
# #     @staticmethod
# #     def add_reply(comment_id):
# #         data = request.get_json()
# #         user_id = data.get('user_id')
# #         comment_id = data.get('comment_id')
# #         content = data.get('content')
        
# #         reply = comment_service.add_reply(comment_id=comment_id,user_id=user_id,content=content)
# #         return {"reply posted"}, 201
    
# #     @staticmethod
# #     def get_replies(comment_id):
# #         replies = comment_service.get_replies(comment_id)
# #         return {"replies found.."} ,200