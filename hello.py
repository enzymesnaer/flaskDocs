from flask import Flask

app = Flask(__name__)

"""
@app.route('/')
def hello_world():
    return 'Hello, World!'
"""

# To run the application you can either use the flask command or python’s -m switch with Flask. Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:

# set FLASK_APP=hello.py
# python -m flask run
# you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:


# set FLASK_ENV=development
# python -m flask run

"""
@app.route('/')
def index():
    return 'Index Page!'

@app.route('/hello')
def hello():
    return 'Hello, World!'
"""
    
# *************************************************

# You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the <variable_name> as a keyword argument. Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.
"""
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)
"""
"""
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
"""
"""
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
"""


# Unique URLs / Redirection Behavior
"""
@app.route('/projects/')
def projects():
    return 'The project page'
"""
# Flask redirects you to the canonical URL with the trailing slash.
"""
@app.route('/about')
def about():
    return 'The about page'
"""
# The canonical URL for the about endpoint does not have a trailing slash. It’s similar to the pathname of a file. Accessing the URL with a trailing slash produces a 404 “Not Found” error.

#********************************************************************

# URL Building

#  To build a URL to a specific function, use the url_for() function.

# Why would you want to build URLs using the URL reversing function url_for() instead of hard-coding them into your templates?

"""
from flask import Flask, escape, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
"""

# HTTP Methods
# By default, a route only answers to GET requests. You can use the methods argument of the route() decorator to handle different HTTP methods.

"""
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
"""

# Static Files
# CSS or JS files will be made available by your local /static folder on the application

# To generate URLs for static files, use the special 'static' endpoint name:

"""
url_for('static', filename='style.css')

The file has to be stored on the filesystem as static/style.css.
"""

# Rendering Templates

"""
Flask configures the Jinja2 template engine for you automatically.

To render a template you can use the render_template() method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments.
"""

"""
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
"""

"""
Flask will look for templates in the templates folder. So if your application is a module, this folder is next to that module, if it’s a package it’s actually inside your package:
----------------------------------------------
Case 1: a module:

/application.py
/templates
    /hello.html
----------------------------------------------
Case 2: a package:

/application
    /__init__.py
    /templates
        /hello.html
-----------------------------------------------
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
------------------------------------------------

"""
# ----------------------------------------------------------------------
# https://www.smartlabsoftware.com/ref/http-status-codes.htm
# https://2.python-requests.org/en/master/user/quickstart/#make-a-request
# https://2.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
# https://2.python-requests.org/en/master/user/quickstart/#response-content
# https://2.python-requests.org/en/master/user/quickstart/#binary-response-content
# https://2.python-requests.org/en/master/user/quickstart/#json-response-content
# https://2.python-requests.org/en/master/user/quickstart/#raw-response-content
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
# https://developer.mozilla.org/en-US/docs/Glossary/General_header
# https://developer.mozilla.org/en-US/docs/Glossary/CORS
# https://developer.mozilla.org/en-US/docs/Glossary/Request_header
# https://developer.mozilla.org/en-US/docs/Glossary/Response_header
# https://developer.mozilla.org/en-US/docs/Glossary/Entity_header
# https://2.python-requests.org/en/master/user/quickstart/#custom-headers
# https://2.python-requests.org/en/master/user/quickstart/#more-complicated-post-requests
# https://2.python-requests.org/en/master/user/quickstart/#post-a-multipart-encoded-file
# https://2.python-requests.org/en/master/user/quickstart/#response-status-codes
# https://2.python-requests.org/en/master/user/quickstart/#response-headers
# https://2.python-requests.org/en/master/user/quickstart/#errors-and-exceptions
# https://2.python-requests.org/en/master/user/quickstart/#redirection-and-history
# https://2.python-requests.org/en/master/user/quickstart/#timeouts
# https://2.python-requests.org/en/master/user/quickstart/#redirection-and-history
# https://2.python-requests.org/en/master/user/quickstart/#cookies
# https://www.programiz.com/python-programming/regex
# https://www.programiz.com/python-programming/exceptions
# https://www.programiz.com/python-programming/list-comprehension
# https://www.programiz.com/python-programming/directory
# https://www.programiz.com/python-programming/file-operation
# https://www.programiz.com/python-programming/decorator
# ----------------------------------------------------------------------

"""
Accessing Request Data
"""
# It’s crucial to react to the data a client sends to the server. In Flask this information is provided by the global request object.

# test_request_context()
"""
from flask import request

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'
"""

# The Request Object
# https://www.youtube.com/watch?v=Ih-UJFNOP-c
# https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request
# https://flask.palletsprojects.com/en/1.1.x/api/#response-objects

# About Responses
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#about-responses


# APIs with JSON
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#apis-with-json



"""
from flask import request

The current request method is available by using the method attribute. To access form data (data transmitted in a POST or PUT request) you can use the form attribute. Here is a full example of the two attributes mentioned above:

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

"""


# FILE UPLOAD

# You can handle uploaded files with Flask easily. Just make sure not to forget to set the enctype="multipart/form-data" attribute on your HTML form, otherwise the browser will not transmit your files at all.

# Uploaded files are stored in memory or at a temporary location on the filesystem. You can access those files by looking at the files attribute on the request object. Each uploaded file is stored in that dictionary. It behaves just like a standard Python file object, but it also has a save() method that allows you to store that file on the filesystem of the server.

"""
from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    ...
"""

# Cookies
# The cookies attribute of request objects is a dictionary with all the cookies the client transmits.
"""
Reading cookies:

from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.



Storing cookies:

from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
"""
# Note that cookies are set on response objects. Since you normally just return strings from the view functions Flask will convert them into response objects for you.

# ------------------------------------------------------------------


# Redirects and Errors

# To redirect a user to another endpoint, use the redirect() function; to abort a request early with an error code, use the abort() function:

"""
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
This is a rather pointless example because a user will be redirected from the index to a page they cannot access (401 means access denied) but it shows how that works.
"""


"""
By default a black and white error page is shown for each error code. If you want to customize the error page, you can use the errorhandler() decorator:

from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
Note the 404 after the render_template() call. This tells Flask that the status code of that page should be 404 which means not found. By default 200 is assumed which translates to: all went well.
"""

# -------------------------------------------------------------------

# Sessions
"""
In addition to the request object there is also a second object called session which allows you to store information specific to a user from one request to the next. This is implemented on top of cookies for you and signs the cookies cryptographically. What this means is that the user could look at the contents of your cookie but not modify it, unless they know the secret key used for signing.

In order to use sessions you have to set a secret key. Here is how sessions work:

from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

"""
"""
Next>>