from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from mysite.models import BodyInfo

def index(request):
	classmates = BodyInfo.objects.all().order_by('-h')
	now = datetime.now()
	return render(request, "index.html", locals())