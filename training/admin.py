# Register your models here.
from django.contrib import admin

from .models import Participant, Trainer

admin.site.register(Trainer)
admin.site.register(Participant)
