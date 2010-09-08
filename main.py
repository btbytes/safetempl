import os
from flask import Flask
from jinja2 import FileSystemLoader
from jinja2.sandbox import SandboxedEnvironment

app = Flask(__name__)
loader = FileSystemLoader(os.path.join(os.getcwd(), 'templates'))
env = SandboxedEnvironment(loader=loader)
def render_template(tmpl_name, **kw):
	tmpl = env.get_template(tmpl_name)
	return tmpl.render(**kw)

@app.route("/")
def home():
    return render_template("home.html", msg="Hello world!")

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)