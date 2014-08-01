from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from datetime import datetime

import json
from models import Canvas, Point


#create new canvas from user request
def create_canvas(request):
	respons = 'Failure'
	if request.method == 'POST':
		data = json.loads(request.body)

		newName = data['canvasTitle']
		uuid = newName.replace(' ', '').lower() #remove spaces and make lower case

		if len(uuid) > 10: uuid = uuid[:10]

		newC = Canvas()
		newC.uuid = uuid
		if len(newName) > 50: newName =newName[:50]
		newC.title = newName

		newC.save()

		respons = "OK"

	return HttpResponse(json.dumps({"respons":respons}))


#data handeling
def receive_data(request):
	respons = 'Failure'
	if request.method == 'POST':
		data = json.loads(request.body)

		canvas = get_object_or_404(Canvas, pk=data['uuid'])

		for point in data['points']:
			newP = Point()
			newP.latitude = point['latitude']
			newP.longitude = point['longitude']

			newP.creation_time = datetime.now()
			newP.canvas = canvas

			newP.save()

		respons = str(len(data['points']))

	return HttpResponse(json.dumps({'respons':respons}))

def get_data(request):
	outData = {'respons':'Failure'}
	if request.method == 'POST':
		data = json.loads(request.body)

		uuid = data['uuid']
		canvas = get_object_or_404(Canvas, pk=uuid)

		points = Point.objects.filter(canvas=canvas)

		pointData = [[p.latitude, p.longitude] for p in points]

		outData = {
			'canvas': uuid,
			'points': pointData,
			'respons': 'OK',
		}

	return HttpResponse(json.dumps(outData))



#map view
def map_view(request):
	canvases = Canvas.objects.all()

	return render(request, 'paintr/map.html', {'canvases': canvases})

def tracker_view(request):
	canvases = Canvas.objects.all()

	return render(request, 'paintr/tracker.html', {'canvases': canvases})
	#return render(request, 'paintr/brush.html', {'canvases': canvases})