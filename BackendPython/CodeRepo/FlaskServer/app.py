from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskServer.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)






# from http.server import HTTPServer, BaseHTTPRequestHandler
# from flask import Flask, abort, redirect, url_for


# app = Flask(__name__)

# hostName = "localhost"
# serverPort = 8080
# @app.route('/')
# def index():
#     return "<h1>This is a project</h1>"

# @app.route('/home')
# def home():
#     return ("<nav><div><h1>NeedlePoint</h1></nav>")

# @app.route('/about')
# def about():
#     return "<h1>This is an about page</h1> "

# @app.route('/login')
# def login():
#     abort(401)



# if __name__ == '__main__':
#     webServer = HTTPServer((hostName, serverPort), Flask)
#     app.run(debug=True)
#     print("Server started http://%s:%s" % (hostName, serverPort))

#     try: 
#         webServer.serve_forever()
#     except KeyboardInterrupt:
#         pass

#     webServer.server_close()
#     print("Server stopped.")