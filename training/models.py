# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models
from multiselectfield import MultiSelectField  # type: ignore

User = get_user_model()


class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    years_of_experience = models.PositiveIntegerField()
    description = models.TextField()
    total_rate = models.PositiveIntegerField()
    education = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to="training/images", null=True, blank=True
    )
    resume = models.FileField(
        upload_to="training/resumes", null=True, blank=True
    )

    def __str__(self):
        first_name = self.user.first_name.title()
        last_name = self.user.last_name.title()
        if first_name and last_name:
            return f"{first_name} {last_name}"
        else:
            return self.user.username.title()


class TrainingCourse(models.Model):
    DAYS_OF_WEEK_CHOICES = (
        ("mon", "Monday"),
        ("tue", "Tuesday"),
        ("wed", "Wednesday"),
        ("thu", "Thursday"),
        ("fri", "Friday"),
        ("sat", "Saturday"),
        ("sun", "Sunday"),
    )

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    total_rate = models.PositiveIntegerField()
    class_fee = models.FloatField()
    remined_capacity = models.PositiveIntegerField()
    class_time = models.TimeField()
    days_of_week = MultiSelectField(max_length=10, choices=DAYS_OF_WEEK_CHOICES)

    def __str__(self):
        return self.title


class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    traing_classes = models.ManyToManyField(TrainingCourse)

    def __str__(self):
        first_name = self.user.first_name.title()
        last_name = self.user.last_name.title()
        if first_name and last_name:
            return f"{first_name} {last_name}"
        else:
            return self.user.username.title()
