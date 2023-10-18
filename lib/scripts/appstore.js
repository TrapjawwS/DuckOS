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
    imageSrc: '/media/icons/notes.png',
    title: 'Notes',
    description: 'It\'s just a notes app... do I really need to explain everything?',
    function1: () => {
      const notesApp = `
          <iframe src="https://www.rapidtables.com/tools/notepad.html" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
        `
      const notes = {
        id: 5,
        imageSrc: '/media/icons/notes.png',
        text: 'Notes',
        clickFunction: function() {
          createWindow('Notes', notesApp, '70%', '60%');
        }
      };
      createApp(notes);
      console.log('Successfully installed the app "Notes" with the ID of "5".');
    },
    function2: () => {
      removeAppById(5);
      console.log('Successfully uninstalled the app "Notes" with the ID of "5".');
    },
    buttonTexts: ['Install Notes', 'Uninstall Notes']
  },
  {
    imageSrc: '/media/icons/meowie.png',
    title: 'Meowie Games',
    description: 'Description for this app... blah blah blah...',
    function1: () => {
      const meowie = `
          <iframe src="https://meowiegames.com/home.html" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
        `
      const meowieGames = {
        id: 6,
        imageSrc: '/media/icons/meowie.png',
        text: 'Meowzie\'s Adventures',
        clickFunction: function() {
          createWindow('Meowie Games', meowie, '60%', '70%');
        }
      };
      createApp(meowieGames);
      console.log('Successfully installed the app "Meowie Games" with the ID of "6".');
    },
    function2: () => {
      removeAppById(6);
      console.log('Successfully uninstalled the app "Meowie Games" with the ID of "6".');
    },
    buttonTexts: ['Install App', 'Uninstall App']
  },
  {
    imageSrc: '/media/icons/clock.png',
    title: 'Clockworks',
    description: 'ANOTHER OS?!?',
    function1: () => {
      const clock = `
      <iframe src="/system/apps/clockworks/clockworks.html" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
    `
      const clockworks = {
        id: 7,
        imageSrc: '/media/icons/clock.png',
        text: 'Clockworks',
        clickFunction: function() {
          createWindow('Clockworks', clock, '60%', '70%');
        }
      };
      createApp(clockworks);
      console.log('Successfully installed the app "Clockworks" with the ID of "7".');
    },
    function2: () => {
      removeAppById(7);
      console.log('Successfully uninstalled the app "Clockworks" with the ID of "7".');
    },
    buttonTexts: ['Install App', 'Uninstall App']
  },
  {
    imageSrc: '/media/icons/calender.jpg',
    title: 'Homework Organizer/Reminder',
    description: 'A good app for reminding you to do homework.',
    function1: () => {
      const homework = `
      <iframe src="https://your-haru.netlify.app/" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
    `
      const homeworkreminder = {
        id: 8,
        imageSrc: '/media/icons/calender.jpg',
        text: 'Homework Reminder',
        clickFunction: function() {
          createWindow('Homework Reminder', homework, '60%', '70%');
        }
      };
      createApp(homeworkreminder);
      console.log('Successfully installed the app "Homework Reminder" with the ID of "8".');
    },
    function2: () => {
      removeAppById(8);
      console.log('Successfully uninstalled the app "Homework Reminder" with the ID of "8".');
    },
    buttonTexts: ['Install App', 'Uninstall App']
  },
  {
    imageSrc: '/media/icons/schoology.png',
    title: 'Schoology',
    description: 'It\'s just schoology.',
    function1: () => {
      const school = `
      <iframe src="https://stratfordschools.schoology.com" frameborder="0" style="width: 100%; height: 100%; border: none; margin: none;"></iframe>
    `
      const schoology = {
        id: 9,
        imageSrc: '/media/icons/schoology.png',
        text: 'Schoology',
        clickFunction: function() {
          createWindow('Schoology', schoology, '60%', '70%');
        }
      };
      createApp(schoology);
      console.log('Successfully installed the app "Schoology" with the ID of "9".');
    },
    function2: () => {
      removeAppById(9);
      console.log('Successfully uninstalled the app "Schoology" with the ID of "9".');
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
