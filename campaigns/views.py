from django.http import HttpResponse,Http404
from campaigns.models import *
from django.db.models import *
import time,datetime,random
from django.shortcuts import render_to_response


def campaigns_load_data(dataset_id,campaign_id):
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
	return query
	




def campaigns(request,campaign_id):
	t = datetime.datetime.now()
	dataset_id = t.minute/15 + 1
	query = campaigns_load_data(dataset_id,campaign_id)
	if len(query) < 1:
		raise Http404

	if not "shown_banners" in request.session.keys():
		request.session["shown_banners"] = []
	if dataset_id != request.session.get("current_dataset",-1):
		request.session["shown_banners"] = []
		request.session["current_dataset"] = dataset_id

	shown_banners = request.session.get("shown_banners",[])

	banner = -1
	for item in query:
		if not item['banner_id'] in shown_banners:
			banner = item['banner_id']
			request.session["shown_banners"] = shown_banners + [banner]
			break
	if banner == -1:
		banner = query[0]['banner_id'] if query[0]['banner_id'] != shown_banners[-1] else query[1]['banner_id']
		request.session["shown_banners"] = [banner]
	return render_to_response('campaign.html', {'banner_id' : banner})
