from django.contrib import admin
from django.contrib.auth.models import Group, User
from . import models


admin.site.register(models.Customer)


#Unregister 
admin.site.unregister(Group)
#Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    #Just display username fields on admin page
    fields = ['username']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
