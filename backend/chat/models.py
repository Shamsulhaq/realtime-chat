# at chatapp/backend/chat/models.py

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Conversation(models.Model):
    user_one = models.ForeignKey(
        User,
        related_name='participent',
        on_delete=models.CASCADE
    )
    user_two = models.ForeignKey(
        User,
        related_name='participent_two',
        on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ['user_one', 'user_two']

    def __str__(self):
        return str(self.id)

    def last_message(self):
        return self.messages.all().last()

    def conversation_url(self):
        return reverse("chats:room", kwargs={"room_name": self.pk})


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        related_name='messages',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        related_name='sender',
        on_delete=models.CASCADE
    )
    content = models.TextField()
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.content
