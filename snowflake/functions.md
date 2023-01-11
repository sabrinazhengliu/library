## String Repeat Score
```sql
/***
1) Takes a string and return a number between 0 and 1.
2) Removes allsymbols and only keep alphanumerical chars. 
3) Ignores upper/lower case differences. 
4) Repeat Score = count of repetitive paris divided by length - 1.
5) e.g. aaaa -> 1.0 (3/3); aaac -> 0.67 (2/3)
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

## String Serial Score
```sql
/***
1) Takes a string and return a number between 0 and 1.
2) Removes allsymbols and only keep alphanumerical chars. 
3) Ignores upper/lower case differences. 
4) Serial Score = count of sequential paris divided by length - 1.
5) e.g. abcd -> 1.0 (3/3); abcc -> 0.67 (2/3)
6) Reverse sequence also counts, e.g. 12321 -> 1.0
***/

create or replace function udf_score_serial(string varchar)
  returns number
  language sql
  as '
  with clean_string as (select regexp_replace(lower(string), ''[^a-zA-Z0-9]+'', '''') as value)
  select div0(
      regexp_count(value,
        ''(ab)|(cd)|(ef)|(gh)|(ij)|(kl)|(mn)|(op)|(qr)|(st)|(uv)|(wx)|(yz)|(01)|(23)|(45)|(67)|(89)'', 2, ''i'')
    + regexp_count(value,
        ''(bc)|(de)|(fg)|(hi)|(jk)|(lm)|(no)|(pq)|(rs)|(tu)|(vw)|(xy)|(12)|(34)|(56)|(78)|(90)'', 2, ''i'')
    + regexp_count(reverse(value),
        ''(ab)|(cd)|(ef)|(gh)|(ij)|(kl)|(mn)|(op)|(qr)|(st)|(uv)|(wx)|(yz)|(01)|(23)|(45)|(67)|(89)'', 2, ''i'')
    + regexp_count(reverse(value),
        ''(bc)|(de)|(fg)|(hi)|(jk)|(lm)|(no)|(pq)|(rs)|(tu)|(vw)|(xy)|(12)|(34)|(56)|(78)|(90)'', 2, ''i'')
    , len(value) - 1)
  from clean_string'
;
describe function udf_score_serial(string)
;
select get_ddl('function', 'udf_score_serial(string)')
;
select <DATABASE>.<SCHEMA>.udf_score_serial('aabbccdd')
```
