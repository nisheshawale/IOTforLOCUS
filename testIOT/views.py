from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import TempModel
from .serializers import tempserializer

import datetime
import json

def index(requeest):
    #DetectionModel.filter(date=datetime.today())
    return HttpResponse("Working...") #HttpResponse('Connected')
    #return HttpResponse("Connected")

@csrf_exempt
def post_data(request):
    if request.method == "POST":
        #   print(request.body)
        received_data = json.loads(request.body.decode('utf-8'))
        print(received_data)
        serializer = tempserializer(
            data={ #Must match model
                #'date': datetime.datetime.now(),
                'room': received_data['room'],
                'temperature_f': received_data['temperature_f'],
                'humidity': received_data['humidity']
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

        tempModel = TempModel.objects.all()
        context = {'tempModel': tempModel}
        return render(request, 'testIOT/index.html', context)

