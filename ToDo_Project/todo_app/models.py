from django.db import models
from django.utils import timezone
# Create your models here.
class Todo(models.Model):
    Priorities = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    ]
    Categories= [
        ('Work','Work'),
        ('Personal','Personal'),
        ('Shopping','Shopping'),
        ('Health','Health'),
        ('Other','Other'),
    ]
    
    title = models.TextField(help_text="What's need to be done?")
    completed = models.BooleanField(default=False,help_text='Is this task finished?')    
    created_at = models.DateTimeField(auto_now_add=True,help_text="When was this task added?")
    updated_at = models.DateTimeField(auto_now=True,help_text="When was this last changed?")
    due_date = models.DateField(null=True,help_text="When does this need to be done?")
    priority = models.CharField(max_length=100,choices=Priorities,default='Medium')
    category = models.CharField(max_length=100,choices=Categories,null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Todo Task'
        verbose_name_plural = "Todo Tasks"
    def mark_complete(self):
        if not self.completed:
            self.completed = True
            self.updated_at = timezone.now()
            self.save()
            return True
        return False
    def mark_incomplete(self):
        if self.completed:
            self.completed = False
            self.updated_at= timezone.now()
            self.save()
            return True 
        return False
    def is_overdue(self):
        if self.due_date and not self.completed:
            if timezone.now().date() > self.due_date:
                return True
        return False