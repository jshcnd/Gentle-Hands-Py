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

class GrowthRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    head_circumference = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    chest_circumference = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    teeth_upper = models.PositiveIntegerField(blank=True, null=True)
    teeth_lower = models.PositiveIntegerField(blank=True, null=True)
    date_recorded = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Growth Record for {self.child} at age {self.age}"

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

class Appointment(models.Model):
    patient_name = models.ForeignKey(Child, on_delete=models.CASCADE)
    medical_type = models.CharField(max_length=100, choices=[
        ('General Checkup', 'General Checkup'),
        ('Dental', 'Dental'),
        ('Pediatrics', 'Pediatrics'),
    ])
    appointment_date = models.DateField()
    hospital_name = models.CharField(max_length=255, blank=True, null=True)
    medic_name = models.CharField(max_length=255, blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient_name} - {self.medical_type}"

class Immunization(models.Model):
    group_name = models.CharField(max_length=100)
    patient_name = models.ForeignKey(Child, on_delete=models.CASCADE) 
    vaccine = models.CharField(max_length=100)
    dose_no = models.IntegerField()
    date_due = models.DateField()
    age_when_due = models.CharField(max_length=50)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient_name} - {self.vaccine}"
