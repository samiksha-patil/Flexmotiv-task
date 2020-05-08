from django.shortcuts import render,redirect
from django.forms import modelformset_factory
from .forms import PicForm,PostForm
from .models import Pic,Post
# Create your views here.

def display_post(request):
    posts = Post.objects.all()
    context={
        'posts':posts
        }
    return render(request,'post/display.html',context)


def upload_image(request):
    if request.method=='POST':
        form1=PicForm(request.POST, request.FILES)
        form2=PostForm(request.POST)
        print(form1)
        if form1.is_valid() and form2.is_valid():
            print('hi')
            form1.save()             
            form2.instance.uploaded_by=request.user
            id =Pic.objects.filter(image=str(form1.instance))
            form2.save()
            form2.instance.image.set(id)
            form2.save()
            return redirect('')

    else:
        form1 = PicForm()
        form2= PostForm()
    return render(request,'post/upload_image.html',{
        
        'form1':form1,
        'form2':form2
        })
       