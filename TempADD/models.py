from django.db import models

# Create your models here.
class Calculate(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    output = models.IntegerField(
        default=0,  # This value will be overwritten during save()
        editable=False,  # Hides this field in the admin interface.
    )
    def __str__(self):
        return f"self.num31,self.num2,self.output"

