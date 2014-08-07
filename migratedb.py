import psycopg2,urlparse,os
result = urlparse.urlparse(os.environ['DATABASE_URL'])
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
conn = psycopg2.connect(database = database,user = username,password = password,host = hostname)



#conn = psycopg2.connect("dbname='AdvidiTest' user='postgres' host='localhost' password='2288428'")
cursor = conn.cursor()






for i in range(1,5):
	print "Creating Dataset #%s..." % i
	query =  "INSERT INTO campaigns_dataset VALUES (%s);"
	cursor.execute(query, (i,))


	Data = {}
	Campaign_Data = {}

	print "Getting Conversions Data on Dataset #%s..." % i
	header = False
	f = open("./dataset/%s/conversions_%s.csv" % (i,i))
	for line in f:
		if not header:
			headers = line.strip().split(',')
			header = True
		else:
			spl = line.strip().split(',')
			click_id = int(spl[1])
			Data[click_id] = (int(spl[0]),float(spl[2]))
	f.close()




	print "Populating Clicks Table on Dataset #%s..." % i
	header = False
	f = open("./dataset/%s/clicks_%s.csv" % (i,i))
	for line in f:
		if not header:
			headers = line.strip().split(',')
			header = True
		else:
			spl = map(int,line.strip().split(','))
			click_id = int(spl[0])
			banner_id = int(spl[1])
			campaign_id = int(spl[2])
			if not (campaign_id,banner_id) in Campaign_Data:
				Campaign_Data[(campaign_id,banner_id)] = [0,0.0]
			Campaign_Data[(campaign_id,banner_id)][0] += 1
			if click_id in Data:
				Campaign_Data[(campaign_id,banner_id)][1] += Data[click_id][1]
		



	print "Creating Impressions Table on Dataset #%s..." % i

	header = False
	f = open("./dataset/%s/impressions_%s.csv" % (i,i))
	for line in f:
		if not header:
			headers = line.strip().split(',')
			header = True
		else:
			spl = map(int,line.strip().split(','))
			banner_id = spl[0]
			campaign_id = spl[1]
			cursor.execute("SELECT 1 FROM campaigns_impressions WHERE campaign_id=%s AND banner_id=%s AND dataset_id=%s",(campaign_id,banner_id,i))
			if cursor.fetchone() is not None:
				continue;
			if (campaign_id,banner_id) in Campaign_Data:
				clicks = Campaign_Data[(campaign_id,banner_id)][0]
				revenue = Campaign_Data[(campaign_id,banner_id)][1]
			else:
				clicks = 0
				revenue = 0.0
			query =  "INSERT INTO campaigns_impressions (banner_id, campaign_id, dataset_id,total_clicks,total_revenue) VALUES (%s, %s, %s, %s, %s);"
			data = (banner_id,campaign_id,i,clicks,revenue)
			cursor.execute(query, data)


	print "Creating Clicks Table on Dataset #%s..." % i
	header = False
	f = open("./dataset/%s/clicks_%s.csv" % (i,i))
	for line in f:
		if not header:
			headers = line.strip().split(',')
			header = True
		else:
			spl = map(int,line.strip().split(','))
			cursor.execute("SELECT id FROM campaigns_impressions WHERE campaign_id = %s AND banner_id = %s AND dataset_id = %s",(spl[2],spl[1],i))
			imp_id = cursor.fetchone()[0]
			query =  "INSERT INTO campaigns_clicks (click_id, banner_id) VALUES (%s, %s);"
			data = (spl[0],imp_id)
			cursor.execute(query, data)


	print "Creating Conversions Table on Dataset #%s..." % i
	header = False
	f = open("./dataset/%s/conversions_%s.csv" % (i,i))
	for line in f:
		if not header:
			headers = line.strip().split(',')
			header = True
		else:
			spl = line.strip().split(',')
			cursor.execute("SELECT id FROM campaigns_clicks WHERE click_id = %s",(int(spl[1]),))
			click_id = cursor.fetchone()[0]
			query =  "INSERT INTO campaigns_conversions (conversion_id, revenue,click_id) VALUES (%s, %s, %s);"
			data = (int(spl[0]),float(spl[2]),click_id)
			cursor.execute(query, data)






print "Commiting to Database..."
conn.commit()

