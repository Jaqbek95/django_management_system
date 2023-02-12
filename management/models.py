from django.db import models
from authentication.models import User

class Customer(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):

    project_manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    id = models.IntegerField(primary_key=True, unique=True)
    description = models.TextField(max_length=200)

    STATUS =(
    ("DESIGN", "Design"),
    ("PRODUCTION", "Production"),
    ("ASSEMBLY", "Assembly"),
    ("MEASUREMENT", "Measurement"),
    ("FINISH", "Finish"),
)
    status = models.CharField(max_length=12, choices=STATUS, default="DESIGN")
    
    def __str__(self):
        return str(self.id)

