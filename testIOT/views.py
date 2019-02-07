from django.shortcuts import render, render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Beat, Record, RecordForm
from .serializers import beatserializer
import django
import io

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt

import json

def recommend(request):
    #DetectionModel.filter(date=datetime.today())
    return render(request, 'testIOT/form.html') #HttpResponse('Connected')
    #return HttpResponse("Connected")


@csrf_exempt
def post_data(request):
    if request.method == "POST":
        #   print(request.body)
        received_data = json.loads(request.body.decode('utf-8'))
        print(received_data)
        #existing = Beat.objects.get(pk=1)
        serializer = beatserializer(
            data={
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
        ytotal = []
        x = range(300)

        #for i in beatData:
            #y.append(int(i.beat))
        #print(Beat.objects.get(pk = 1))
        '''data = Beat.objects.get(pk = 1)
        yt = data.beat.split(',')
        y = [int(p) for p in yt]'''
        '''for i in range(2):
            data = Beat.objects.get(pk = (i+1))
            yt = data.beat.split(',')
            yu = [int(p) for p in yt]
            y.extend(yu)'''

        for i in range(len(Beat.objects.all())):
            data = Beat.objects.get(pk = (i+1))
            yt = data.beat.split(',')
            yu = [int(p) for p in yt]
            ytotal.extend(yu)

        y = ytotal[-300:]


        #ax.plot(x, y, '-')

        ## exponential smoothing test
        alpha = 0.4
        # No need to do anything to y0
        for i in range(1, len(y)):
            y[i] = y[i-1] + alpha * (y[i] - y[i-1])
        ##

        #ax.plot(x, y, '-')

        ## exponential smoothing test
        alpha = 0.2
        # No need to do anything to y0
        for i in range(1, len(y)):
            y[i] = y[i-1] + alpha * (y[i] - y[i-1])
        ##

        '''now = datetime.datetime.now()
        delta = datetime.timedelta(days=1)
        for i in range(47):
            x.append(now)
            now += delta'''
        ax.plot(x, y, '-')
        #ax.scatter(x, y)
        #ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
        #fig.autofmt_xdate()
        buf = io.BytesIO()
        canvas = FigureCanvas(fig)
        canvas.print_png(buf)
        response = django.http.HttpResponse(buf.getvalue(), content_type='image/png')
        fig.clear()
        response['Content-Length'] = str(len(response.content))
        return response


def records(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            #temp = form.save(commit=False)
            form.save()
            '''try:
                a = Record.objects.get(unique=temp.unique)
                a.first_name = temp.first_name
                a.last_name = temp.last_name
                a.recommendations = temp.recommendations
                a.unique = temp.unique
                a.save()
            except ObjectDoesNotExist:
                data = Beat.objects.get(pk=1)
                temp.heart_beat = data.beat
                temp.save()'''

            return HttpResponseRedirect('/thanks/')


def thanks(request):
    return render(request, 'testIOT/thanks.html')


def search(request):
    query = request.GET.get('query')
    try:
        query = int(query)
    except ValueError:
        query = None
        results = None
    if query:
        try:
            results = Record.objects.get(unique=query)
        except ObjectDoesNotExist:
            results = 0
    #context = RequestContext(request)
    return render_to_response('testIOT/results.html', {"results": results, })
