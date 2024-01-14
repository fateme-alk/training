# Register your models here.
from django.contrib import admin

from .models import Participant, Trainer, TrainingCourse

admin.site.register(Trainer)
admin.site.register(Participant)
admin.site.register(TrainingCourse)
