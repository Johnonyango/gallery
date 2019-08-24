from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt



# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def photos_of_day(request):
    date = dt.date.today()
    date = dt.date.today()
    return render(request, 'all-news/today_photos.html', {"date": date,})


    
# View Function to present news from past days
def past_days_photos(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()

    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Photos taken on {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)
