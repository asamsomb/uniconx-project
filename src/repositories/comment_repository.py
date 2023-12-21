from src.models import db, Comment

# Repository class for Comment Repository model
class CommentRepository:

    # Retrieves all posts from db and returns list of Post objects
    def get_all_comments(self):
        return Comment.query.all()

    # Retrieves a comment from db by comment_id and returns created Post object
    def get_comment_by_id(self, comment_id):
        return Comment.query.get(comment_id)

    # Defines function to add new comment
    def add_comment(self, user_id, post_id, comment_date_time, comment_content):

        # Assigns comment attributes to new_comment variable
        new_comment = Comment(user_id=user_id, post_id=post_id, comment_date_time=comment_date_time, comment_content=comment_content)

        # Adds and commits new comment to db
        db.session.add(new_comment)
        db.session.commit()

        # Returns new comment
        return new_comment

# Assigns singleton instance of PostRepository
comment_repository_singleton = CommentRepository()