from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'aplicacion/index.html')

def about(request):
    return render(request, 'aplicacion/about.html')

def contact(request):
    return render(request, 'aplicacion/contact.html')

def gallery(request):
    return render(request, 'aplicacion/gallery.html')

def testimonial(request):
    return render(request, 'aplicacion/testimonial.html')
    
