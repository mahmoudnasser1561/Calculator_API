from flask import Flask
from flask_restful import Api
from routes.add import Add
from routes.subtract import Subtract

app = Flask(__name__)
api = Api(app)


# Home route
@app.route('/')
def home():
    return '''
    <h1>Welcome to the Math API</h1>
    <p>Use the following endpoints:</p>
    <ul>
        <li><b>POST /add</b>: JSON with "x" and "y" to return x + y</li>
        <li><b>POST /subtract</b>: JSON with "x" and "y" to return x - y</li>
    </ul>
    '''

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")

if __name__ == "__main__":
    app.run(debug=True)