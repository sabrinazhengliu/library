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

## Run Files Parallelly or Sequentially
```python
import os
import subprocess

def run_file(filename, **kwargs):
    dict_func = dict(
        sql=run_sql_file,
        py=run_python_file,
    )
    filetype = filename.split(".")[-1]
    filefunc = dict_func[filetype]
    filefunc(filename, **kwargs)
    return

def run_sql_file(filename, **kwargs):
    sql_file = os.path.join(current_directory, "sql", filename)
    with open(sql_file, 'r') as f:
        qry = f.read().format(**kwargs)
    execute_sql(qry)
    return
    
def run_python_file(filename, **kwargs):
    program = f"/home/{uid}/miniconda3/bin/python"
    py_file = os.path.join(current_directory, "src", filename)
    if len(kwargs):
        kwargs = {k: v for k, v in kwargs.items() if len(v) <= 20}
        arg1 = ",".join(kwargs.keys())
        arg2 = ",".join(kwargs.values())
    command = f"{program} {py_file} {arg1} {arg2}"
    exit_code = subprocess.run(command, shell=True)
    return exit_code

def execute_scripts_parallel(files, **kwargs):
    threads = []
    for filename in files:
        t = threading.Thread(
            target=run_file, name=filename, args=(filename, ), kwargs=kwargs
        )
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return

def execute_scripts_sequential(files, **kwargs):
    lock = threading.Lock()
    for filename in files:
        with lock:
            run_file(filename, **kwargs)
    return
```
