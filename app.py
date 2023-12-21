from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from src.models import User, Post, Comment, db
from src.repositories.user_repository import user_repository_singleton
from src.repositories.post_repository import post_repository_singleton
from src.repositories.comment_repository import comment_repository_singleton
from datetime import datetime
from functools import wraps

# Flask app initialization
app = Flask(__name__)

# Secret key for session security purposes.
app.secret_key = '*************************************************'

# Flask-Login initialization
login_manager = LoginManager(app)

# Sets 'login.html' for unauthorized users (unregistered users)
login_manager.login_view = 'login'

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://*********************************************************' 

# Create 'user_account_schema' in your MySQL local database and add info here. REMOVE BEFORE COMMIT!!!
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db.init_app(app)

# Defines login_requried function with parameter 'view func' using wrapper.
# Checks user authetication and routes them to login if not.
def login_required(view_func):
    @wraps(view_func)

    # Decorated function redirects users who have not been authenticate to 'login'
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        return view_func(*args, **kwargs)
    return decorated_function

# Loads user by retrieving user_id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():

    # Authenticated users, once logged in, are redirected to 'forum'
    if current_user.is_authenticated:
        return redirect(url_for('forum'))

    # Checks authentication of user credentials 
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # User Authentication
        user = user_repository_singleton.authenticate_user(email, password)

        if user:
            # Session variable to represent user log-in
            session['user_id'] = user.user_id
            login_user(user) # Log in user w/ Flask-Login
            return redirect(url_for('index'))  # Redirect to the home page
        else:
            # Shows invalid credentials if user credentials are not recognized
            flash('Invalid credentials. Please try again.', 'danger')

    # Pass additional variable to template to indicate authentication status
    return render_template('login.html', authentication_failed=request.method == 'POST')

# Route to log users out
@app.route('/logout')
def logout():
    logout_user() # log out user w/ Flask-Login
    return redirect(url_for('login')) # Redirects to 'login.html'

# route to Home page
@app.get('/')
def index(): 
    return render_template('index.html')

# route to Rida forum page
@app.get('/forum_2')
def forum_2(): 
    return render_template('forum_2.html')

# Route to About Us page
@app.get('/about-uniconx')
def about_uniconx(): 
    return render_template('about-uniconx.html')

# Route to Contact Us page
@app.get('/contact-uniconx')
def contact_uniconx(): 
    return render_template('contact-uniconx.html')

# Route to Contact Us page
@app.get('/tech_portfolio')
@login_required
def tech_portfolio(): 
    return render_template('techPortfolio.html')

# Route to Create New Account form
@app.get('/users/new')
def create_account_form():
    return render_template('create_account_form.html', create_account_active=True)

# Custom error page route to code 401
@app.route('/code_401')
def code_401():
    return render_template('401.html')

# Custom error page route to code 400
@app.route('/code_400')
def code_400():
    return render_template('400.html')

# Route to remove a post only when a user is logged in
@app.route('/delete_post/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):

    # Retrieves post_id and assigns it to variable post.
    post = Post.query.get(post_id)

    # Check for existing post. If not found, returns message.
    if not post:
        return "Post not found"

    # Checks if current user in session is the original post's poster
    if current_user.user_id == post.user_id:

        # Deletes associated comments explicitly by allowing users to delete only comments they've posted
        comments_to_delete = Comment.query.filter(Comment.post_id == post.post_id).all()

        # Deletes comment in db
        for comment in comments_to_delete:
            db.session.delete(comment)

        # Deletes post from original user
        db.session.delete(post)

        # Commits deletion
        db.session.commit()

        # Refreshes forum to confirm delee action
        return redirect(url_for('forum'))
    else:
        # If no post to delete, returns code 401 page.
        return redirect(url_for('code_401'))

# Routes Edit Post function that allows original uses of post to edit and resubmit their post
@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get(post_id)

    if not post:
        return "Post not found"

    # Checks for user_id in post's user id
    if current_user.user_id != post.user_id:
        return redirect(url_for('code_401'))

    # Populates a new title and new content form for user to update/change post
    if request.method == 'POST':
        post.title = request.form['new_title']
        post.content = request.form['new_content']

        # Commits user post changes & refreshes forum page to confirm changes
        db.session.commit()
        return redirect(url_for('forum'))

    return render_template('forum.html', current_user=current_user, edit_post=post)

# Routes Forum
@app.route('/forum', methods=['GET', 'POST'])
def forum():

    if request.method == 'POST':

        # If a user is not logged in, redirects to login page.
        if not current_user.is_authenticated:
            return redirect(url_for('login'))

        # Retrieves title and content from new post form
        title = request.form.get('title')
        content = request.form.get('content')

        # Assume user is already logged in, and user_id of current user to post
        user_id = current_user.get_id()

        # Insert new post into the database via Flask-SQLAlchemy
        new_post = post_repository_singleton.create_post(user_id=user_id, title=title, post_date_time=datetime.now(), content=content)
        db.session.add(new_post)
        db.session.commit()

    # Get posts from the database using Flask-SQLAlchemy
    posts = db.session.query(Post, User.email).join(User, Post.user_id == User.user_id).all()

    # Fetch comments for each post separately
    comments = {}
    for post, email in posts:
        post_id = post.post_id
        post_comments = db.session.query(Comment, User.email).join(User, Comment.user_id == User.user_id).filter(Comment.post_id == post_id).all()
        comments[post_id] = post_comments

    return render_template('forum.html', posts=posts, comments=comments)

# Routes to add comment; requires user to be logged in
@app.route('/add_comment/<int:post_id>', methods=['POST'])
@login_required
def add_comment(post_id):  # Add post_id as a parameter
    if request.method == 'POST':

        # If a user is not logged in, redirects to login page.
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        
        # Retrieves comment content from new comment form
        comment_content = request.form.get('comment_content')

        # Assume user is already logged in, and user_id of current user to comment
        user_id = current_user.get_id()

        # Make sure to associate the comment with the correct post_id
        new_comment = comment_repository_singleton.add_comment(user_id=user_id, post_id=post_id, comment_content=comment_content, comment_date_time=datetime.now())
        
        # Adds new comment to db
        db.session.add(new_comment)

        # Commits new comment
        db.session.commit()

    return redirect(url_for('forum'))

# Creates new user
@app.route('/users', methods=['POST'])
def create_user():
    first_name = request.form.get('first_name', '')
    last_name = request.form.get('last_name', '')
    email = request.form.get('email', '')
    password = request.form.get('password', '')

    created_user = user_repository_singleton.create_user(first_name, last_name, email, password)

    if created_user:
        return redirect(url_for('forum'))
    else:
        return redirect(url_for('code_400'))

# routes to redirect form on About Us page
@app.route('/create_account_redirect', methods=['POST'])
def create_account_redirect():
    if current_user.is_authenticated:
        return redirect(url_for('tech_portfolio'))
    else:
        return redirect(url_for('create_account_form'))

# runs application
if __name__ == '__main__':
    # creates db table
    db.create_all(bind='__all__', tables=[User.__table__, Post.__table__])
    app.run(debug=True)