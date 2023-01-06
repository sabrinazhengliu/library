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
