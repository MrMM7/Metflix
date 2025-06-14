const params = new URLSearchParams(window.location.search);
const movieName = params.get("m");
const videoPlayer = document.querySelector("video");
const descriptionBox = document.querySelector(".movie-description");
const movieNameDiv = document.querySelector(".movie-title");

let allMovies = [];
fetch("/api/all-movies")
  .then((res) => {
    if (!res.ok) {
      throw new Error("Could not GET from movies server");
    }
    return res.json();
  })
  .then((obj) => {
    allMovies.push(obj);
    const moviesArray = Object.values(allMovies[0]);
    moviesArray.forEach((item) => {
      videoPlayer.src = `../static/movies/${item.ms}`;
      descriptionBox.innerHTML = item.d;
      movieNameDiv.innerHTML = item.m;
      document.title = `Watch - ${movieName}`;
    });
  })
  .catch((err) => console.error(err));
