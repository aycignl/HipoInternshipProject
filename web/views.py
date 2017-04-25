from django.shortcuts import render
from web.models import SearchEntry


def search(request):
	results = None
	query = request.GET.get('query')
	location = request.GET.get('location')
	if query and location:
		entry, created = SearchEntry.objects.get_or_create(query=query, location=location)
		entry.hits += 1
		entry.save()
		results = entry.get_results()

	previous_searches = SearchEntry.objects.order_by('-last_search').all()[:10]
	context = { 
		'results': results,
		'previous_searches': previous_searches}
	return render(request, 'search.html', context)
