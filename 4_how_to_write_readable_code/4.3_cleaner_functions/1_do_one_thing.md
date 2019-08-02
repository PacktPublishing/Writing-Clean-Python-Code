# Functions should do one thing only

# Bad
```python
def email_newsletter(users):

    for user in users:
        if user.active:
            mailer.send(user)
```

# Good
Here we are separating the responsibility by creating a function 
that returns active users 

```python
def get_active_users(users):

    return [user for user in users if user.active]

def email_newsletter(users):
   for user in users:
        mailer.send(user)
    
""" Get only active users """    
recipients = get_active_users() 

""" Send a newsletter to each active user """
email_newsletter(recipients)

```

