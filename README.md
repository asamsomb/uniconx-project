# Flask Discussion Forum with User Account Features

This application uses the **Flask** framework to create a full-stack application expanding our first product, UniConX. 
This discussion forum uses the following features: user account login and registration, thread management, commenting/replying to a thread, and editing and deleting a post.

## Authors

- Zainab Bello (@ZayLaVie) zbello@uncc.edu
- Aida Samsombath (@asamsomb) asamsomb@uncc.edu
- Rida Fatimah (@ridars01) rfatimah@uncc.edu
- Sofia Mata Avila (@sofiamata457) smataavi@uncc.edu
- Brianna Caudle (@BriannaNC) bcaudle6@uncc.edu

## Description

The purpose of this Flask application allows users to interact and engage with one another to provide solutions, scholarly advice, and professional recommendations.
The problem it addresses occurs within newly introduced undergraduate students (freshmen and sophomores) who lack opportunity to attend networking or skill-building events due to a full schedule or other engagements.
Upperclassmen (juniors and seniors) who use this application can ask questions and share information with one another as well as underclassmen about recruitment and career trends.

## Technologies

### Front-End

* [Bootstrap V4](https://getbootstrap.com) - Bootstrap is a well-known open-source front-end framework used for responsive web-page design and development.
* [jQuery V3](https://api.jquery.com) - jQuery allows enhanced JavaScript accessibility and promotes cross-browser compatibility in web-development.
* [Popper V1](https://popper.js.org/docs/v2) - Popper is a web-development JavaScript library used to incorporate positioning of UI elements in Bootstrap.

### Back-End 

* Python 3.11.7
* MySQL - Production
* [Flask V3](https://flask.palletsprojects.com/en/3.0.x) - Python Framework for Web Applications
* [Pip V23](https://pypi.org/project/pip/23.2.1) - Python Library and Package Management and Installation

## Features

* CRUD (create / read / update / delete) threads or posts.
* Create, read, and update comments.
* User registration and login.
* Account authentication.
* Commenting and thread reply.

## Prequisites

* Python 3.11 or above
```shell
# Check Python Version:
    $ python --version
```

* Pip 23.2
```shell
# Check Pip Version:
    $ pip --version
```

* MySQL Workbench 8.0 CE 
* Git and Git Bash

## Installation

* Clone project from GitHub repository using Git Bash.

```shell
    $ https://github.com/ZayLaVie/ZeBRA-Project.git
    $ cd ZeBRA-Project
```

* Create Virtual Environment. Confirm you are in the virtual environment when '(venv)' is visibile.

```shell
# Use 'python3' or 'python' according to your Python version. 
    $ python -m venv venv
    $ source venv/Scripts/activate
```

* Install dependencies from requirements.txt within the virtual environment. 

```shell
# Use 'pip' or 'pip3' according to your Pip version.
    $ pip install -r requirements.txt
```

* **Prior to running the development server, please ensure that you've created a database from 'user_accounts.sql' with the following tables:**

```shell
    post
    comment
    user
```

* Run development server.

```shell
    $ flask run
```