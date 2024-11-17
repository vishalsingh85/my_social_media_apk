from datetime import datetime
from shared.utils.db_utils import db
from shared.models.user_model import User

class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Self-referential relationship to allow replies to comments
    parent_id = db.Column(db.Integer, db.ForeignKey('comments.comment_id'), nullable=True)
    replies = db.relationship(
        'Comment',
        backref=db.backref('parent', remote_side=[comment_id]),
        lazy='dynamic'
    )

    # String reference for User model to resolve import timing issues
    user = db.relationship('User', backref='comments', lazy=True)

    def to_dict(self):
        """Converts the Comment object to a dictionary, including replies."""
        return {
            "comment_id": self.comment_id,
            "content": self.content,
            "user_id": self.user_id,
            "author": getattr(self.user, 'username', 'Unknown'),  # Assuming User model has 'username' attribute
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "replies": [reply.to_dict() for reply in self.replies.all()]  # Use .all() for dynamic relationships
        }















# from datetime import datetime
# from shared.utils.db_utils import db

# class Comment(db.Model):
#     __tablename__ = 'comments'

#     comment_id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
#     post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

#     # Self-referential relationship to allow replies to comments
#     parent_id = db.Column(db.Integer, db.ForeignKey('comments.comment_id'), nullable=True)
#     replies = db.relationship(
#         'Comment',
#         backref=db.backref('parent', remote_side=[comment_id]),
#         lazy='dynamic'
#     )

#     # Assuming there's a User model with a one-to-many relationship to comments
#     user = db.relationship('User', backref='comments', lazy=True)

#     def to_dict(self):
#         """Converts the Comment object to a dictionary, including replies."""
#         return {
#             "comment_id": self.comment_id,
#             "content": self.content,
#             "user_id": self.user_id,
#             "author": getattr(self.user, 'username', 'Unknown'),  # Assuming User model has 'username' attribute
#             "created_at": self.created_at.isoformat() if self.created_at else None,
#             "updated_at": self.updated_at.isoformat() if self.updated_at else None,
#             "replies": [reply.to_dict() for reply in self.replies.all()]  # Use .all() for dynamic relationships
#         }











