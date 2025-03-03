## Connection through Credentials
```python
import getpass
import platform
import configparser as cp

def parse_server_config(profile):
    user = getpass.getuser()
    if platform.system() == 'Linux':
        config_file = f'/home/{user}/.../con.ini'
        conf = cp.ConfigParser()
        conf.read(config_file)
        config_params = conf._sections[profile]
    elif platform.system() == 'Windows':
        config_params = dict(
            account=...,
            user=user,
            authenticator='externalbrowser',    # authenticate with OKTA
            warehouse=...,
            role=...,
    )
    return config_params
```

## Set HTTP Proxy
```python
import os

def set_http_proxy():
    """
    alternatively, setup in bash shell
    $ nano ~/.bashrc
        export HTTP_PROXY='...'
        export HTTPS_PROXY='...'
    $ source ~/.bashrc
    """
    if ... in os.uname().nodename:      # depends on machine
        proxy = '...'
        if not os.environ.get('HTTP_PROXY'):
            os.environ['HTTP_PROXY'] = proxy
        if not os.environ.get('HTTPS_PROXY'):
            os.environ['HTTPS_PROXY'] = proxy
    return
```

## Snowflake
```python
import warnings
warnings.filterwarnings("ignore", ".*supports_statement_chache*")

import snowflake.connector
snowflake.connector.paramstyle = u'pyformat'
from snowflake.sqlalchemy import URL
from sqlalchemy import create engine

def connect_to_snowflake(profile, database=None, schema=None):
    params = parse_server_config(profile='snowflake')
    params.update(dict(database=database, schema=schema))
    connection = snowflake.connector.connect(**params)
    return connection

def query_snowflake(sql_scripts, database, schema, results=True):
    con = connect_to_snowflake(database=database, schema=schema)
    try:
        cur = con.cursor()
        cur.execute(sql_scripts)
        if results:
            df_res = cur.fetch_pandas_all()
            df_res.columns = [c.lower() for c in df_res.columns]
            return df_res
    except Exception as e:
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        print('-' * 50, '>' * 3, 'Query Failed!')
    finally:
        cur.close()
        con.close()

#TODO: return rowcount
def execute_in_snowflake(sql_scripts, database, schema):
    query_snowflake(
        sql_scripts,
        database=database,
        schema=schema,
        results=False
    )
    return
```


## Hive
```python
import pyhs2 as hive

def connect_to_hive(database=None, username=None, password=None, **kwargs):
    params = parse_server_config(profile='hive')    # host, port, user, password, authMechanism='LDAP'
    params.update(database=database)
    connection = hive.connect(**params)
    return connection
```

## SQL Server
```python
import pyodbc

def connect_to_mssql(database, schema, **kwargs):
    params = parse_server_config(profile='mssql')    # host, port, user, password, authMechanism='LDAP'
    driver = ('/opt/microsoft/msodbcsql/lib64/libmsodbcsql-version#')
    engine = f"driver={driver};server={host};port={port};database={database};uid={username};pwd={password}"
    connection = pyodbc.connect(driver, **kwargs)
    return connection
```

## MySQL
```python
import mysql.connector

def connect_to_mysql(database):
    params = parse_server_config(profile='mysql')    # host, user, password
    params.update(database=database)
    connection = mysql.connector.connect(**params)
    return connection
```
