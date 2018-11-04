from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="New")
    text = models.TextField(default="Text")
    notes = models.TextField(default="Notes")
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False)
