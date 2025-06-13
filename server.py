from flask import Flask, render_template, jsonify
import json
import threading
import webbrowser

app = Flask(__name__)
jsonfile_data = []

# turning the JSON into regular dictionaries 
with open("db.json", 'r') as f:
     jsonfile_data = list(json.load(f).values())

# main page
@app.route('/home')
def index():
    return render_template("front-page.html")

# watching page
@app.route('/watch')
def watching_page():
    return render_template("watch.html")

# returns the requested movie by the front-end
@app.route('/api/movies/<name>', methods=['GET'])
def get_movie(name: str):
    print("🔎 API received request for:", name)
    print("📦 Current jsonfile_data:", jsonfile_data)

    for movie in jsonfile_data.values():  #type: ignore
        print("🔍 Comparing with:", movie['m'])  # Debug print    #type: ignore
        if movie['m'] == name:
            print("✅ Match found!")
            return jsonify(movie)

    print("❌ Movie not found!")
    return jsonify({'error': 'Movie not found'}), 404

# sends the db.json file to the front-end
@app.route('/api/all-movies', methods=['GET'])
def get_all_movies():
    return jsonify(jsonfile_data)


# this automatically opens the webbrowser and show the site without needing to do it manually
def open_browser():
    webbrowser.open_new_tab("http://localhost:5000/home")

if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()
    app.run()