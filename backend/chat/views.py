# at chatapp/backend/chat/views.py

import json

from django.contrib.auth.decorators import login_required
from django.db.models import Max, Q
from django.shortcuts import render
from django.utils.safestring import mark_safe

from .models import Conversation


@login_required
def index(request):
    conv = Conversation.objects.filter(
        Q(user_one=request.user)
        | Q(user_two=request.user)
    )
    conv = conv.annotate(last_message_time=Max('messages__timestamp')).order_by('-last_message_time')
    return render(request, 'chat/index.html', {'conversations': conv})


@login_required
def room(request, room_name):
    conv = Conversation.objects.filter(
        Q(user_one=request.user)
        | Q(user_two=request.user)
    )
    conv = conv.annotate(last_message_time=Max('messages__timestamp')).order_by('-last_message_time')
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
        'conversations': conv
    })
