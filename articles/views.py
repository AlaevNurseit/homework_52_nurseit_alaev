from django.http import HttpResponseRedirect
from django.shortcuts import render
from articles.models import ToDolist


def todolist_list(request):
    todolists = ToDolist.objects.all()
    context = {'todolists': todolists}
    return render(request, "index.html", context)


def todolist_detail(request):
    id = request.GET.get('id')
    if id:
        try:
            todolist = ToDolist.objects.get(id=int(id))
            context = {'todolist': todolist}
            return render(request, "todolist_view.html", context)
        except ToDolist.DoesNotExist:
            return HttpResponseRedirect("/todolist/")
    return HttpResponseRedirect("/todolist/")

def todolist_create(request):
    if request.method == 'GET':
        status_choices = ToDolist.STATUS_CHOICES
        return render(request, 'todolist_create.html', {'status_choices': status_choices})
    elif request.method == 'POST':
        ToDolist.objects.create(
            description=request.POST.get("description"),
            status=request.POST.get("status"),
            execution_date=request.POST.get("execution_date") or None,
        )
        return HttpResponseRedirect("/todolist/")