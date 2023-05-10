from django.db import models

class Task(models.Model):
    title_task = models.CharField(max_length=150)
    complete_task = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title_task
    