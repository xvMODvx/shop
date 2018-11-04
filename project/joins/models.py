from django.db import models


class Join(models.Model):
    email = models.EmailField(unique=True)
    friend = models.ForeignKey("self", related_name='referral', null=True,\
                                 blank=True, on_delete=models.CASCADE)
    ref_id = models.CharField(max_length=120, default="ABC", unique=True)
    ip_address = models.CharField(max_length=120, default="ABC")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % (self.email)

    class Meta:
        unique_together = ("email", "ref_id",)
