## Connection through Credentials
```python
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
def connect_to_snowflake(profile, database=None, schema=None):

    params = parse_server_config(profile)
    params.update(dict(database=database, schema=schema))
    connection = snowflake.connector.connect(**params)
    
    return connection
```

