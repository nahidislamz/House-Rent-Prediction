from django.shortcuts import render,redirect
from . import util
from .models import History
# Create your views here.
def home(request):
    
   
    util.load_saved_artifacts()
    locations = util.get_location_names()
    history = History.objects.all().order_by('-id')[0:3]
    estimated_price = ""
    total_sqft = 0.00
    location = ""
    bhk = 0
    bath = 0

    save_history = History()


    if request.method == 'POST':

        total_sqft = float(request.POST.get('area_size'))
        location = request.POST.get('location')
        bhk = int(request.POST.get('bhk'))
        bath = int(request.POST.get('bath'))
        estimated_price = util.get_estimated_price(location,total_sqft,bhk,bath)
        
        save_history.area = float(request.POST.get('area_size'))
        save_history.location = request.POST.get('location')
        save_history.bedrooms = int(request.POST.get('bhk'))
        save_history.bathroom = int(request.POST.get('bath'))
        save_history.estimated_price = util.get_estimated_price(location,total_sqft,bhk,bath)
        save_history.save()   

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


def historyView(request):
    history = History.objects.all().order_by('-id')
    context={
        'history':history
    }
    return render(request,'history.html',context)


def history_delete(request, id):
    history = History.objects.get(id=id)
    history.delete()
    return redirect('history')