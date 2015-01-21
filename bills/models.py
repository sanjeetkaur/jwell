from django.db import models
from front.models import category
# Create your models here.

class expenses(models.Model):
#    name  = models.ForeignKey(category, unique=False, blank=True, null=True)
    purchase_order_no = models.IntegerField(max_length=3, primary_key=True)
    rate_of_pure = models.IntegerField(max_length=15)
    customer_id = models.ForeignKey(category)
    def __unicode__(self):
        return '%s' % (self.purchase_order_no)

class Choice(models.Model):
    name  = models.ForeignKey(expenses, unique=False, blank=True, null=True)
    carat = models.IntegerField(max_length=2)
    item = models.CharField(max_length=25)
    weight = models.FloatField(max_length=10)
#    cost = models.FloatField(max_length=25)
    labour_cost = models.IntegerField(max_length=10)

