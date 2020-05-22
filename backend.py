#!/usr/bin/env python2.7
import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()
sql = """select b.title,count(*) as views from log c,articles b
         where substring(c.path from 10)=b.slug
         group by b.title order by views desc limit 3;"""
c.execute(sql)
rows1 = c.fetchall()
print "\nTitle  |  Views"
for content in rows1:
    print content[0] + "  |  ", content[1]

c.execute("""select name,sum(new_path) as views from fam_authors
             group by name order by views desc;""")
rows2 = c.fetchall()
print "\nAuthor  |  Views"
for content in rows2:
    print content[0] + "  |  ", content[1]

c.execute("""select c.date as date,100 * b.failure/c.total_requests as per
                from for_failedreq b ,for_requestsperday c
                where b.date=c.date and 100*b.failure/c.total_requests>1
                group by c.date,b.failure,c.total_requests;""")
rows3 = c.fetchall()
print "\nDate  |  Percentage of Errors"
for content in rows3:
    print content[0].strftime('%d %b %Y'), "  |  " + str(content[1]) + "%"
db.close()
