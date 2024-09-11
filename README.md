# Django

# Question 1:
By default, are Django signals executed synchronously or asynchronously?
Answer: By default, Django signals are executed synchronously. This means that the signal handler runs immediately in the same thread as the sender, before the code continues execution.

Code Snippet: We can prove this by logging the execution order of a signal handler and the sender.
# SyncOrAsync.py

# Output
 Before saving user
 Signal handler starts
 Signal handler ends
 After saving user

# Question 2: 
Do Django signals run in the same thread as the caller?
Answer: Yes, Django signals run in the same thread as the caller. This can be shown by inspecting the thread ID in both the signal handler and the main caller function.

Code Snippet:
# thread.py

# Output (Thread ID values will be the same)
 Main function running in thread: 139953967470336
 Signal handler running in thread: 139953967470336

# Question 3:
By default, do Django signals run in the same database transaction as the caller?
Answer: Yes, by default Django signals run within the same database transaction. If an exception occurs in the signal handler, the entire transaction is rolled back.

Code Snippet:
# database.py

# Output
 Signal handler starts
 Transaction rolled back: Error in signal handler
