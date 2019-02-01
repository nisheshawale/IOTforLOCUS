from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Beat
from .serializers import beatserializer
import django
import io

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt

import json

def index(request):
    #DetectionModel.filter(date=datetime.today())
    return HttpResponse("Working...") #HttpResponse('Connected')
    #return HttpResponse("Connected")

@csrf_exempt
def post_data(request):
    if request.method == "POST":
        #   print(request.body)
        received_data = json.loads(request.body.decode('utf-8'))
        print(received_data)
        serializer = beatserializer(
            data={ #Must match model
                #'date': datetime.datetime.now(),
                #'room': received_data['room'],
                #'temperature_f': received_data['temperature_f'],
                #'humidity': received_data['humidity']
                'beat': received_data['beat']
                })

        if serializer.is_valid():
            serializer.save()
        return HttpResponse("Got JSON data")


        #else:
         #   print("Data not valid")
          #  return HttpResponse("Upload failed")

        #return HttpResponse("<h1>End of response</h1>")
    else:
        #tempModel = TempModel.objects.get(pk = 1)
        #html = '<h2>' + tempModel.room + '</h2>'
        #return HttpResponse(html)

        #tempModel = TempModel.objects.all()
        #context = {'tempModel': tempModel}
        beatData = Beat.objects.all()
        #context = {'beatData': beatData}
        #return render(request, 'testIOT/index.html', context)

        fig = Figure()
        ax = fig.add_subplot(111)
        y = []
        x = range(47)

        for i in beatData:
            y.append(i.beat)

        '''now = datetime.datetime.now()
        delta = datetime.timedelta(days=1)
        for i in range(47):
            x.append(now)
            now += delta'''
        ax.plot(x, y, '-')
        #ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
        #fig.autofmt_xdate()
        buf = io.BytesIO()
        canvas = FigureCanvas(fig)
        canvas.print_png(buf)
        response = django.http.HttpResponse(buf.getvalue(), content_type='image/png')
        fig.clear()
        response['Content-Length'] = str(len(response.content))
        return response