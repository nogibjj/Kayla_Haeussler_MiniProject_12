from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# In-memory task list
tasks = []

# HTML Template
template = """
<!doctype html>
<html>
    <body>
        <h1>To-Do List</h1>
        <form action="/add" method="post">
            <input type="text" name="task" placeholder="Enter a new task" required>
            <button type="submit">Add Task</button>
        </form>
        <h2>Tasks:</h2>
        <ul>
            {% for task in tasks %}
                <li>
                    {{ task }}
                    <form action="/delete" method="post" style="display:inline;">
                        <input type="hidden" name="task" value="{{ task }}">
                        <button type="submit">Delete</button>
                    </form>
                </li>
            {% endfor %}
        </ul>
    </body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(template, tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append(task)  # Add task to the list
    return redirect("/")  # Redirect to the home page


@app.route("/delete", methods=["POST"])
def delete_task():
    task = request.form.get("task")
    if task in tasks:
        tasks.remove(task)  # Remove task from the list
    return redirect("/")  # Redirect to the home page


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
