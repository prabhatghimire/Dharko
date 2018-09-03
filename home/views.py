from django.shortcuts import render
from .models import Service
from gallery.models import Gallery
from .forms import Search
from django.db.models import Q
from django.views.generic import DetailView

def home(request):
    return render(request, 'home/home.html')

def contact(request):
    return render(request, 'home/contact.html')

# def about(request):
#     return render(request, 'home/about.html')




def search(request):
	form = Search()
	if request.method == 'POST':
		form = Search(request.POST)
		if form.is_valid():
			something = form.cleaned_data['search']
			result =Service.objects.all().filter(Q(title__icontains=something)
			 | Q(detail__icontains=something))
			result1 =Gallery.objects.all().filter(Q(title__icontains=something)
			 | Q(detail__icontains=something))
			return render(request, 'home/search.html', {'result': result, 'result1': result1})
	return render(request, 'home/home.html', {'form': form})

# class GalleryDetailView(DetailView):

#     model = Gallery

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context