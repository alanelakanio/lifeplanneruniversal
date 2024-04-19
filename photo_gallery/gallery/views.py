from django.shortcuts import render, redirect
from .models import Photo
from django.shortcuts import render, get_object_or_404

def home(request):
    photos = Photo.objects.all()
    return render(request, 'home.html', {'photos': photos})

def upload_photo(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        Photo.objects.create(image=image)
        return redirect('home')
    return render(request, 'upload_photo.html')



def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    return render(request, 'photo_detail.html', {'photo': photo})