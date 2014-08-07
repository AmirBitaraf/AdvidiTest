from django.db import models


class DataSet(models.Model):
	dataset_id = models.IntegerField(null=False,primary_key=True)


class impressions(models.Model):
#	impression_id = models.AutoField(primary_key=True)
	banner_id = models.IntegerField(null=False)
	campaign_id = models.IntegerField(null=False)
	total_revenue = models.FloatField(default = 0.0)
	total_clicks = models.IntegerField(default = 0)
	dataset = models.ForeignKey(DataSet)
	class Meta:
		index_together = [["dataset","campaign_id","total_revenue","total_clicks"]]
		unique_together = (("dataset","campaign_id","banner_id"),)
	def __unicode__(self):
		return "banner_id : %s,revenue : %s" % (self.banner_id,self.total_revenue)

class clicks(models.Model):
	click_id = models.IntegerField(null=False)
	banner = models.ForeignKey(impressions)
	class Meta:
		index_together = [["click_id"],]

class conversions(models.Model):
	conversion_id = models.IntegerField(null=False)
	click = models.ForeignKey(clicks)
	revenue = models.FloatField()
	class Meta:
		index_together = [["click","revenue"]]

