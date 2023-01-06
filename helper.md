#### Timer Decorator
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        print(func.__name__, *args, "begins ...")
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        t1 = time.perf_counter()
        print(func.__name__, *args, "complete!")
        print("time use:", round(t1 - t0), "seconds\n")
        return result
    return wrapper
```
