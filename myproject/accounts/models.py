from django.db import models

class Child(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    current_age = models.IntegerField()
    date_of_admission = models.DateField()
    age_of_admission = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
