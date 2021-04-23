from django.shortcuts import render

'''Showing Posts here'''
def index(request):
    return render(request,"myfaceapp/index.html",{'post':post})
   
'''Updating Profile View'''
def profile_upload(request):
    return render(request,"myfaceapp/profile-upload.html",{})

'''Showing Profile '''
def profile(request):
    if not request.user.is_authenticated:
        return redirect("signup")
    else:
        if profilemodel.objects.get(user=request.user) == None:
           return redirect("signup")
        pr = profilemodel.objects.get(user=request.user)
        poscount = Post.objects.filter(user=request.user).count()
        if poscount == 0:
            pos = ""
        else:
            pos = Post.objects.filter(user=request.user)
        postsnumber =  Post.objects.filter(user=request.user).count()
        followers = pr.followers.count()
        following = pr.following.count()
        context = {'pr':pr,'post':pos,"followers":followers,'following':following,'postnumber':postsnumber}
    return render(request,"myfaceapp/profile.html",context)

'''Sign Up And Redirecting to the signup page '''
def signup(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        email = data['email']
        first = data['firstname']
        lastname = data['lastname']
        password = data['password']
        check = User.objects.filter(username=username)
        if check:
            messages.warning(request,"Username Already Exists")
            return redirect("signup")
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.first_name = first
            user.last_name = lastname
            if user.save():
                a = authenticate(username=username,password=password)
                if a is not none:
                    login(request,a)
                    return redirect("profileupload")

           
    return render(request,'myfaceapp/sign.html',{})
''' login And Redirecting to the post'''
def login1(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("profile")
        else:
            messages.warning(request,'''You Don't Have Any Account Please Sign Up''')
            return redirect("signup")
    else:
        return redirect("signup")

'''for showing posts'''
def uploadpost(request):
    if not request.user.is_authenticated:
        return redirect("signup")
    else:
        if request.method == 'POST':
            data = request.POST
            postdesc = data['desc']
            postimage = request.FILES['file']
            # Saving Post In Database
            pr = profilemodel.objects.get(user=request.user)
            postsave = Post(post=postimage,profileuser=pr,user=request.user)
            # Saving Post Model Which We Have TO Do
            postsave.save()
            return redirect(profile)
    return render(request,"myfaceapp/upload-post.html",{})

'''For logout'''
def logout1(request):
    logout(request)
    return redirect("signup")
    
'''Search '''
def search(request):
    searchname = request.GET.get('search1')
    a = profilemodel.objects.filter(user__username=searchname)
    return render(request,'myfaceapp/search.html',{'pr':a})

'''Following user here'''
def follow_user(request):
    if request.method == 'POST':
        user_to_follow = request.POST['user']
        follow = profilemodel.objects.get(user__username=user_to_follow)
        following = profilemodel.objects.get(user__username=request.user)
        follow.followers.add(request.user)
        user_following = User.objects.get(username=user_to_follow)
        following.following.add(user_following)
        return JsonResponse({'follow': "Tui"})
    return redirect("search")