Advidi Test
==========
This is a simple web-application which serves banners for an advertising agency.
It renders banners based on their revenue-performance for each campaign.
You can use it by simply opening **/campaigns/{campaign id}/** web page.

Setting up the dev machine
----------
This web-app is written using Python-Django and uses PostgreSQL but you can change the database server whenever you desire.

To setup the development environment you must have "python" and "postgresql" installed on your machine. You can setup a virtual environment and use "foreman" to make management easier.

The only thing you need to do is download the python requirements using "pip". They are listed in "requirements.txt". Also there is another file, "migratedb.py", which imports all raw data from CSV files.

To run the server you can simply run ```foreman start web```

[Lettuce] is used for testing. You can add your features to the "features" directory and test using ```lettuce ```.


About the Development Process
---------
The development of this web-app is Test-Driven i.e. we write tests before coding. The app is flexible and can be changed easily. We also used some of the best possible indexing and optimization techniques in the database in order to handle as many requests as possible.

The migration code imports the raw CSV files into the "impressions" table which is indexed so that each query will have time complexity O(lgn) based on the height of the created B-Tree.
And by using at most three queries We can now serve up to 9k requests per minute. This result is based on the stress test done using ```siege ```. You can see its output below


```

Transactions:		        9010 hits
Availability:		      100.00 %
Elapsed time:		       59.45 secs
Data transferred:	        2.84 MB
Response time:		        0.33 secs
Transaction rate:	      151.56 trans/sec
Throughput:		        0.05 MB/sec
Concurrency:		       49.86
Successful transactions:        9010
Failed transactions:	           0
Longest transaction:	        0.45
Shortest transaction:	        0.08
```

We save all the other data from the CSV files so that it can be used for logging or other purposes later.

At the Client-Level we used HTML5, CSS3 and jQuery to create an animated page that would be pleasing to the users' eyes.



[Lettuce]:http://lettuce.it/
