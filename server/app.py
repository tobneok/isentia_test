from flask import Flask, request
from flask_cors import CORS

import database

app = Flask(__name__)
app.config["ERROR_404_HELP"] = False

# allow all for simplicity
CORS(app)

@app.route("/")
def landing():
    return """
        Hello, this is the News Article Searcher of Koen Douterloigne! <br>
        Please enter any keyword to search for articles containing that keyword<br>
        <form action="search" method="post">
        <input type="text" name="search" />
        </form>
    """

@app.route("/search", methods=['GET', 'POST'])
def search():
    data = request.values
    query = data['search']

    db = database.Database()
    results = db.search(query)

    print(results)

    if not results:
        return "No results found :("
    else:
        return "Results: " + str(results)

if __name__ == "__main__":
    app.run()
