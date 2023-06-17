from application import app
from flask import render_template,request,redirect,flash
from .forms import ToDoForm
from datetime import datetime
from application import db
from bson.objectid import ObjectId
from application import collection


@app.route("/")
def show():
    todos=[]
    for todo in collection.find().sort("datecreated",-1):
        todo["_id"]=str(todo["_id"])
        todo["date_created"]=todo["date_created"].strftime("%b %d %Y %H:%M:%S")
        todos.append(todo)

    return render_template("viewtodo.html" , title="home", todos=todos)

@app.route("/addtodo", methods = ['POST', 'GET'])
def addtodo():
    if request.method == "POST":
        form = ToDoForm(request.form)
        todo_name = form.task.data
        todo_description = form.description.data
        completed = form.completed.data

        collection.insert_one({
            "name": todo_name,
            "description": todo_description,
            "completed": completed,
            "date_created": datetime.utcnow()
        })
        flash("Todo successfully added", "success")
        return redirect("/")
    else:
        form = ToDoForm()
    return render_template("addtodo.html", form = form)

@app.route("/deletetodo/<id>")
def deletetodo(id):
    collection.find_one_and_delete({"_id": ObjectId(id)})
    flash("Todo successfully deleted", "success")
    return redirect("/")


@app.route("/updatetodo<id>", methods = ['POST', 'GET'])
def updatetodo(id):
    if request.method == "POST":
        form = ToDoForm(request.form)
        todo_name = form.task.data
        todo_description = form.description.data
        completed = form.completed.data

        collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
            "name": todo_name,
            "description": todo_description,
            "completed": completed,
            "date_created": datetime.utcnow()
        }})
        flash("Todo successfully updated", "success")
        return redirect("/")
    else:
        form = ToDoForm()

        todo = collection.find_one({"_id": ObjectId(id)})
        print(todo)
        form.task.data = todo.get("name", None)
        form.description.data = todo.get("description", None)
        form.completed.data = todo.get("completd", None)

    return render_template("addtodo.html", form = form)
