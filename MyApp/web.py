from flask import Flask, request, jsonify
from flask import render_template


app = Flask(__name__)


class Employee:
    def __init__(self, e_id, e_name, participation_project):
        self.e_id = e_id
        self.e_name = e_name
        self.participation_project = participation_project


def get_employee(num):
    str_num = str(num)
    e_id = 'id_' + str_num
    e_name = 'name_' + str_num
    ptcpt_project = ['A00' + str_num, 'B00' + str_num]
    return Employee(e_id, e_name, ptcpt_project)


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


@app.route('/employee', methods=['GET', 'POST'])
def get_employee_by_form():
    if request.method == 'GET':
        return render_template("form.html")
    else:
        req_id = int(request.form['id'])
        return render_template("form.html",
                               json_str=get_employee(req_id).__dict__)


@app.route('/api/employee/<int:e_id>', methods=['GET'])
def get_employee_by_get(e_id):
    return jsonify(get_employee(e_id).__dict__)


@app.route('/api/employee', methods=['POST'])
def get_employee_by_post():
    try:
        # Setting force=True will ignore
        # the request.headers.get('Content-Type') == 'application/json' check
        # that flask does for you.
        content = request.get_json(force=True)
        e_id = content['e_id']
        return jsonify(get_employee(e_id).__dict__)
    except KeyError:
        return jsonify({'result': 'KeyError'})


if __name__ == '__main__':
    app.run()  # the default ip and port is 127.0.0.1:5000
    # app.run(host='0.0.0.0', port=6006)  # to customize your ip and port
