# Django

Question 1: By default, are Django signals executed synchronously or asynchronously?
Answer: By default, Django signals are executed synchronously. This means that the signal handler runs immediately in the same thread as the sender, before the code continues execution.

Code Snippet: We can prove this by logging the execution order of a signal handler and the sender.
# signals.py
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_signal(sender, instance, **kwargs):
    print("Signal handler starts")
    time.sleep(5)  # Simulate long running task
    print("Signal handler ends")

# In any view or script where we save a User instance
def create_user():
    print("Before saving user")
    user = User.objects.create(username='testuser', password='testpass')
    print("After saving user")

# Output
# Before saving user
# Signal handler starts
# Signal handler ends
# After saving user

Question 2: Do Django signals run in the same thread as the caller?
Answer: Yes, Django signals run in the same thread as the caller. This can be shown by inspecting the thread ID in both the signal handler and the main caller function.

Code Snippet:
# signals.py
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_signal(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.get_ident()}")

# In any view or script where we save a User instance
def create_user():
    print(f"Main function running in thread: {threading.get_ident()}")
    user = User.objects.create(username='testuser', password='testpass')

# Output (Thread ID values will be the same)
# Main function running in thread: 139953967470336
# Signal handler running in thread: 139953967470336

Question 3: By default, do Django signals run in the same database transaction as the caller?
Answer: Yes, by default Django signals run within the same database transaction. If an exception occurs in the signal handler, the entire transaction is rolled back.

Code Snippet:
# signals.py
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_signal(sender, instance, **kwargs):
    print("Signal handler starts")
    # Raise an exception to check if the transaction is rolled back
    raise Exception("Error in signal handler")

# In any view or script where we save a User instance
def create_user():
    try:
        with transaction.atomic():
            user = User.objects.create(username='testuser', password='testpass')
    except Exception as e:
        print(f"Transaction rolled back: {e}")

# Output
# Signal handler starts
# Transaction rolled back: Error in signal handler
