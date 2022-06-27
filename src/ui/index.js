// const position = { x: 0, y: 0 };

// interact(".draggable").draggable({
//   listeners: {
//     start(event) {
//       console.log(event.type, event.target);
//     },
//     move(event) {
//       position.x += event.dx;
//       position.y += event.dy;

//       event.target.style.transform = `translate(${position.x}px, ${position.y}px)`;
//     },
//   },
// });

// Sortable.create(simpleList, {
//   store: {
//     /**
//      * Get the order of elements. Called once during initialization.
//      * @param   {Sortable}  sortable
//      * @returns {Array}
//      */
//     get: function (sortable) {
//       var order = localStorage.getItem(sortable.options.group.name);
//       return order ? order.split("|") : [];
//     },

//     /**
//      * Save the order of elements. Called onEnd (when the item is dropped).
//      * @param {Sortable}  sortable
//      */
//     set: function (sortable) {
//       var order = sortable.toArray();
//       localStorage.setItem(sortable.options.group.name, order.join("|"));
//     },
//   },
// });

var input = document.getElementById("newCategory");
var button = document.getElementById("saveCategory");

// This event is fired when button is clicked
button.addEventListener("click", function () {
  console.log("button clicked!");
});

input.addEventListener("keyup", function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    button.click();
  }
});

const newTask = document.getElementById("newTask");
const taskTitle = document.getElementById("taskTitle");
const taskDesc = document.getElementById("taskDesc");

const insertData = (newTask) => {
  fetch("http://localhost:5000/api/addtask", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(newTask),
  })
    .then((resp) => resp.json())
    .then((data) => {
      console.log(data);
    })
    .catch((error) => console.log(error));
};

const getAllTask = (tasks) => {
  fetch("http://localhost:5000/api/tasks", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((resp) => resp.json())
    .then((data) => {
      loadTask(data);
    })
    .catch((error) => console.log(error));
};

const getAllCategory = (categories) => {
  fetch("http://localhost:5000/api/categories", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((resp) => resp.json())
    .then((data) => {
      console.log(data);
    })
    .catch((error) => console.log(error));
};

newTask.addEventListener("submit", (e) => {
  e.preventDefault();

  const newData = {
    title: taskTitle.value,
    desc: taskDesc.value,
    status: 0,
    priority: "Normal",
    category_id: 1,
  };
  insertData(newData);
  newTask.reset();
  // console.log(newData);
});

getAllCategory();
getAllTask();
function loadTask(mytasks) {
  tasks.innerHTML = "";
  mytasks.forEach((data) => {
    tasks.innerHTML += `
    <div id="accordion" class="card mt-2">
    <div class="card-header">
        <div class="row">
            <div class="col-md-11">
                <h5 class="mb-0">${data.title}</h5>
            </div>
            <div class="col-md-1">
                <span class="mb-0"><i class="fa fa-star"></i></span>
            </div>
        </div>
    </div>
    <div id="task1" class="card-body collapse">
        <div class="row">
            <p class="card-text">${data.desc}</p>
            <button class="col btn btn-secondary">ویرایش</button>
        </div>

    </div>
</div>
  `;
  });
}

$(function () {
  $("#accordion").accordion();
});
