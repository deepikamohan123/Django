from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_signal(sender, instance, **kwargs):
    print("Signal handler starts")
    # Raise an exception to check if the transaction is rolled back
    raise Exception("Error in signal handler")

def create_user():
    try:
        with transaction.atomic():
            user = User.objects.create(username='testuser', password='testpass')
    except Exception as e:
        print(f"Transaction rolled back: {e}")

