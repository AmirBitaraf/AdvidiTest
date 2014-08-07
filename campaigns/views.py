from django.http import HttpResponse
from campaigns.models import *
from django.db.models import *
import time,datetime,random
from django.shortcuts import render_to_response


#Lettuce: def campaigns_load_data(campaign_id)

def campaigns(request,campaign_id):
	t = datetime.datetime.now()
	dataset_id = t.minute/15 + 1
	revenue_data = impressions.objects.values("banner_id").filter(Q(dataset=dataset_id) & Q(campaign_id=campaign_id) & Q(total_revenue__gt=0)).order_by("-total_revenue")[:10]
	query = list(revenue_data)
	count = len(query)
	if(count >= 5):	
		pass
	else:
		for item in impressions.objects.values("banner_id").filter(Q(dataset=dataset_id) & Q(campaign_id=campaign_id) & Q(total_revenue=0.0) & Q(total_clicks__gt=0)).order_by("-total_clicks")[:5]:
			if(count<5):
				query.append(item)
				count += 1
			else:
				break
		for item in impressions.objects.values("banner_id").filter(Q(dataset=dataset_id) & Q(campaign_id=campaign_id) & Q(total_revenue=0.0) & Q(total_clicks=0)).order_by("?")[:5]:
			if(count<5):
				query.append(item)
				count += 1
			else:
				break
		
	random.shuffle(query)
	return render_to_response('campaign.html', {'query' : query})
