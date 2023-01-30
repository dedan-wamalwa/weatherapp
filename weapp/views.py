from django.shortcuts import render,redirect
import json
import urllib.request
# Create your views here.
def index(request):
    if request.method =='POST':
        city = request.POST['city']
        req = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=a206f603779720072cc3d578a00e224f').read()
        json_data = json.loads(req)
        data ={
            "country_code":str(json_data['sys']['country']),
            "cordinates":str(json_data['coord']['lon']) + str(json_data['coord']['lat']),
            "temp":str(json_data['main']['temp'])+'K',
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
            "city":city,
        }
    else:
        data =''
    return render(request,'index.html',{'data':data})
