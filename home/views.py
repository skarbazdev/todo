from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title != " ":
            Todo.objects.create(title=title)
        
        return redirect('index')
    data = Todo.objects.all()
    context = {
            'data': data
        }
    return render(request, 'index.html', context = context)



def delview(request,id=None):
    dlt = Todo.objects.get(id=id)
    dlt.delete()
    return redirect('/')

# def editview(request,id):

#     edit = Todo.objects.get(pk=id)
#     # form = Todo(instance=edit)

#     return redirect('/')

def Complete(request, id=None):
    data = Todo.objects.get(id=id)
    data.complete = True
    data.save()
    return redirect('index')
    
def InComplete(request, id=None):
    data = Todo.objects.get(id=id)
    data.complete = False
    data.save()
    return redirect('index')