Advidi Test
==========
This is a sample web-application which serves banners for an advertising agency.
It renders banners based on their revenue-performance for each campaign.
You can use it by simply opening **/campaigns/{campaign id}/** web page.

Setting up dev machine
----------
This web-app is written using Python-Django and PostgreSQL as database. It has the flexiblity to change the database whenever you want.

To setup the development environment you must have "python" and "postgresql" installed on your machine. You can setup a virtual environment and use "foreman" in order to make management easier.

So the only thing you need to do is to download python requirements using "pip". They are all available in "requirements.txt" file. Also there is another file called "migratedb.py" which imports all raw data from CSV files.

To run the server you can simply type ```foreman start web```

[Lettuce] is used for testing. You can simply add your features to the "features" directory and test using ```lettuce ```.


About Development Process
---------
The development of this web-app is Test-Driven in which we write tests before coding. App is also flexible to any changes made in future. Also we used one of the best possible indexing and optimizations in database in order to handle requests as much as possible.

The migration code here imports raw CSV files into the "impressions" table which is indexed carefully so each query will have time complexity O(lgn) on height of created B-Tree at most.
And by using at most three queries We can now serve up to 9k requests per minute. This result is based on the stress test made using ```siege ```. You can see its output below


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

Also we save all other datas from CSV files so that it can be used for logging or other purposes later.

At the Client-Level we used HTML5,CSS3 and jQuery to make an animated page so it can attract users' eyes.



[Lettuce]:http://lettuce.it/

