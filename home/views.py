from django.shortcuts import render
from . import util
# Create your views here.
def home(request):
    
    if request.method == 'POST':

        total_sqft = float(request.POST.get('area_size'))
        location = request.POST.get('location')
        bhk = int(request.POST.get('bhk'))
        bath = int(request.POST.get('bath'))

        util.load_saved_artifacts()
        print(total_sqft," location: ",location," BHK: ",bhk," BATH: ",bath)
        estimated_price = util.get_estimated_price(location,total_sqft,bhk,bath)
        print("estimated_price = ",estimated_price)
        context ={
            'locations': util.get_location_names(),
            'estimated_price': estimated_price,
            'total_sqft':total_sqft,
            'bath':bath,
            'location':location,
            'bhk':bhk
            }
        
    return render(request,'index.html',context)