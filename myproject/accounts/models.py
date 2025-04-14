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

class DentalRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='dental_records')
    record_date = models.DateField()
    dental_center = models.CharField(max_length=255)
    reason = models.TextField()
    investigations = models.TextField()
    outcome = models.TextField()

    def __str__(self):
        return f"Dental Record for {self.child.first_name} on {self.record_date}"

class Medication(models.Model):
    group = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')])
    patient_name = models.ForeignKey(Child, on_delete=models.CASCADE)
    prescribed_by = models.CharField(max_length=100)
    medicine_name = models.CharField(max_length=100)
    strength = models.CharField(max_length=50)
    mg_per_kg_per_day = models.CharField(max_length=50)
    dose = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    dwm = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.patient_name} - {self.medicine_name}"

class Illness(models.Model):
    group = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')])
    patient_name = models.ForeignKey(Child, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    treatment = models.CharField(max_length=255)
    date_logged = models.DateField()

    def __str__(self):
        return f"{self.patient_name} - {self.reason}"
