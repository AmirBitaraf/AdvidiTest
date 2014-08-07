from lettuce import *
from campaigns.views import campaigns_load_data
import psycopg2,urlparse,os
from django.test.client import Client
result = urlparse.urlparse(os.environ['DATABASE_URL'])
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
conn = psycopg2.connect(database = database,user = username,password = password,host = hostname)
cursor = conn.cursor()


def select_top_revenue():
    cursor.execute("SELECT banner_id FROM campaigns_impressions WHERE dataset_id = 1 AND campaign_id=%s AND total_revenue > 0.0 ORDER BY total_revenue DESC LIMIT 10",(world.campaign_id,))
    ret = []
    for row in cursor.fetchall():
        ret.append(row[0])
    return ret

def select_top_clicks():
    cursor.execute("SELECT banner_id FROM campaigns_impressions WHERE dataset_id = 1 AND campaign_id=%s AND total_revenue = 0.0 ORDER BY total_clicks DESC LIMIT 5",(world.campaign_id,))
    ret = []
    for row in cursor.fetchall():
        ret.append(row[0])
    return ret

def select_random():
    cursor.execute("SELECT banner_id FROM campaigns_impressions WHERE dataset_id = 1 AND campaign_id=%s AND total_revenue = 0.0 AND total_clicks=0 LIMIT 5",(world.campaign_id,))
    ret = []
    for row in cursor.fetchall():
        ret.append(row[0])
    return ret


    

@step(u'Campaign with id ([0-9]+)')
def set_id(step, id):
    world.campaign_id = int(id)

@step(u'I open it$')
def open_view(step):
    c = Client()
    response = str(c.get("/campaigns/%s/" % world.campaign_id))
    world.banner = int(response[response.find("images/image_")+13:response.find(".png")])


@step(u'I open it twice')
def open_view_second(step):
    c = Client()
    response = str(c.get("/campaigns/%s/" % world.campaign_id))
    world.banner = int(response[response.find("images/image_")+13:response.find(".png")])
    response = str(c.get("/campaigns/%s/" % world.campaign_id))
    world.banner_2 = int(response[response.find("images/image_")+13:response.find(".png")])



@step(u'Then I should see a Random Banner')
def see_random_banner(step):
    data = select_random()
    assert world.banner in data, "Random Banner Not Found"
    


@step(u'Then I should see a banner from Top-10')
def then_i_should_see_a_banner_from_top_10(step):
    data = select_top_revenue()
    print type(world.banner), type(data[0])
    assert world.banner in data, "Banner from Top-10 Not Found"



@step(u'Then I should see a Top Click Banner')
def then_i_should_see_a_top_click_banner(step):
    data = select_top_clicks()
    assert world.banner in data, "Banner from Top Clicks Not Found"


@step(u'Then I shouldn\'t see equal banners')
def then_i_shouldn_t_see_equal_banners(step):
    assert world.banner != world.banner_2 , "Equal Banners Found"









