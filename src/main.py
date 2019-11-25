import os
import markdown
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# restful api
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/api')

# traditional Flask
@app.route('/')
def hello_world():
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()

        return markdown.markdown(content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
