from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Response)
admin.site.register(Test)
# admin.site.register(Right)