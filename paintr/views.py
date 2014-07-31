from django.shortcuts import render
from django.http import XMLHttpRequest

import json
from models import Canvas, Point


#create new canvas from user request
def create_canvas(request):
	if request.method == 'POST':
		data = json.load(request.body)

		newName = data['title']
		uuid = newName.replace(' ', '').lower() #remove spaces and make lower case

		if len(uuid) > 10: uuid = uuid[:10]

		newC = Canvas()
		newC.uuid = uuid
		if len(newName) > 50: newName =newName[:50]
		newC.title = newName

		newC.save()

		return XMLHttpRequest('OK')


#data handeling
def receive_data(request):
	pass

def send_data(request):
	pass

#map view
def map_view():
	pass