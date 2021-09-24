from flask import Flask, jsonify

# Intializes flask app
app = Flask(__name__)

books = [{
"id":1,
"title":"Python for beginners",
},
{
"id":2,
"title":"Automation with python",
},
{
"id":3,
"title":"Python API mastery",
}]

# Home page that displays "Hello World"
@app.route('/')
def index():
    return "Hello World"

# Route to get all books 
@app.route('/api/v1/books', methods=['GET'])
def get_books():
    return jsonify({"books":books})

# Route to get single book based on ID
@app.route('/api/v1/books/<int:id>', methods=['GET'])
def get_book(id):
    book = [book for book in books if book['id'] == id]
    return jsonify({'book': book})

# Initialize serrver for app to run
if __name__ == "__main__":
    app.run(debug=True)