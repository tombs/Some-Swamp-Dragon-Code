from django.db import models
from swampdragon.models import SelfPublishModel
from .serializers import NotificationSerializer


class Notification(SelfPublishModel, models.Model):
    serializer_class = NotificationSerializer
    message = models.TextField()
    status = models.CharField(max_length=255,default="new") # new, sent
    created = models.DateTimeField(auto_now_add=True)
