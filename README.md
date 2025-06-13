# Metflix

A streaming service web app — a recreation of my past non-functioning streaming service, now **fully functioning**!

---

## Features

- Browse a library of movies  
- Watch movies with video player  
- Movie details with cover image and description  

---

## Getting Started

### 1. Add Your Movies & Covers

- Put your movie files inside the `static/movies/` folder.  
- Put your movie cover images inside the `static/thumbnail/` folder.  

---

### 2. Update `db.json`

Add an entry for each movie in `db.json` like this:

```json
"1": {
  "m": "Morbius",                                   // Movie name
  "ms": "static/movies/movie1.mp4",                 // Movie source (file path)
  "mc": "static/thumbnail/Morbius.jpg",             // Movie cover image path
  "d": "funny green guy"                            // Description
}
```

Make sure the paths match the files you added in step 1.

---

### 3. Run the Server

Start the Flask server by running:

```
python server.py
```

Wait a few seconds — your default web browser will automatically open the app at:

```
http://localhost:5000/home
```

---

## Notes

- The front-end UI design was generated with the help of AI, but all the programming and backend work were done mostly by me.
- Ensure your movie and cover image file names and paths in `db.json` exactly match what’s in your `static` folders.  
- To add more movies, add new numbered keys in `db.json` (`"2"`, `"3"`, etc.) with the same structure.

---

## Tech Stack

- Python Flask (backend)  
- HTML/CSS/JS (frontend)  
- JSON file as simple database  

---

Feel free to contribute or open issues!

---

Made by MrMM7
