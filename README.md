## Flask
A comprehensive flask web project.<br>
You can understand how to develop html pages and APIs with cache and multiprocessing in flask.<br>
As well as you can understand how to deploy the project into apache on ubuntu.

## Updated List

### Version 1.0
You can understand the relationship between flask, html, and other static file such as js, css and image.<br>
The following samples are available:<br>
* http://127.0.0.1:5000/
* http://127.0.0.1:5000/index
* http://127.0.0.1:5000/sample/{int}<br>
The examples:<br>
http://127.0.0.1:5000/sample/1<br>
http://127.0.0.1:5000/sample/3
* http://127.0.0.1:5000/employee<br>
Post data by html form.

### Version 2.0
You can understand the development of api which return a json string with get or post method.<br>
The following samples are available:<br>
* GET: http://127.0.0.1:5000/api/employee/{int} <br>
The examples:<br>
http://127.0.0.1:5000/api/employee/1<br>
http://127.0.0.1:5000/api/employee/66
* POST: http://127.0.0.1:5000/api/employee <br>
The post json examples:<br>
{"e_id": 1}<br>
{"e_id": 66}

## Environment

### Development
* Python 3.5.2
* Flask 1.0.2

### Deployment
* Ubuntu 16.04.3 LTS
* Apache 2.4.18
* mod_wsgi 4.3.0

There is a tutorial which teach you how to deploy the project into apache on ubuntu.
Please refer to this [gitbook](https://bobtai.gitbooks.io/mynotes/content/AWS/flask_apache.html) to get more deployment tutorial.