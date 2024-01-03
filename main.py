from flask import Flask, render_template, request, redirect, url_for
import requests
app = Flask(__name__)
tasks = []

@app.route('/')
def main():
    return render_template('index.html',tasks=tasks)
@app.route('/add_task', methods=['POST'])
def add_task():
    new_element = request.form['task']
    tasks.append(new_element)
    print(tasks)
    return redirect(url_for('main'))
@app.route('/delete_task/<int:task_id>',methods=['GET'])
def delete_task(task_id):
    if task_id<len(tasks):
        del tasks[task_id]
    return redirect(url_for('main'))
if __name__ == "__main__":
    app.run()