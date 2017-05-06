from django.db import models
from django.utils import timezone

class Task(models.Model):
    assignee = models.ForeignKey('auth.User')
    title = models.CharField(max_length=160)
    description = models.TextField()
    deadline = models.DateTimeField(
            default=timezone.now)
    created_date = models.DateTimeField(
        blank=True, null=True)
    progress = models.TextField()

    def create(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
