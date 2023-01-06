## Parallelize Function with List of Args
```python
import threading

def _parallelize(func, args, **kwargs):
    threads = []
    for arg in args:
        t = threading.Thread(
            target=func, name=arg, args=(arg, ), kwargs=kwargs
        )
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return
```
