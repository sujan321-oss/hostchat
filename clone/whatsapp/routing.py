from django.urls import path
from whatsapp import consumer
from .consumer import MySyncConsumer



websocket_urlspatterns=[
    
    path("ws/sc/<str:groupname>/",consumer.MySyncConsumer.as_asgi())
]