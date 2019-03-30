from django.db import transaction
from django.shortcuts import render
from django.utils import timezone
from django.utils.datetime_safe import datetime
import json
from .models import Prom

@transaction.atomic
def all_proms(request):
    today = datetime.now()
    promt = Prom.objects.filter(Start_date__lte=today, Stop_date__gte=today)
    return render(request, 'index.html', {'promt': promt})
