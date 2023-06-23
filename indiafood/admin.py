from django.contrib import admin

# Register your models here.
from .models import *
#from  .models import Food 
from import_export.admin import ImportExportModelAdmin

@admin.register(Food)

class FoodAdmin(ImportExportModelAdmin):
    pass

@admin.register(Details)

class DetailsAdmin(ImportExportModelAdmin):
    pass

@admin.register(Rating)

class RatingAdmin(ImportExportModelAdmin):
    pass


@admin.register(Location)

class LocationAdmin(ImportExportModelAdmin):
    pass


