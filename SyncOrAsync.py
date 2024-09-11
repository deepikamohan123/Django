import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_signal(sender, instance, **kwargs):
    print("Signal handler starts")
    time.sleep(5)  # Simulate long running task
    print("Signal handler ends")

def create_user():
    print("Before saving user")
    user = User.objects.create(username='testuser', password='testpass')
    print("After saving user")

