from django.shortcuts import render
from django.contrib.auth.models import User,auth
from .models import Photos,UserGroup,Chat
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

   
    


# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from social.models import ProfilePicture,Upload




def signup(request):
    message=""
    if request.method=="POST":

        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        password1=request.POST["password1"]
        profilepictur=request.FILES["profilepicture"]
        
        if password!=password1:
            message="password incorrect"
            
        elif username=="" or email=="" or password=="" or password1=="":
            message="Field can not be blank"
            
        elif len(password)<8:
            message="password cant be less than 8"
            
            
            
        
        elif User.objects.filter(email=email).exists():
            message="email already present"
            return HttpResponseRedirect("/")  
            
          
        
        elif User.objects.filter(username=username).exists():
            message="username already present"
            return HttpResponseRedirect("/") 
        
            
        
        else:
            
            print(f'{username}')
            # user = auth.authenticate(request, username=username, password=password,email=email)
            # auth.login(request,user)
          
            userr=User.objects.create_user(email=email,password=password,username=username)
            userr.save()
            user = authenticate(username=username,password=password)
            login(request, user)
        
            
            k=User.objects.get(username=username)
            
            print(k)
            pp=Photos(photo=profilepictur,user=User.objects.get(username=username))
            
            pp.save()
            
            
            
            return HttpResponseRedirect(f"/{username}/user/")
            
            
            
          
    
    return render(request,"signup.html",{"message":message})


    
    
    
    
    
def signin(request):
    # message=""
    # if request.method=="POST":
        
    #     email=request.POST["email"]
    #     password=request.POST["password"]
    #     # user=auth.authenticate(email=email,password=password)
    #     # auth.login(request,user)
        
    #     if User.objects.filter(email=email).exists() and User.objects.filter(password=password).exists():
    #         k=User.objects.get(email=email)
    #         print(k.username)
    #         message="logedinn"
    #         return HttpResponseRedirect(f"/{k.username}/user/")
        

            
    #     else:
    #         message="unable to login"
    # message=""
    # if request.method=="POST":
    #     email=request.POST["email"]
    #     password=request.POST["password"]
    #     if User.objects.filter(email=email) and User.objects.filter(password=password):
    #         message="logedinn"
    #         return HttpResponseRedirect("/socialbook")
    #     else:
    #         message="unable to login"
    
    message="hello"
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        
        if user is not None:
            login(request, user)
            
            print("hello")
            print(request.user)
            message="able to login"
            return HttpResponseRedirect(f"/{username}/user/")
            # return HttpResponseRedirect("/homepage/")   
            
        else:
            message="not able"    
        
    
    return render(request,"signin.html",{"message":message})
        
        
    
     
    
    
    return render(request,"signin.html",{"message":message})
               
        
    
     
    
    
    return render(request,"signin.html",{"message":message})
    

    






# taeke image and the uploaded things from the user

# def uploaded(request):
   
    
    
#     return render(request,"socialbook.html")



# renering users

@login_required(login_url="signup")
def users(request,username):
  
    photo=[]

# other userid

    m=User.objects.get(username=username)
    print(m)
    
 
    k=Photos.objects.get(user=m)

    print(k.id)
    
    
    print("USer id is ",k.id)
    
    users=User.objects.all()
    
    photo=Photos.objects.exclude(user=m)
    
    
    
    print("User name is ",k)
    l=Photos.objects.all()
    print(l)
    
    
    photo=Photos.objects.all()
        
    
    
    
    
    
    
    
    
    return render(request,"users.html",{"username":m,"photos":photo,"userid":k.id,})



# we got two argument in message username and id

def message(request,username,id):
    
    
    
    return render(request,"message.html")


# here usersid is the id of auhtenticated person

def chat(request,userid,usersid,username):
    chats=[]
    users=request.user
    
    print(users)
    print("id of the authenticated person",usersid)
    
    
    print("Username is ",username)
    print("user id is ",userid)
    # logged in user 
   
    
    m=User.objects.get(username=username)
    # remove logged in user
    photo=Photos.objects.exclude(user=m)

    
    if (userid<usersid):
        groupname=f'{userid}_{usersid}'
        senduserid=usersid
        print(groupname)
        
    else:
        groupname=f'{usersid}_{userid}'
        senduserid=usersid
        print(groupname)
    
    if UserGroup.objects.filter(usergroupname=groupname).exists():
        k=UserGroup.objects.filter(usergroupname=groupname).first()
        chats=Chat.objects.filter(groupname=k)
        print(chats)
       
        
    
    else:
        UserGroup(usergroupname=groupname).save()
        
    
    
    
    return render(request,"chat.html",{"photo":photo,"usersid":usersid,"groupname":groupname,"chat":chats,"username":username})



def cssfortheusers(request):
    
    photo=Photos.objects.all()
    print(photo)
    
    
    
    return render(request,"cssfortheusers.html",{"photo":photo})
