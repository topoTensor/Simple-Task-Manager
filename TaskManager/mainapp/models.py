from django.db import models

# Create your models here.
class TaskModel(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=True)
    deadline_date = models.DateTimeField(null=True)
    importance = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"name : {self.name}, content : {self.content}"