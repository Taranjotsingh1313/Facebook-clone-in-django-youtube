from django.shortcuts import render,redirect
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.models import User
'''Showing Posts here'''
def index(request):
    return render(request,"myfaceapp/index.html")
   
'''Updating Profile View'''
def profile_upload(request):
    return render(request,"myfaceapp/profile-upload.html")

'''Showing Profile '''
def profile(request):
    return render(request,"myfaceapp/profile.html")

'''Sign Up And Redirecting to profile page '''
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        a = User.objects.create_user(username,email,password)
        a.first_name = fname
        a.last_name = lname
        a.save()
        if a:
           user = authenticate(username=username,password=password)
           if user is not None:
               login(request,user)
               return redirect('profile')
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

''' For Uploading Post'''
def uploadpost(request):
    return render(request,'myfaceapp/upload-post.html') 