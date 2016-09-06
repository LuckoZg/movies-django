from django.views import generic
from .models import Movie

class IndexView(generic.ListView):
	template_name = 'movies/index.html'
	context_object_name = 'movies'

	def get_queryset(self):
		return Movie.objects.order_by('position')[:5]

class ListView(generic.ListView):
	template_name = 'movies/list.html'
	context_object_name = 'movies'

	def get_queryset(self):
		return Movie.objects.order_by('position')

class DetailView(generic.DetailView):
	model = Movie
	template_name = 'movies/detail.html'