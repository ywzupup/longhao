from django.contrib import admin
from .models import ConsultPost, IndustryColumn, MeasurePost

# Register your models here.
admin.site.register(ConsultPost)
admin.site.register(IndustryColumn)
admin.site.register(MeasurePost)
