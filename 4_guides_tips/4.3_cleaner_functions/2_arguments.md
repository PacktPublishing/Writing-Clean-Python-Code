# Functions arguments - Keep them to two or less

# Bad
```python
def create_page(title, meta, body, footer, menu):
    # ...
```

# Good

```python
Class Page:
    def __init__(self, config: dict):
        title = config["title"]
        meta = config["meta"]
        body = config["body"]
        footer = config["footer"]
        menu = config["menu"]

page = Page(
    {
        "title": "This is the page title",
        "meta": "Dummy page",
        "body": "Page body",
        "footer": "List of links",
        "menu": "Menu items"
    }
)
    
```

# Better
```python
class PageConfig:
    title: str
    meta: str
    body: str
    footer: str
    menu: str


def create_page(config: PageConfig):
    title = config.title
    meta = config.meta
    body: config.body
    footer: config.footer
    menu: config.meu

config = PageConfig
config.title = "This is the page title"
config.meta = "Dummy pageu"
config.body = "Page body"
config.footer = "List of links"
config.menu = "Menu items"

create_page(config)
```