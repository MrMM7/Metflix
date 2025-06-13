function addMovie(name, imageName) {
  let containerDiv = document.getElementById("movie-container");
  let htmlTemplate = `
    <div class="movie-card">
    <a href="/watch?m=${encodeURI(name)}">
    <img class="movie-thumb" src="../${imageName}" alt="Movie 1" />
    <div class="movie-title">${name}</div>
    </a>
    </div>
    `;
  containerDiv.insertAdjacentHTML("beforeend", htmlTemplate);
}

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
      addMovie(item.m, item.mc);
    });
  })
  .catch((err) => console.error(err));
