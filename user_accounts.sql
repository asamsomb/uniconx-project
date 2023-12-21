USE user_accounts_schema;
-- Create a table to store user information
CREATE TABLE user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Test User
INSERT INTO user (first_name, last_name, username, password)
VALUES ('John', 'Doe', 'john.doe@example.com', PASSWORD('user_password'));

-- Create a table to store posts
CREATE TABLE posts (
    post_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(255) NOT NULL,
    post_date_time DATETIME NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

-- Test Post
INSERT INTO posts (user_id, title, post_date_time, content)
VALUES (1, 'My First Post', NOW(), 'This is the content of my first post.');

-- Create table to store comments
CREATE TABLE comments (
	comment_id INT AUTO_INCREMENT PRIMARY KEY,
    post_id INT,
    user_id INT,
    comment_date_time DATETIME NOT NULL,
    comment_content TEXT NOT NULL,
    FOREIGN KEY (post_id) REFERENCES post(post_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

-- Test Comment
INSERT INTO comments (post_id, user_id, comment_date_time, comment_content)
VALUES (1, 1, NOW(), 'Sample comment on first post.');