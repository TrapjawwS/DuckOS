const appstoreToggle = document.getElementById("appstoretoggle");
const appstore = document.getElementById("appstore");

let isAppStoreVisible = false;

function showAppStore() {
  appstore.style.display = "block";
  isAppStoreVisible = true;
  setTimeout(() => {
    document.addEventListener("click", hideAppStoreOnClickOutside);
  }, 0);
}

function hideAppStore() {
  appstore.style.display = "none";
  isAppStoreVisible = false;
  document.removeEventListener("click", hideAppStoreOnClickOutside);
}

function toggleAppStore() {
  if (!isAppStoreVisible) {
    showAppStore();
  }
}


appstoreToggle.addEventListener("click", (event) => {
  event.stopPropagation();
  toggleAppStore();
});

function hideAppStoreOnClickOutside(event) {
  if (isAppStoreVisible && !appstore.contains(event.target) && event.target !== appstoreToggle) {
    hideAppStore();
  }
}

const config = [
  {
    imageSrc: '/media/icons/animal crossing.gif',
    title: 'Text based Animal Crossing',
    description: 'It\'s kinda mid tbh.',
    function1: () => {
      const animal = `
      <iframe src="https://replit.com/@Trapjaww/Animal-Crossing-V3?embed=true" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
    `
      const animalcrossing = {
        id: 1,
        imageSrc: '/media/icons/animal crossing.gif',
        text: 'Animal Crossing',
        clickFunction: function() {
          createWindow('Animal Crossing', animal, '60%', '70%');
        }
      };
      createApp(animalcrossing);
      localStorage.app1 = "true";
      console.log('Successfully installed the app "Animal Crossing" with the ID of "1".');
    },
    function2: () => {
      removeAppById(1);
      localStorage.app1 = "false";
      console.log('Successfully uninstalled the app "Animal Crossing" with the ID of "1".');
    },
    buttonTexts: ['Install App', 'Uninstall App']
  },
  {
    imageSrc: '/media/icons/fillericon.png',
    title: 'Eagler Craft',
    description: 'Yippe Minecraft.',
    function1: () => {
      const mc = `
      <iframe src="/eagleronline/index.html" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
    `
      const minecraft = {
        id: 2,
        imageSrc: '/media/icons/fillericon.png',
        text: 'Eagler Craft',
        clickFunction: function() {
          createWindow('Eagler Craft', mc, '60%', '70%');
        }
      };
      createApp(minecraft);
      console.log('Successfully installed the app "Eagler Craft" with the ID of "2".');
    },
    function2: () => {
      removeAppById(1);
      console.log('Successfully uninstalled the app "Eagler Craft" with the ID of "2".');
    },
    buttonTexts: ['Install App', 'Uninstall App']
  }
];

const rowsContainer = document.getElementById('rows');

config.forEach((item, index) => {
  const row = document.createElement('div');
  row.classList.add('row');

  const image = document.createElement('img');
  image.src = item.imageSrc;
  image.alt = `Image ${index + 1}`;
  image.classList.add('image');
  row.appendChild(image);

  const info = document.createElement('div');
  info.classList.add('info');

  const title = document.createElement('h2');
  title.textContent = item.title;
  info.appendChild(title);

  const description = document.createElement('p');
  description.textContent = item.description;
  info.appendChild(description);

  const button = document.createElement('button');
  button.textContent = item.buttonTexts[0];
  button.classList.add('appstorebtn');
  let functionIndex = 1;
  let isLoading = false;

  button.addEventListener('click', () => {
    if (!isLoading) {
      if (functionIndex === 1) {
        isLoading = true;
        button.textContent = 'Installing app, please wait...';
        setTimeout(() => {
          item.function1();
          button.textContent = item.buttonTexts[1];
          isLoading = false;
        }, 2000);

      } else if (functionIndex === 2) {
        isLoading = true;
        button.textContent = 'Uninstalling app, please wait...';
        setTimeout(() => {
          item.function2();
          button.textContent = item.buttonTexts[0];
          isLoading = false;
        }, 1000);
      }
      functionIndex = functionIndex === 1 ? 2 : 1;
    }
  });

  info.appendChild(button);
  row.appendChild(info);
  rowsContainer.appendChild(row);
});
