from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth import login,logout,authenticate
from django.utils.decorators import method_decorator

from app.models import User
from app.models import Blog

from app.forms import Registration_From
from app.forms import Blog_Form
from app.forms import Login_Form


# Create your views here.


def Login_Dec(fn):   #  decorator for user must login

    def wrapper(request,**kwargs):

        if not request.user.is_authenticated:

            return redirect ('log')
        
        else:

            return fn(request,**kwargs)
        
    return wrapper


def Owner_only(fn):                 #  decorator for perform delete and update must be the real owner

    def wrapper(request,**kwargs):

        id=kwargs.get('pk')

        form=Blog.objects.get(id=id)

        if form.user!=request.user:

            return redirect('log')
        
        else:

            return fn(request,**kwargs)
        
    return wrapper



class Home_View(View):                      #  for home page

    def get(self,request):

        return render(request,'index.html')
    
    
class Registration_View(View):              #  for Registration page

    def get(self,request,*args,**kwargs):

        form=Registration_From()

        return render(request,'registration.html',{'form':form})
    
    def post(self,request,*args,**kwargs):

        form=Registration_From(request.POST)

        if form.is_valid():

            User.objects.create_user(**form.cleaned_data)

            return redirect('log')
        
        else:

            return redirect('reg')
        

class Login_View(View):                 #  for login page

    def get(self,request,*args,**kwargs):

        form=Login_Form()

        return render(request,'login.html',{'form':form})
    
    def post(self,request,*args,**kwargs):

        form=Login_Form(request.POST)

        if form.is_valid():

            name=form.cleaned_data.get('username')

            pwd=form.cleaned_data.get('password')

            obj=authenticate(username=name,password=pwd)

            if obj:
                
                login(request,obj)

                return redirect('all_blog')
            
            else:

                return redirect('log')
            

class Logout_View(View):                    #  for logout

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect('home')


@method_decorator(Login_Dec,name='dispatch')                 #  for see all the blogs

class Blog_View(View):

    def get(self,request,*args,**kwargs):

        data=Blog.objects.all().order_by('-id')
        
        return render(request,'all_blog.html',{'data':data})


@method_decorator(Login_Dec,name='dispatch')

class Create_Blog_View(View):                            #  for create a new blog

    def get(self,request,*args,**kwargs):

        form=Blog_Form()

        data = Blog.objects.filter(user=request.user).order_by('-id')

        return render(request,'blog.html',{'form':form,'data':data})
    
    def post(self,request,*args,**kwargs):

        form=Blog_Form(request.POST)

        if form.is_valid():

            Blog.objects.create(**form.cleaned_data,user=request.user)

            data = Blog.objects.filter(user=request.user).order_by('-id')

            form=Blog_Form()

            return render(request,'blog.html',{'form':form,'data':data})
        
        else:

            return redirect('blog')


@method_decorator(Owner_only,name='dispatch')

@method_decorator(Login_Dec,name='dispatch')

class Single_Blog_View(View):                        #  for view a single blog

    def get(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        data=Blog.objects.get(id=id)

        return render(request,"single_blog.html",{'data':data})
    
    
@method_decorator(Owner_only,name='dispatch')

@method_decorator(Login_Dec,name='dispatch')

class Delete_blog_View(View):                    #  for delete a blog

    def get(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        Blog.objects.get(id=id).delete()

        data = Blog.objects.filter(user=request.user).order_by('-id')

        form=Blog_Form()

        return render(request,'blog.html',{'form':form,'data':data})
    

@method_decorator(Owner_only,name='dispatch')

@method_decorator(Login_Dec,name='dispatch')

class Update_Diary_View(View):                   #  for update a blog

    def get(self,request,**kwargs):

        id=kwargs.get('pk')

        data=Blog.objects.get(id=id)
        
        form=Blog_Form(instance=data)

        data = Blog.objects.filter(user=request.user).order_by('-id')

        return render(request,'blog.html',{'form':form,'data':data})
    
    def post(self,request,**kwargs):

        id=kwargs.get('pk')

        data=Blog.objects.get(id=id)

        form=Blog_Form(request.POST,instance=data)

        if form.is_valid():

            form.save()

            form=Blog_Form()

            data = Blog.objects.filter(user=request.user).order_by('-id')

            return render(request,'blog.html',{'form':form,'data':data})
        
        else:
            
            return redirect('blog')




