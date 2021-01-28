import cx_Oracle

import os
os.putenv('NLS_LANG', '.utf8')
conn = cx_Oracle.connect('hr', 'hr', 'localhost/xe')
cur = conn.cursor()

cur.execute("select * from jobs where job_id like :jobid", jobid = "AD%")
for data in cur:
    print(data)

cur.execute("insert into test values (:aa, :bb)", ('77','88'))

cur.close()
conn.commit()
conn.close()
