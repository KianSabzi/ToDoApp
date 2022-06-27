const {
  app,
  BrowserWindow,
  Menu,
  MenuItem,
  Notification,
} = require("electron");
var path = require("path");
const interact = require("interactjs");
const Sortable = require("sortablejs");
require("electron-reload")(__dirname);
require("nunjucks");

// const NOTIFICATION_TITLE = "Basic Notification";
// const NOTIFICATION_BODY = "Notification from the Main process";

// function showNotification() {
//   new Notification({
//     title: NOTIFICATION_TITLE,
//     body: NOTIFICATION_BODY,
//   }).show();
// }

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 990,
    height: 750,
    icon: "src/ui/assets/img/AppIcon.png",
    autoHideMenuBar: true,
    // frame: false,
  });

  mainWindow.loadFile("src/ui/index.html");
  mainWindow.webContents.openDevTools();

  let menu = Menu.buildFromTemplate([
    {
      label: "File",
      submenu: [
        { label: "AllTask" },
        {
          label: "Exit",
          click() {
            app.quit();
          },
        },
      ],
    },
    {
      label: "About",
    },
  ]);

  Menu.setApplicationMenu(menu);
}

app.whenReady().then(() => {
  createWindow(), showNotification();
  const ctxMenu = new Menu();
  ctxMenu.append(
    new MenuItem({
      label: "Hello from Task manager application",
      click: function () {
        console.log("contex menu clicked");
      },
    })
  );
  ctxMenu.append(
    new MenuItem({ role: "selectall" }),
    new MenuItem({ role: "inspect" })
  );
  mainWindow.webContents.on("context-menu", function (e, params) {
    ctxMenu.popup(mainWindow, params.x, params.y);
  });
});
