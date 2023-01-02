from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from whatsapp.models import Chat ,UserGroup
import json

from asgiref.sync import sync_to_async,async_to_sync


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("event is ",event)
        self.groupname=self.scope['url_route']['kwargs']['groupname']
        print("groupnmae is",self.groupname)
        async_to_sync(self.channel_layer.group_add)(self.groupname,self.channel_name)
        print("Current User is ")
        print("Name of the channel layer is ")
        print("Websocket connected<<")
        self.send({
            "type":"websocket.accept"
        }
        )
        
        
        
        
    def websocket_receive(self,event):
        print("Message received")
        print("message revceived from client side",event['text'])
        print("event in message received",event)
        l=json.loads(event['text'])
        print("After loading the message now messsage is ",l)
        print("actual message is",l['message'])
        print("Username is ",l['username'])
        
        
        k=UserGroup.objects.get(usergroupname=self.groupname)
        print("Group name is ",k)
        
  
        chat=Chat(chatcontent=l['message'],groupname=k,username=l['username'])
        chat.save()
        
        # k=Group.objects.get(usergroupname=self.groupname)
        # take a group name form the database
        # k=Group.objects.filter()
        
        
        # chat=Chat(groupname=k,chatcontent=event['text']).save()
        print("Send message is ",event['text'])
        
        
        async_to_sync(self.channel_layer.group_send)(self.groupname,{"type":"message.send","message":l['message'],"username":l['username']})
        
    
    
    
    def message_send(self,event):
        
        self.send({
            "type":"websocket.send",
            "text":json.dumps({"message":event['message'],"username":event['username']})
        })
        
        
        
        
        
    
    def websocket_disconnect(self,event):
        async_to_sync(self.channel_layer.group_discard)(self.groupname,self.channel_name)
        print("Discard group is ",self.groupname)
        print("Websocket disconnected>>>>>")
        raise StopConsumer()
    
    