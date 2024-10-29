from django.db import models
import csv
from django.core.files.storage import default_storage
# Create your models here.

class Category(models.Model):
    """Model for representing Catagories."""
    name = models.CharField(max_length=50,unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
class FormulaTemplate(models.Model):
    """Model for storing the formula."""
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    variables = models.JSONField()
    weight = models.JSONField()
    
    def __str__(self):
        return self.name
