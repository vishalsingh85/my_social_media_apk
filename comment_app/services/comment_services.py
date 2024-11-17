from shared.utils.db_utils import db
from shared.models.comment_model import Comment 
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class CommentService:
    
    @staticmethod
    def add_comment(user_id, post_id, content):
        try:
            # Create a new comment instance
            new_comment = Comment(post_id=post_id, user_id=user_id, content=content)
            
            # Add the comment to the session
            db.session.add(new_comment)
            
            # Commit the transaction to save the comment
            db.session.commit()
            
            return new_comment.to_dict()  # Assuming Comment model has a to_dict() method
        
        except Exception as e:
            # Rollback the transaction if an error occurs
            db.session.rollback()
            logger.error(f'ERROR: Failed adding comment - {e}')
            return None

    @staticmethod
    def get_comments_by_post(post_id):
        try:
            comments = Comment.query.filter_by(post_id=post_id).all()
            return [comment.to_dict() for comment in comments]
        except Exception as e:
            logger.error(f"Error fetching comments: {e}")
            return None

    @staticmethod
    def add_reply(comment_id, user_id, content):
        try:
            # Ensure Reply model is correctly referenced (case-sensitive)
            new_reply = Reply(comment_id=comment_id, user_id=user_id, content=content)
            
            # Add the reply to the session
            db.session.add(new_reply)
            
            # Commit the transaction
            db.session.commit()
            
            return new_reply.to_dict()  # Assuming Reply model has a to_dict() method
        
        except Exception as e:
            db.session.rollback()
            logger.error(f"Error adding reply: {e}")
            return None

    @staticmethod
    def get_replies_by_comment(comment_id):
        try:
            # Ensure Reply model is correctly referenced (case-sensitive)
            replies = Reply.query.filter_by(comment_id=comment_id).all()
            return [reply.to_dict() for reply in replies]
        except Exception as e:
            logger.error(f"Error fetching replies: {e}")
            return None

# from shared.utils.db_utils import db
# from shared.models.comment_model import Comment
# from shared.models.reply_model import Reply  # Assuming the Reply model exists


# class CommentService:
    
#     @staticmethod
#     def add_comment(user_id, post_id, content):
#         try:
#             # Create a new comment instance
#             new_comment = Comment(post_id=post_id, user_id=user_id, content=content)
            
#             # Add the comment to the session
#             db.session.add(new_comment)
            
#             # Commit the transaction to save the comment
#             db.session.commit()
            
#             return new_comment.to_dict()  # Assuming Comment model has a to_dict() method for serialization
        
#         except Exception as e:
#             # Rollback the transaction if an error occurs
#             db.session.rollback()
#             print(f'ERROR: Failed adding comment - {e}')
#             return None
        
#     @staticmethod
#     def get_comments_by_post(post_id):
#         try:
#             comments = Comment.query.filter_by(post_id=post_id).all()
#             return [comment.to_dict() for comment in comments]
#         except Exception as e:
#             print(f"Error fetching comments: {e}")
#             return None

#     @staticmethod
#     def add_reply(comment_id, user_id, content):
#         try:
#             new_reply = reply(comment_id=comment_id, user_id=user_id, content=content)
#             db.session.add(new_reply)
#             db.session.commit()
#             return new_reply.to_dict()
#         except Exception as e:
#             db.session.rollback()
#             print(f"Error adding reply: {e}")
#             return None

#     @staticmethod
#     def get_replies_by_comment(comment_id):
#         try:
#             replies = reply.query.filter_by(comment_id=comment_id).all()
#             return [reply.to_dict() for reply in replies]
#         except Exception as e:
#             print(f"Error fetching replies: {e}")
#             return None
