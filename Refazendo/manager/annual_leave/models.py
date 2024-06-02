from django.db import models
from manager.backend.models import Usuario

class AnnualLeave(models.Model): 
    employee = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    photo_of_the_day = models.ImageField(upload_to="photos/%d/%m/%Y/", null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    lunch_start = models.TimeField()
    lunch_end = models.TimeField()
    day_off = models.DateField()
    extra_hours = models.FloatField()

    def __str__(self):
        return self.employee

    def save(self, *args, **kwargs):
        self.extra_hours = self.end_time - self.start_time
        super(AnnualLeave, self).save(*args, **kwargs)