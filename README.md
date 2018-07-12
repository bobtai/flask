## Flask
A simple flask web site.<br>
You can understand how to deploy the project into apache on ubuntu.

## Updated List

### Version 1.0
You can understand the relationship of python, html, and other static file such as js, css and image.<br>
The following samples are available:<br>
* http://127.0.0.1:5000/
* http://127.0.0.1:5000/index
* http://127.0.0.1:5000/sample/<int>


### Version 2.0
You can understand the development of api which return a json string with get or post method.<br>
The following samples are available:<br>
* http://127.0.0.1:5000/api/employee/{int} (GET)
* http://127.0.0.1:5000/api/employee (POST)<br>
The post json string is like this:`{"e_id": 1}`

## Environment

### Development
* Python 3.5.2
* Flask 1.0.2

### Deployment
* Ubuntu 16.04.3 LTS
* Apache 2.4.18
* mod_wsgi 4.3.0

More deployment tutorial please refer to this [gitbook](https://bobtai.gitbooks.io/mynotes/content/AWS/flask_apache.html).