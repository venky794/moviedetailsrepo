from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import deleting_data, Inserting_data, Updating_data
from .models import Movies_data


def home(request):
    return render(request, 'movies/home.html')


def creating_view(request):
    if request.method == 'POST':
        inform = Inserting_data(request.POST)
        if inform.is_valid():
            messages.success(request, 'Form submission successful')
            mid = request.POST.get('movie_id')
            mame = request.POST.get('movie_name')
            maiming = request.POST.get('timings')
            loc = request.POST.get('location')
            data = Movies_data(
                movie_id=mid,
                movie_name=mame,
                timings=maiming,
                location=loc
            )
            data.save()

            inform = Inserting_data()

            return render(request, 'movies/create.html', {'form': inform})
        else:
            return HttpResponse('invalid')
    else:
        inform = Inserting_data()
        return render(request, 'movies/create.html', {'form': inform})


def display_view(request):
    details = Movies_data.objects.all()
    return render(request, 'movies/display.html', {'details': details})


def update_view(request):
    if request.method == 'POST':
        ufo = Updating_data(request.POST)
        if ufo.is_valid():
            mid = request.POST.get('movie_id')
            maiming = request.POST.get('timings')
            loc = request.POST.get('location')
            mame = request.POST.get('movie_name')
            movie = Movies_data.objects.filter(movie_id=mid)
            if not movie:
                return HttpResponse('Not Available')
            else:
                movie.update(movie_name=mame,
                             timings=maiming,
                             location=loc)
            ufo = Updating_data()
            messages.success(request, 'updated successfully')
            return render(request, 'movies/update.html', {'form': ufo})
    else:
        ufo = Updating_data()
        return render(request, 'movies/update.html', {'form': ufo})


def delete_view(request):
    if request.method == "POST":
        deform = deleting_data(request.POST)
        if deform.is_valid():
            mid = request.POST.get('movie_id')
            movie_id = Movies_data.objects.filter(movie_id=mid)
            mame = request.POST.get('movie_name')
            movie_name = Movies_data.objects.filter(movie_name=mame)
            if movie_id and movie_name:
                movie_id.delete()
                deform = deleting_data()
                context = {'form': deform}
                messages.success(request, 'movie deleted successful')
                return render(request, 'movies/delete.html', context)

            else:
                return HttpResponse('Not Available')
    else:
        deform = deleting_data()
        context = {'form': deform}
        return render(request, 'movies/delete.html', context)
