## String Repeat Score
```sql
/***
Takes a string and return a number between 0 and 1.
Removes allsymbols and only keep alphanumerical chars. 
Ignores upper/lower case differences. 
Repetition Score = count of repetitive paris divided by length - 1.
e.g. aaaa -> 1.0 (3/3); aaac -> 0.67 (2/3)
***/

create or replace function udf_score_repeat(string varchar)
  returns number
  language sql
  as '
  with clean_string as (select regexp_replace(lower(string), ''[^a-zA-Z0-9]+'', '''') as value)
  select div0(
    len(value) - len(regexp_replace(value, concat(
    ''(a+)|(b+)|(c+)|(d+)|(e+)|(f+)|(g+)|(h+)|(i+)|(j+)|(k+)|(l+)|'',
    ''(m+)|(n+)|(o+)|(p+)|(q+)|(r+)|(s+)|(t+)|(u+)|(v+)|(w+)|(x+)|'',
    ''(y+)|(z+)|(0+)|(1+)|(2+)|(3+)|(4+)|(5+)|(6+)|(7+)|(8+)|(9+)'')
    , ''~''))
    , len(value) - 1)
  from clean_string'
;
describe function udf_score_repeat(string)
;
select get_ddl('function', 'udf_score_repeat(string)')
;
select <DATABASE>.<SCHEMA>.udf_score_repeat('aabbccdd')
```

