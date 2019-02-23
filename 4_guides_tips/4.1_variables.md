# Meaningful variable names

# Bad

```python
import datetime

n = datetime.date.today().strftime("%y-%m-%d")
```

# Good
    
```python
import datetime

current_date = datetime.date.today().strftime("%y-%m-%d")
```
