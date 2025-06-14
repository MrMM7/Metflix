function addMovie(name, imageName, id) {
  let containerDiv = document.getElementById("movie-container");
  let htmlTemplate = `
    <div class="movie-card">
    <a href="/watch?id=${id}">
    <img class="movie-thumb" src="../static/thumbnail/${imageName}"/>
    <div class="movie-title">${name}</div>
    </a>
    </div>
    `;
  containerDiv.insertAdjacentHTML("beforeend", htmlTemplate);
}

let allMovies = [];
fetch("/api/movies/all-movies", {
  method: "GET",
})
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
      addMovie(item.m, item.mc, item.id);
    });
  })
  .catch((err) => console.error(err));
