# Function names
Function names should say what they are precisely doing and 
should indicate what is returned

# Bad
```python
class Validation:

    def handle(self, val, max):
    
        if val < max:
            return False
            
validator = Validation()

# What does handle do?
validator.handle(5, 6)

```

# Good
```python
class Validation:

    def is_valid(self, val, max):
    
        if val < max:
            return False

validator = Validation()
validator.is_valid(5, 6)

```

