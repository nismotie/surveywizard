from django.db import models
# Create your models here.

class Survey(models.Model):
    def __init__(self, questions):
        self.questions = questions
