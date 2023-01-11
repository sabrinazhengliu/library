## Check Table Exists
```sql
select count(*)
from <DATABASE>.information_schema.tables
where table_schema = '<SCHEMA>'
and table_name = '<TABLE>'
```

## Check Table Ownership and Prilileges
```sql
select *
from <DATABASE>.information_schema.table_privileges
where table_schema = '<SCHEMA>'
and table_name = '<TABLE>'
```

## Check Available Libraries and Versions
```sql
select *
from <DATABASE>.information_schema.packages
where language = 'python'
and package_name = 'jellyfish'
```

## Check Query History and Query Status
```sql
select query_id
, query_text
, execution_status
, to_time(convert_timezone('America/Denver', start_time)) as start_time
, to_time(convert_timezone('America/Denver', end_time)) as end_time
, ceil(total_elapsed_time / 1000) as seconds_elapsed
, rows_produced
, error_code
, error_message
from table (information_schema.query_history())
where user_name = '<ROLE>'
and schema_name = '<SCHEMA>'
and query_tag = '<TAG>'
and timestampdiff('min', end_time, current_timestamp()) < 60
order by start_time
```
