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
      console.log('Successfully installed the app "Animal Crossing" with the ID of "1".');
    },
    function2: () => {
      removeAppById(1);
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
      removeAppById(2);
      console.log('Successfully uninstalled the app "Eagler Craft" with the ID of "2".');
    },
    buttonTexts: ['Install App', 'Uninstall App']
  },
  {
    imageSrc: '/media/icons/fillericon.png',
    title: 'Cookie Clicker',
    description: 'Om Nom Nom I love cookies. (It\'s kinda broken, but i\'m trying to fix it)',
    function1: () => {
      const cookie = `
      <iframe src="/cookie clicker/index.html" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
    `
      const clicker = {
        id: 3,
        imageSrc: '/media/icons/fillericon.png',
        text: 'Cookie Clicker',
        clickFunction: function() {
          createWindow('Cookie Clicker', cookie, '60%', '70%');
        }
      };
      createApp(clicker);
      console.log('Successfully installed the app "Cookie Clicker" with the ID of "3.');
    },
    function2: () => {
      removeAppById(3);
      console.log('Successfully uninstalled the app "Cookie Clicker" with the ID of "3".');
    },
    buttonTexts: ['Install App', 'Uninstall App']
  },
  {
    imageSrc: '/media/icons/fillericon.png',
    title: 'Sonic',
    description: 'Zoom.',
    function1: () => {
      const zoom = `
      <iframe src="/sonic.html" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
    `
      const sonic = {
        id: 4,
        imageSrc: '/media/icons/fillericon.png',
        text: 'Sonic',
        clickFunction: function() {
          createWindow('Sonic', zoom, '60%', '70%');
        }
      };
      createApp(sonic);
      console.log('Successfully installed the app "Sonic" with the ID of "4".');
    },
    function2: () => {
      removeAppById(4);
      console.log('Successfully uninstalled the app "Sonic" with the ID of "4".');
    },
    buttonTexts: ['Install App', 'Uninstall App']
  },
  {
    imageSrc: '/media/icons/fillericon.png',
    title: 'Meat Boy',
    description: '*squishy flesh noises*.',
    function1: () => {
      const meat = `
      <iframe src="/supermeatboy.html" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
    `
      const meatboy = {
        id: 5,
        imageSrc: '/media/icons/fillericon.png',
        text: 'Meat Boy',
        clickFunction: function() {
          createWindow('Meat Boy', meat, '60%', '70%');
        }
      };
      createApp(meatboy);
      console.log('Successfully installed the app "Meat Boy" with the ID of "5".');
    },
    function2: () => {
      removeAppById(5);
      console.log('Successfully uninstalled the app "Meat Boy" with the ID of "5".');
    },
    buttonTexts: ['Install App', 'Uninstall App']
  },
  {
    imageSrc: '/media/icons/fillericon.png',
    title: 'The Binding Of Isaac',
    description: 'W game you should play',
    function1: () => {
      const isaac = `
      <iframe src="/tboi.html" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
    `
      const tboi = {
        id: 6,
        imageSrc: '/media/icons/fillericon.png',
        text: 'The Binding Of Isaac',
        clickFunction: function() {
          createWindow('The Binding Of Isaac', isaac, '60%', '70%');
        }
      };
      createApp(tboi);
      console.log('Successfully installed the app "The Binding Of Isaac" with the ID of "6".');
    },
    function2: () => {
      removeAppById(6);
      console.log('Successfully installed the app "The Binding Of Isaac" with the ID of "6".');
    },
    buttonTexts: ['Install App', 'Uninstall App']
  },
  {
    imageSrc: '/media/icons/fillericon.png',
    title: 'Tetris',
    description: 'I <3 the tetris soundtrack',
    function1: () => {
      const tetris = `
      <iframe src="/tetris.html" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
    `
      const tetrisgame = {
        id: 7,
        imageSrc: '/media/icons/fillericon.png',
        text: 'Tetris',
        clickFunction: function() {
          createWindow('Tetris', tetris, '60%', '70%');
        }
      };
      createApp(tetrisgame);
      console.log('Successfully installed the app "Tetris" with the ID of "7".');
    },
    function2: () => {
      removeAppById(7);
      console.log('Successfully installed the app "Tetris" with the ID of "7".');
    },
    buttonTexts: ['Install App', 'Uninstall App']
  },
  {
    imageSrc: '/media/icons/fillericon.png',
    title: 'Super Smash Flash',
    description: 'Super Smash Bros Knockoff',
    function1: () => {
      const supersmash = `
      <iframe src="/supersmashflash.html" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
    `
      const supersmashflash = {
        id: 8,
        imageSrc: '/media/icons/fillericon.png',
        text: 'Super Smash Flash',
        clickFunction: function() {
          createWindow('Super Smash Flash', supersmash, '60%', '70%');
        }
      };
      createApp(supersmashflash);
      console.log('Successfully installed the app "Super Smash Flash" with the ID of "8".');
    },
    function2: () => {
      removeAppById(8);
      console.log('Successfully installed the app "Super Smash Flash" with the ID of "8".');
    },
    buttonTexts: ['Install App', 'Uninstall App']
  },
  {
    imageSrc: '/media/icons/fillericon.png',
    title: 'SM64',
    description: 'Yahoo!',
    function1: () => {
      const sm64 = `
      <iframe src="/sm64/index.html" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
    `
      const mario = {
        id: 10,
        imageSrc: '/media/icons/fillericon.png',
        text: 'SM64',
        clickFunction: function() {
          createWindow('SM64', sm64, '60%', '70%');
        }
      };
      createApp(mario);
      console.log('Successfully installed the app "SM64" with the ID of "10".');
    },
    function2: () => {
      removeAppById(10);
      console.log('Successfully installed the app "SM64" with the ID of "10".');
    },
    buttonTexts: ['Install App', 'Uninstall App']
  },
  {
    imageSrc: '/media/icons/fillericon.png',
    title: 'Emulator',
    description: 'No ROMs Provided. It supports most retro consoles, so yeah.',
    function1: () => {
      const gba = `
      <iframe src="/emulator.html" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
    `
      const gbaemulator = {
        id: 9,
        imageSrc: '/media/icons/fillericon.png',
        text: 'Emulator',
        clickFunction: function() {
          createWindow('Emulator', gba, '60%', '70%');
        }
      };
      createApp(gbaemulator);
      console.log('Successfully installed the app "Emulator" with the ID of "9".');
    },
    function2: () => {
      removeAppById(9);
      console.log('Successfully installed the app "Emulator" with the ID of "9".');
    },
    buttonTexts: ['Install App', 'Uninstall App']
  },
  {
    imageSrc: '/media/icons/fillericon.png',
    title: 'BTD5',
    description: 'pop the balloons',
    function1: () => {
      const btd5 = `
      <iframe src="/btd5/index.html" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
    `
      const monkey = {
        id: 10,
        imageSrc: '/media/icons/fillericon.png',
        text: 'BTD5',
        clickFunction: function() {
          createWindow('BTD5', btd5, '60%', '70%');
        }
      };
      createApp(monkey);
      console.log('Successfully installed the app "BTD5" with the ID of "10".');
    },
    function2: () => {
      removeAppById(10);
      console.log('Successfully installed the app "BTD5" with the ID of "10".');
    },
    buttonTexts: ['Install App', 'Uninstall App']
  },
  {
    imageSrc: '/media/icons/fillericon.png',
    title: 'Monkey Mart',
    description: 'B A N A N A',
    function1: () => {
      const monkeymart = `
      <iframe src="/monkey mart/index.html" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
    `
      const banana = {
        id: 11,
        imageSrc: '/media/icons/fillericon.png',
        text: 'Monkey Mart',
        clickFunction: function() {
          createWindow('Monkey Mart', monkeymart, '60%', '70%');
        }
      };
      createApp(banana);
      console.log('Successfully installed the app "Monkey Mart" with the ID of "11".');
    },
    function2: () => {
      removeAppById(11);
      console.log('Successfully installed the app "Monkey Mart" with the ID of "11".');
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
