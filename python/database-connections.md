## Connection through Credentials
```python
import getpass
import configparser as cp

def parse_server_config(profile):

    user = getpass.getuser()
    config_file = ...    # .../con.ini
    conf = cp.ConfigParser()
    conf.read(config_file)
    config_params = conf._sections[profile]

    return config_params
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

