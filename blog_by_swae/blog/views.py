from django.shortcuts import render
from .models import Posts
from .forms import Create_form

# Create your views here.
def posts(request):
    obj = Posts.objects.all()
    return render(request,'templates/index.html',context = {'obj': obj})

def view_page_two(request):
    return render(request,'templates/<int:id>')

def new_post_upload(request):
    form = Create_form(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form':form
    }
    return render(request,'templates/createpost.html',context)

def post(request,id):
    obj = Posts.objects.get(id= id)
    return render(request,'templates/posts.html',{'obj':obj})
