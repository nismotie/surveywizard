from django.db import models
# Create your models here.
class MentorCall(models.Model):
    learner_name = models.CharField()
    learner_email = models.CharField()
    mentor_name = models.CharField()
    mentor_email = models.CharField()
    subject = models.CharField
    response = models.CharField()
