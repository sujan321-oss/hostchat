from django.contrib import admin

from whatsapp.models import Photos,User,Chat,UserGroup

class ShowPhoto(admin.ModelAdmin):
    list_display=("photo","user")



admin.site.register(Photos,ShowPhoto)  


class ChatShow(admin.ModelAdmin):
    list_display=("chatcontent","groupname")

admin.site.register(Chat,ChatShow)  


class Groupnamesave(admin.ModelAdmin):
    list_display=("usergroupname",)  
      
admin.site.register(UserGroup,Groupnamesave)  
  




class UserPhoto(admin.ModelAdmin):
    list_display=("photo",)
 
      


     
    
    
    
    

