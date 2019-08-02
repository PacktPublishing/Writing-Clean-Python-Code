# Don't mix contexts

# Bad
```python
class Order:
    username = ''
    last_logged_in = None
    total = 0
    items = []
    
    def __init__(self, username, last_logged_in, total, items):
        self.username = username
        self.last_logged_in = last_logged_in
        self.total = total
        self.items = items
```

# Good
```python
class Order:
    total = 0
    items = []
    
    def __init__(self, total, items):
        self.total = total
        self.items = items
    
class Customer:
    username = ''
    last_logged_in = None
    
    def __init__(self, username, last_logged_in):
        self.username = username
        self.last_logged_in = last_logged_in
        
class Ordered:
    customer = None
    order = None
    
    def __init__(self, order, customer):
        self.order = order
        self.customer = customer