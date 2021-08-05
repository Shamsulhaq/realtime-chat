# at chatapp/backend/chat/apps.py
from django.apps import AppConfig


class ChatConfig(AppConfig):
    name = 'backend.chat'
    label = "users"
    verbose_name = "Users"
