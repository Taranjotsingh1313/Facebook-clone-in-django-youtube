from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import profilemodel,Post
'''Showing Posts here'''
def index(request):
    if request.user.is_authenticated:
        post = Post.objects.filter(profileuser__followers=request.user)
        
        return render(request,"myfaceapp/index.html",{'post':post})
    else:
        return redirect("signup")
   
'''Updating Profile View'''
def profile_upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_bio = request.POST['bio']
            profile_pic = request.FILES['file']
            profile_upload = profilemodel.objects.create(image=profile_pic,bio=user_bio,user=request.user)
            if profile_upload:
                return redirect("profile")
            else:
                return HttpResponse("Error! Please Try Again Later")
        return render(request,"myfaceapp/profile-upload.html")
    else:
        return redirect("signup")

'''Showing Profile '''
def profile(request):
    if request.user.is_authenticated:
        profile = profilemodel.objects.get(user=request.user)
        posts = Post.objects.filter(profileuser=profile)
        print(posts)
        return render(request,"myfaceapp/profile.html",{'profile':profile,'posts':posts})
    else:
        return redirect("/signup")

'''Sign Up And Redirecting to profile page '''
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        if User.objects.filter(username=username).first():
            messages.warning(request,"Username already exists")
            return redirect("signup")
        else:
            a = User.objects.create_user(username,email,password)
            a.first_name = fname
            a.last_name = lname
            a.save()
            if a:
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('uploadprofile')
    return render(request,"myfaceapp/sign.html",{})

'''For logout'''
def logout1(request):
    logout(request)
    return redirect("signup")
    
'''Search '''
def search(request):
    
    return render(request,'myfaceapp/search.html')

'''Following user here'''
def follow_user(request):
    
    return redirect("search")
'''For logging Users'''
def login1(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.warning(request,"Username Doesn't exist")
            return redirect("signup")

''' For Uploading Post'''
def uploadpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            profile = profilemodel.objects.get(user=request.user)
            postdesc = request.POST['desc']
            file = request.FILES['file']
            posts = Post.objects.create(post=file,profileuser=profile,user=request.user)
        return render(request,'myfaceapp/upload-post.html')
    else:
        return redirect("signup")