from django.shortcuts import render,redirect
from .models import ToDo_app
from django.contrib import messages
# Create your views here.
def home(request):
    post = ToDo_app.objects.all()
    if request.method=='POST':
        #the ['content'] below is the name of the input type in HTML form
        content = request.POST['content']
        #this line of code below collects data from HTML form and saves it into the database
        Content= ToDo_app.objects.create(content=content)
        messages.success(request, 'list has been submitted')
    return render(request, 'home.html', {'post':post})


def delete(request, pk):
    deleted_task = ToDo_app.objects.get(id=pk)
    content = deleted_task.content  # Retrieve content associated with the deleted task
    if request.method == 'POST':
        deleted_task.delete()
        return redirect("/")
    return render(request, 'home.html', {'content': content})
