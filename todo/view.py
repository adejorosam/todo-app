todos = Task.objects.all() #quering all todos with the object manager
    num_todo = len(todos)
    # print(num_todo)
    categories = Category.objects.all()
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["title"]
            description = request.POST["description"] #description
            due_date = str(request.POST["due_date"]) #date
            category = request.POST["category_select"] #category
            Todo = Task(description = description, title=title, due_date=due_date, category=Category.objects.get(name=category))
            Todo.save() #saving the todo 
            return redirect("/") #reloading the page
        
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = Task.objects.get(id=int(todo_id)) #getting todo id
                print(todo)
                todo.delete() #deleting todo
                return redirect("/") #reloading the page

    return render(request, "index.html", {"todos": todos, "categories":categories, "num_todo":num_todo})
