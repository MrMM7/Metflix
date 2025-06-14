from flask import Flask, render_template, jsonify
import json
import threading
import webbrowser

auto_open_browser = True
app = Flask(__name__)
jsonfile_data = []

# turning the JSON into regular dictionaries 
with open("db.json", 'r') as f:
     jsonfile_data = list(json.load(f).values())

# main page
@app.route('/home')
def home_page():
    return render_template("front-page.html")

# watching page
@app.route('/watch')
def watching_page():
    return render_template("watch.html")

# returns the requested movie by the front-end
@app.route('/api/movies/<int:id>', methods=['GET'])
def get_movie(id: int):
    for i in range(len(jsonfile_data)):
        if jsonfile_data[i]['id'] == id:
            print(jsonfile_data[i])
            return jsonify(jsonfile_data[i]), 200
        
    return jsonify(f"Movie does not exist id:{id}"), 404
    

# sends the db.json file to the front-end
@app.route('/api/all-movies', methods=['GET'])
def get_all_movies():
    return jsonify(jsonfile_data)


# this automatically opens the webbrowser and show the site without needing to do it manually
def open_browser():
    webbrowser.open_new_tab("http://localhost:5000/home")

if __name__ == "__main__":
    if auto_open_browser: threading.Timer(1.0, open_browser).start()

    app.run()