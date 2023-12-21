from src.models import db, Post

# Post model operations repository class
class PostRepository:

    # Retrieves and returns all post objects from db
    def get_all_posts(self):
        return Post.query.all()

    # Retrieves and returns a post by post_id from db
    def get_post_by_id(self, post_id):

        # Returns post object corresponding to post_id
        return Post.query.get(post_id)

    # Creates new post in db
    def create_post(self, user_id, title, post_date_time, content):

        # Assigns user's Post attributes to new post
        new_post = Post(user_id=user_id, title=title, post_date_time=post_date_time, content=content)

        # Adds new post to db
        db.session.add(new_post)

        # Commits new post to db
        db.session.commit()

        # Returns new post
        return new_post

# Creates singleton instance of PostRepository
post_repository_singleton = PostRepository()