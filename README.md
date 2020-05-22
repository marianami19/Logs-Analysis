fullstack-nanodegree-vm
=============
I have used the Git Bash command Line to run the code.
***python backend.py***

*Note:*
The aliases I have used for the three tables are:
authors a
articles b
log c
1. What are the most popular three articles of all time?
COLUMNS TO DISPLAY:
1]Title of the article.
2]The views each article received.
MY LOGIC:
The number of views per article can be calculated from the log table whereas the title of each article can be found in the articles table of the database.
The structure of the path column of the log table is as follows:
/article/slug-column-of-articles-table
Thus to relate both the tables I used the substring function to eliminate the /article/ part of the path column.
Every time a user views a article the entry is updated in the logs table.
The count function allows us the count the total number of views and to find out the views per article, I grouped the query by the title column of the articles table.
Finally in order to print the top 3 articles, I ordered the views(column that counts the views) column by descending and gave it a limit 3.

2. Who are the most popular article authors of all time?
COLUMNS TO DISPLAY:
1]name of the author
2]total views=summing up the views of all the articles the author has written.
**VIEWS TO CREATE**:
create view fam_authors as select a.name,b.title,count(substring(c.path from 10)) as new_path from authors a , articles b , log c where a.id=b.author and substring(c.path from 10)=b.slug group by a.name,b.title;

MY LOGIC:
In the view:
The view fam_authors is just a advancement of the previous table with an
added column "name" from the authors table. As the id column of the authors table and the author column of the articles table are the same, relating the authors table to the query was simpler.
In the query:
By using the sum function I added up the views and grouped it by the names of the authors.

3. On which days did more than 1% of requests lead to errors?
*Note*
Aliases used for the views crated are:
for_successfulreq a
for_failedreq b
for_requestsperday c

COLUMNS TO DISPLAY:
1]date which has more than 1% errors
2]Percentage of errors
**VIEWS TO CREATE**
create view for_successfulreq as select date(time) as date,count(status) as success from log  where status='200 OK' group by date;

create view for_failedreq as select date(time) as date,count(status) as failure from log where status!='200 OK' group by date;

create or replace view for_requestsperday as select a.date as date,a.success + b.failure as total_requests from for_successfulreq a,for_failedreq b where a.date=b.date;

MY LOGIC:
view 1(for_successfulreq) = Count of all successful requests grouping by date.
view 2(for_failedreq) = Count of all failed requests grouping by date.
view 3(for_requestsperday) = Total number of requests each day.

In the query:
To calculate percentage of Errors occurred per day I divided the failed requests by the total requests and multiplied by 100.
Gave a where clause to only print rows which have more than 1% of errors.
And finally did the necessary grouping.
