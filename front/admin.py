from django.contrib import admin
from front.models import category
# Register your models here.

#class ChoiceInline(admin.StackedInline):
#    model = Choice
#    extra = 3


#class mcategoryAdmin(admin.ModelAdmin):
#    fields = ['abc', 'efg']

 #   inlines = [ChoiceInline]

admin.site.register(category)

