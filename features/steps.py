from lettuce import *
from campaigns.views import campaigns_load_data
import psycopg2,urlparse,os
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


    



@step(u'Campaign with id ([0-9]+)')
def set_id(step, id):
    world.campaign_id = int(id)

@step(u'I open it$')
def open_view(step):
    world.campaign_data = campaigns_load_data(world.campaign_id)


@step(u'I open it twice')
def open_view_second(step):
    world.campaign_data = campaigns_load_data(world.campaign_id)
    world.campaign_data_2 = campaigns_load_data(world.campaign_id)


@step(u'I should see Top-([0-9]+) Banners')
def check_topx(step, topx):
    topx = int(topx)
    bannerset = []
    flag = True
    for item in select_top_revenue():
        flag = flag and not item in world.campaign_data

    assert flag, "Top Banners Not Match"


@step(u'I should see Top Click Banner')
def then_i_should_see_top_click_banner(step):
    cursor.execute("SELECT banner_id FROM campaigns_impressions WHERE dataset_id = 1 AND campaign_id=%s AND total_revenue = 0.0 ORDER BY total_clicks DESC",(world.campaign_id,))
    banner_id = cursor.fetchone()[0]
    flag = False
    for item in world.campaign_data:
        flag = flag or banner_id == item['banner_id']
    assert flag , "Top Click Banner Not Found"



@step(u'Then I should see a Random Banner')
def see_random_banner(step):
    cursor.execute("SELECT banner_id FROM campaigns_impressions WHERE dataset_id = 1 AND campaign_id=%s AND total_revenue = 0.0 ORDER BY total_clicks DESC",(world.campaign_id,))
    rows = cursor.fetchall()
    flag = False
    for item in world.campaign_data:
        flag = flag or (item['banner_id'],) in rows
    assert flag, "Random Banner Not Found"

@step(u'Then I shouldn\'t see equal sequences')
def then_i_shouldn_t_see_equal_sequences(step):
    eq = 0
    for i in range(len(world.campaign_data)):
        if world.campaign_data[i]['banner_id'] == world.campaign_data_2[i]['banner_id']:
            eq += 1
    assert eq <= 3, "Saturation Found"
    








