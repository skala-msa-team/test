const API_URL = "http://127.0.0.1:8000/api/tasks";
const EMPTY_MESSAGE = "표시할 할 일이 없습니다.";

const form = document.querySelector("#task-form");
const titleInput = document.querySelector("#task-title");
const formMessage = document.querySelector("#form-message");
const filterSelect = document.querySelector("#task-filter");
const taskList = document.querySelector("#task-list");
const emptyMessage = document.querySelector("#empty-message");

async function request(url, options = {}) {
  const response = await fetch(url, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  const body = await response.json();
  if (!response.ok) throw new Error(body.message || "요청에 실패했습니다.");
  return body;
}

function renderTasks(tasks) {
  taskList.replaceChildren();
  emptyMessage.textContent = EMPTY_MESSAGE;
  emptyMessage.hidden = tasks.length > 0;

  tasks.forEach((task) => {
    const item = document.createElement("li");
    item.className = "task-item";

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.completed;
    checkbox.setAttribute("aria-label", `${task.title} 완료 상태`);
    checkbox.addEventListener("change", () => updateTask(task.id, checkbox.checked));

    const title = document.createElement("span");
    title.textContent = task.title;
    if (task.completed) title.classList.add("completed");

    item.append(checkbox, title);
    taskList.append(item);
  });
}

async function loadTasks() {
  try {
    const status = filterSelect.value;
    const { tasks } = await request(`${API_URL}?status=${status}`);
    renderTasks(tasks);
  } catch (error) {
    formMessage.textContent = error.message;
  }
}

async function updateTask(taskId, completed) {
  await request(`${API_URL}/${taskId}`, {
    method: "PATCH",
    body: JSON.stringify({ completed }),
  });
  await loadTasks();
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  formMessage.textContent = "";

  try {
    await request(API_URL, {
      method: "POST",
      body: JSON.stringify({ title: titleInput.value }),
    });
    titleInput.value = "";
    await loadTasks();
  } catch (error) {
    formMessage.textContent = error.message;
  }
});

filterSelect.addEventListener("change", loadTasks);
loadTasks();

