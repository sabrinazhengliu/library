## Create Scheduled Task
```sql
create or replace task my_special_task
    warehouse = <WAREHOUSE>
    schedule = 'USING CRON 00 00 * * *'   -- mm hh dom month dow
    comment = 'this runs daily'
as
call my_stored_proc()
```

## Activate/Enable Task
must run this step before task automatically runs on schedule
```sql
show tasks;
alter task my_special_task resume;
show tasks;
```

## Manually Run Task
```sql
execute task my_special_task;
```

## Check Task History
```
select *
from table(<DATABASE>.information_schema.task_history())
where schema_name = '<SCHEMA>'
order by scheduled_time
```
