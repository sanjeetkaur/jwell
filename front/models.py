from django.db import models
# Create yourodels here.


class category(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(null = True)
    metal = models.CharField(max_length=10)
    mode_of_payment = models.CharField(max_length=15)
    telephone = models.IntegerField(max_length=10)
    address = models.CharField(max_length=75)
    customer_id = models.IntegerField(max_length=4)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return unicode(self.name)
