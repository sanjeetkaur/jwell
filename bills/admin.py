from django.contrib import admin
from bills.models import expenses, Choice
# Register your models here.
#inlines = [ChoiceInline]



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5
    list_display = ['carat', 'item', 'weight', 'labour_cost']


class expensesAdmin(admin.ModelAdmin):
    fields =  ['purchase_order_no', 'rate_of_pure', 'customer_id']
#    list_display = ['carat', 'item', 'weight', 'cost', 'labour_cost']

    inlines = [ChoiceInline]



admin.site.register(expenses, expensesAdmin)
