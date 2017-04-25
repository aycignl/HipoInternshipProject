from django.conf import settings
from django.db import models
import requests


class SearchEntry(models.Model):
	query = models.CharField(max_length=80)
	location = models.CharField(max_length=80)
	hits = models.PositiveIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	last_search = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = ('query', 'location')
		verbose_name_plural = "Search Entries"

	def __str__(self):
		return '{query} in {location}'.format(
			query=self.query, location=self.location)

	def get_results(self, limit=25):
		url = settings.FOURSQUARE_VENUE_API_URL.format(
			location=self.location, 
			query=self.query, 
			limit=limit,
			client_id=settings.FOURSQUARE_CLIENT_ID, 
			client_secret=settings.FOURSQUARE_CLIENT_SECRET)
		return requests.get(url).json()