const params = new URLSearchParams(window.location.search);
const movieID = params.get("id");
const videoPlayer = document.querySelector("video");
const descriptionBox = document.querySelector(".movie-description");
const movieName = document.querySelector(".movie-title");

let allMovies = [];

fetch(`/api/movies/${movieID}`, {
  method: "GET",
})
  .then((res) => {
    if (!res.ok) throw new Error("Cannot GET movie from server");
    return res.json();
  })
  .then((item) => {
    videoPlayer.src = `../static/movies/${item.ms}`;
    descriptionBox.innerHTML = item.d;
    movieName.innerHTML = item.m;
    document.title = `Watch - ${movieName}`;
  })
  .catch((err) => console.error(err));
