# Don't repeat contexts

# Bad
```python
class Product:
    product_name
    product_title
    product_category
```

# Good
```python
class Product:
    name
    title
    category

```