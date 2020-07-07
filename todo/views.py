from django.shortcuts import render, redirect
from .models import Task,Category


def index(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    if request.method == "POST": #checking if the request method is a POST
        if "addTask" in request.POST: #checking if there is a request to add a todo
            title = request.POST["title"]
            description = request.POST["description"] #description
            due_date = str(request.POST["due_date"]) #date
            category = request.POST["category_select"] #category
            Todo = Task(description = description, title=title, due_date=due_date, category=Category.objects.get(name=category))
            print(Todo)
            Todo.save() #saving the todo 
            return redirect("/") #reloading the page

        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST.getlist('checkedbox') #checked todos to be deleted
            for task_id in checkedlist:
                todo = Task.objects.get(id=int(task_id)) #getting todo id
                todo.delete()#deleting todo
                return redirect("/") #reloading the page
    return render(request, "index.html", {'tasks':tasks, 'categories':categories})


