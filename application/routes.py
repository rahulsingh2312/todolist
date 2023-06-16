from application import app
from flask import render_template,request,redirect,flash
from .forms import ToDoForm
from datetime import datetime
from application import db
from application import collection


@app.route("/")
def show():
    todos=[]
    for todo in collection.find().sort("datecreated",-1):
        todo["_id"]=str(todo["_id"])
        todo["date_created"]=todo["date_created"].strftime("%b %d %Y #H:%M:%S")
        todos.append(todo)

    return render_template("viewtodo.html" , title="home", todos=todos)

@app.route("/updatetodo<id>", methods =['POST','GET'])
def updatetodo(id):
    todos=[]
    for todo in collection.find().sort("datecreated",-1):
        todo["_id"]=str(todo["_id"])
        todo["date_created"]=todo["date_created"].strftime("%b %d %Y #H:%M:%S")
        todos.append(todo)    
    if request.method == "POST":
        form = ToDoForm(request.form)
        todo_task = form.task.data
        todo_description = form.description.data
        completed = form.completed.data

        return redirect("/")
    else:
        form = ToDoForm()
    return render_template("addtodo.html", form = form , todos=todos)






@app.route("/addtodo", methods = ['POST', 'GET'])
def add_todo():
    todos=[]
    for todo in collection.find().sort("datecreated",-1):
        todo["_id"]=str(todo["_id"])
        todo["date_created"]=todo["date_created"].strftime("%b %d %Y #H:%M:%S")
        todos.append(todo)
    if request.method == "POST":
        form = ToDoForm(request.form)
        todo_task = form.task.data
        todo_description = form.description.data
        completed = form.completed.data

        collection.insert_one({
            "name": todo_task,
            "description": todo_description,
            "completed": completed,
            "date_created": datetime.utcnow()
        })
        flash("Todo successfully added", "success")
        return redirect("/")
    else:
        form = ToDoForm()
    return render_template("addtodo.html", form = form , todos=todos)