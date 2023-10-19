const link = "https://duckos-juegos.pages.dev"
const config = {
  images: [
    {
      title: "Minecraft",
      url: "juegosfiles/minecraft/icon.png",
      link: "juegosfiles/minecraft/index.html"
    },
    {
      title: "Legend of Zelda",
      url: "icons/zelda.png",
      link: link + "/zelda",
    },
    {
      title: "2048",
      url: "icons/2048.png",
      link: "https://duckos-juegos.pages.dev/2048/"
    },
    {
      title: "Tank Trouble",
      url: "icons/tankt.png",
      link: "https://duckos-juegos.pages.dev/tanktrouble/"
    },
    {
      title: "Surviv.io",
      url: "icons/surviv.jpg",
      link: "https://duckos-juegos.pages.dev/surviv/"
    },
    {
      title: "Slope",
      url: "icons/slope.jpg",
      link: "https://duckos-juegos.pages.dev/slope/"
    },
    {
      title: "World's Hardest juegos",
      url: "icons/worlds-hardest-juegos.jpg",
      link: "https://duckos-juegos.pages.dev/worlds-hardest-juegos/"
    },
    {
      title: "World's Hardest juegos 2",
      url: "icons/worlds-hardest-juegos-2.jpg",
      link: "https://duckos-juegos.pages.dev/worlds-hardest-juegos-2/"
    },
    {
      title: "The Impossible Quiz",
      url: "icons/impossiblequiz.png",
      link: "https://duckos-juegos.pages.dev/the-impossible-quiz/"
    },
    {
      title: "Ducklife",
      url: "icons/ducklife.jpg",
      link: "https://duckos-juegos.pages.dev/ducklife/"
    },
    {
      title: "1v1.lol",
      url: "icons/1v1-lol.jpg",
      link: "https://duckos-juegos.pages.dev/1v1lol/"
    },
    {
      title: "paper.io",
      url: "icons/paperio.jpg",
      link: "https://duckos-juegos.pages.dev/paperio2/"
    },
    {
      title: "Tetris",
      url: "icons/tetris.png",
      link: "https://duckos-juegos.pages.dev/tetris/"
    },
    {
      title: "Pokemon Emerald (GBA)",
      url: "icons/emerald.jpg",
      link: "https://duckos-juegos.pages.dev/pokemon/emerald/"
    },
    {
      title: "Pokemon Fire Red (GBA)",
      url: "icons/fire.jpg",
      link: "https://duckos-juegos.pages.dev/pokemon/fire-red/"
    },
  ]
};

const gallery = document.getElementById('gallery');
const searchInput = document.getElementById('searchInput');

function renderGallery(images) {
  gallery.innerHTML = '';
  images.forEach(image => {
    const imageContainer = document.createElement('a');
    imageContainer.className = 'image-container';
    imageContainer.href = image.link;

    const img = document.createElement('img');
    img.className = 'image';
    img.src = image.url;
    img.alt = image.title;

    const content = document.createElement('div');
    content.className = 'content';

    const title = document.createElement('div');
    title.className = 'image-title';
    title.textContent = image.title;

    content.appendChild(title);
    imageContainer.appendChild(img);
    imageContainer.appendChild(content);
    gallery.appendChild(imageContainer);
  });
}

function filterImages(searchTerm) {
  const filteredImages = config.images.filter(image =>
    image.title.toLowerCase().includes(searchTerm.toLowerCase())
  );
  renderGallery(filteredImages);
}
renderGallery(config.images);
searchInput.addEventListener('input', () => {
  filterImages(searchInput.value);
});