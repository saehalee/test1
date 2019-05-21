from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'
@app.route('/about')
def about():
    return 'The About Page'

@app.route('/blog')
def blog():
    return '''
    <html>
    <head></head>
    <body>
    <h2>Welcome to this blog! </h2>
    <p>I am Avi, the author of this </p>
    </body>
    '''

@app.route('/blog/<blog_id>')
def blogpost(blog_id):
    return 'This is blog post number' + str(blog_id)
