from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from datetime import datetime

import json
from models import Canvas, Line, Point


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


#data handling
def receive_data(request):
	respons = 'Failure'
	if request.method == 'POST':
		data = json.loads(request.body)

		canvas = get_object_or_404(Canvas, pk=data['uuid'])

		# create a new line object and initialize it with the given parameters
		newLine = Line()
		newLine.line_type = data['type']
		newLine.line_width = data['width']
		newLine.line_color = data['color']
		newLine.canvas = canvas;
		newLine.save()

		for point in data['points']:
			newP = Point()
			newP.latitude = point['latitude']
			newP.longitude = point['longitude']

			newP.creation_time = datetime.now()
			newP.line = newLine

			newP.save()

		respons = "OK"

	return HttpResponse(json.dumps({'respons':respons}))

def get_data(request):
	outData = {
		'respons':'Failure',
		'lines': [],
		}

	if request.method == 'POST':
		data = json.loads(request.body)

		uuid = data['uuid']
		canvas = get_object_or_404(Canvas, pk=uuid)

		lines = Line.objects.filter(canvas=canvas)

		for l in lines:
			points = Point.objects.filter(line=l)
			#convert to a format that leaflet understands
			pointData = [[p.latitude, p.longitude] for p in points]
			outData['lines'].append({
					'type': l.line_type,
					'width': l.line_width,
					'color': l.line_color,
					'points':pointData,
				})


		outData['canvas'] = uuid
		outData['respons'] = 'OK'

	return HttpResponse(json.dumps(outData))



#map view
def map_view(request):
	canvases = Canvas.objects.all()

	return render(request, 'paintr/map.html', {'canvases': canvases})

def map_view_mobile(request):
	canvases = Canvas.objects.all()

	return render(request, 'paintr/map_mobile.html', {'canvases': canvases})

def tracker_view(request):
	canvases = Canvas.objects.all()

	return render(request, 'paintr/tracker.html', {'canvases': canvases})

def brush_view(request):
	canvases = Canvas.objects.all()

	return render(request, 'paintr/brush.html', {'canvases': canvases})
