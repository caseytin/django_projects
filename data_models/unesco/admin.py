from django.contrib import admin

# Register your models here.

from unesco.models import Site, Category, States, Region, ISO

admin.site.register(Site)
admin.site.register(Category)
admin.site.register(States)
admin.site.register(Region)
admin.site.register(ISO)