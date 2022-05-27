from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.user.username
class Dweet(models.Model):
    user = models.ForeignKey(
        User, related_name="dweets", on_delete=models.DO_NOTHING
        )
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"{self.created_at:%Y-%m-%d %H:%M}: "
            f"{self.body[:30]}..."
        )

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()

class Quote(models.Model):
    invoice_no = models.CharField(max_length=16, default="")
    user = models.ForeignKey(User, related_name="quotes", on_delete=models.DO_NOTHING)
    # organisation = models.ForeignKey("Organisation", on_delete=models.CASCADE, related_name="quotes", blank=True, null=True)
    school_name = models.CharField(max_length=256)
    to_name = models.CharField(max_length=256)
    school_address = models.CharField(max_length=2048)
    school_country = models.CharField(max_length=256)
    to_email = models.EmailField()
    school_size = models.IntegerField()
    price_per_student = models.IntegerField()
    discount = models.IntegerField()
    total = models.IntegerField()
    date = models.DateField()
    currency = models.CharField(max_length=3)
    bank_detail = models.CharField(max_length=2048, blank=True)
    pdf_file = models.FileField(null=True, blank=True)
    # Optional Fields
    special_comments = models.CharField(max_length=2048, blank=True, null=True)

    def __str__(self):
        return (
            f"{self.invoice_no} "
            f"{self.pdf_file} "
            f"{self.school_name} "

        )
