from django.shortcuts import render, redirect
from django.http  import HttpResponse
import datetime as dt
from .models import Image




# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def photos_of_day(request):
    date = dt.date.today()
    photos = Image.photos_of_day()
    return render(request, 'all/today_photos.html', {"date": date, "photos":photos})


    
# View Function to present news from past days
def past_days_photos(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()

    if date == dt.date.today():
        return redirect(photos_of_day)
    
    photos = Image.photos_of_day(date)


    return render(request, 'all/past_photos.html', {"date": date,"photos":photos})
