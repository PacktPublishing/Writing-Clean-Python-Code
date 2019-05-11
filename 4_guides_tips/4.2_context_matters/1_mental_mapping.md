# Avoid forcing the reader of the code to guess what the variable represents

# Bad
```python
items = ('Python', 'PHP', 'JavaScript')

for x in items:
    portfolio_update()
    resume_update() 
    # ...
    # Wait, what's `x` for again?
    do_somthing(x)
```    
  
# Good

```python
programming_languages = ('Python', 'PHP', 'JavaScript')

for language in programming_languages:
    portfolio_update()
    cv_update() 
    # ...
    do_somthing(language)
```