from django.db import models
import datetime
from category.models import Category
# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    assign_date=models.DateField(default=datetime.date.today)
    is_complete=models.BooleanField(default=False)
    category=models.ManyToManyField(Category)
    
    def __str__(self) -> str:
        return self.title