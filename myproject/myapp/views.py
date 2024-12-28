from django.shortcuts import render
from .models import SampleData

def index(request):
    data = SampleData.objects.all()  # Fetch all records
    return render(request, 'index.html', {'data': data})
