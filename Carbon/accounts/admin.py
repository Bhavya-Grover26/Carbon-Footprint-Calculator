from django.contrib import admin
from .models import User,Calculate,Individual,Organisation
# Register your models here.

admin.site.register(User)
admin.site.register(Calculate)
admin.site.register(Individual)
admin.site.register(Organisation)


