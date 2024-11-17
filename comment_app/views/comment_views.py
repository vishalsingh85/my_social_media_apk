class CommentView:
    @staticmethod
    def render_comments(comments):
        def serialize_comment(comment):
            return {
                "comment_id": comment.comment_id,
                "content": comment.content,
                "user_id": comment.user_id,
                "author": getattr(comment.user, 'username', "Unknown"),
                "created_at": comment.created_at.isoformat() if comment.created_at else None,
                "updated_at": comment.updated_at.isoformat() if comment.updated_at else None,
                "replies": serialize_replies(comment.replies)
            }

        def serialize_replies(replies):
            return [
                {
                    "comment_id": reply.comment_id,
                    "content": reply.content,
                    "user_id": reply.user_id,
                    "author": getattr(reply.user, 'username', "Unknown"),
                    "created_at": reply.created_at.isoformat() if reply.created_at else None,
                    "updated_at": reply.updated_at.isoformat() if reply.updated_at else None
                }
                for reply in (replies or [])
            ]

        return {
            "comments": [serialize_comment(c) for c in comments]
        }

# class CommentView:
#     @staticmethod
#     def render_comments(comments):
#         return {
#             "comments": [
#                 {
#                     "comment_id": c.comment_id,
#                     "content": c.content,
#                     "user_id": c.user_id,
#                     "created_at": c.created_at,
#                     "updated_at": c.updated_at,
#                     "author": getattr(c.user, 'username', "Unknown"),
#                     "replies": [
#                         {
#                             "comment_id": r.comment_id,
#                             "content": r.content,
#                             "user_id": r.user_id,
#                             "author": getattr(r.user, 'username', "Unknown"),
#                             "created_at": r.created_at,
#                             "updated_at": r.updated_at
#                         }
#                         for r in c.replies
#                     ]
#                 }
#                 for c in comments
#             ]
#         }
