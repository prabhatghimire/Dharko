from django.shortcuts import render
from gallery.models import Gallery 



def gallery(request):
    return render(request, 'gallery/gallery.html')



def post(request):
    return render(request, 'gallery/post.html')


