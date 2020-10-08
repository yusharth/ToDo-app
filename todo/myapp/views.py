from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
# Create your views here.
def todoview(request):
	all_todo_items=TodoItem.objects.all()
	return render(request,'myhtml.html',
		{'all_items':all_todo_items})

def addtodo(request):
	c = request.POST['content']
	new_item = TodoItem(content = c)
	new_item.save()
	return HttpResponseRedirect('/todo')
	#create a new todo item
	#saving the todo item
	#redireect to the /todo/

def deltodo(request,todo_id):
	item_to_delete=TodoItem.objects.get(id=todo_id)
	item_to_delete.delete()	
	return HttpResponseRedirect('/todo')
	