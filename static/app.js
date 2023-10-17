// Function to fetch and display tasks
function fetchTasks() {
    fetch('/tasks')
        .then(response => response.json())
        .then(data => {
            const tasksList = document.getElementById('tasks');
            tasksList.innerHTML = '';

            data.forEach(task => {
                const listItem = document.createElement('li');
                listItem.innerHTML = `<input type="checkbox" ${task.completed ? 'checked' : ''}> ${task.title} (Due Date: ${task.due_date})`;
                tasksList.appendChild(listItem);
            });
        });
}

// Function to add a new task
function addTask() {
    const taskTitle = document.getElementById('task-title').value;
    const dueDate = document.getElementById('due-date').value;

    if (taskTitle && dueDate) {
        fetch('/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title: taskTitle, due_date: dueDate }),
        })
            .then(() => {
                document.getElementById('task-title').value = '';
                document.getElementById('due-date').value = '';
                fetchTasks();
            });
            print("done")
    }
}

fetchTasks();
