from django.db import models

# Create your models here.
class Application(models.Model):
    
    GENDER_CHOICES =(
        ('M', 'MALE'),
        ('F', 'FEMALE')
    )
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    
    def __str__(self):
        return self.email, self.first_name
    class Meta:
        db_table = 'Applications'