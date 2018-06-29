from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/index')
def index():
    welcome_msg = "Welcome to my web site!"
    enjoy_msg = "Enjoy it!"
    return render_template("index.html",
                           msg1=welcome_msg,
                           msg2=enjoy_msg)


@app.route('/sample/<int:s_id>')
def sample(s_id):
    titles = {1: 'This is sample1 page.',
              2: 'This is sample2 page.',
              3: 'This is sample3 page.',
              4: 'This is sample4 page.'}
    if (s_id > 0) and (s_id < 5):
        return render_template("sample.html",
                               title=titles[s_id])
    else:
        return "The number of id must be between 1 and 4."


if __name__ == '__main__':
    app.run()  # the default ip and port is 127.0.0.1:5000
    # app.run(host='0.0.0.0', port=6006)  # to customize your ip and port
