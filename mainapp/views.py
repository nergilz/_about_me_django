from django.shortcuts import render, render_to_response
import datetime
from .models import Work
from .models import Study

# Create your views here.
def index_view(request):
    name = 'Name'
    surname = 'Surname'
    birthday = datetime.date(day=22, month=3, year=1979) # in html {{birthday|date:"Y M D"}}
    return render_to_response('index.html', {'name': name, 'surname': surname, 'birthday': birthday})

def study_view(request):
    study_list = Study.objects.all()
    return render_to_response('study.html', {'studys': study_list})

def works_view(request):
    work_list = Work.objects.all()
    return render_to_response('works.html', {'works': work_list})
