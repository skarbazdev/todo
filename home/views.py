from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


    # def index(request):
#     if request.method == 'POST':
#         data = request.POST['data']

#         if data != "":
#             Todo.objects.create(data=data)
#         return redirect('index')
#         # all_data = Todo(data=data)
#         # all_data.save()

#     todos = Todo.objects.all()
    
        
#     return render(request,'index.html',{'todos':todos}) 

# def delview(request,id=None):
#     dlt = Todo.objects.get(id=id)
#     dlt.delete()
#     return redirect('/')

# # def editview(request,id):

# #     edit = Todo.objects.get(pk=id)
# #     # form = Todo(instance=edit)

# #     return redirect('/')

# def Complete(request, id=None):
#     data = Todo.objects.get(id=id)
#     data.complete = True
#     data.save()
#     return redirect('index')
    
# def InComplete(request, id=None):
#     data = Todo.objects.get(id=id)
#     data.complete = False
#     data.save()
#     return redirect('index')