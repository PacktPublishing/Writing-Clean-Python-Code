# Avoid flags that redirect the process flow

# Bad
```python
from pathlib import Path

def create_log(filename: str, in_system: bool) -> None:
    if in_system:
        Path('/var/log/' + filename).touch()
    else:
        Path(filename).touch()

```

# Good

```python
from pathlib import Path

def create_log(filename: str) -> None:
    Path(filename).touch()

def create_system_log(filename: str) -> None:
    Path('/var/log/' + filename).touch()
```

