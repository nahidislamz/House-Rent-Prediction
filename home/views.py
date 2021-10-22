from django.shortcuts import render
from . import util
from .models import History
# Create your views here.
def home(request):
    
   
    util.load_saved_artifacts()
    locations = util.get_location_names()
    estimated_price = ""
    total_sqft = 0.00
    location = ""
    bhk = 0
    bath = 0
    history = History.objects.all()
    if request.method == 'POST':

        total_sqft = float(request.POST.get('area_size'))
        location = request.POST.get('location')
        bhk = int(request.POST.get('bhk'))
        bath = int(request.POST.get('bath'))
        estimated_price = util.get_estimated_price(location,total_sqft,bhk,bath)
                
    context ={
        'locations': locations,
        'estimated_price': estimated_price,
        'total_sqft':total_sqft,
        'bath':bath,
        'location':location,
        'bhk':bhk,
        'history':history,
        }
        
    return render(request,'index.html',context)