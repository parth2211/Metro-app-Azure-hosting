from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Analytics
from .models import Count
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
# from .models import Analytics
from django.contrib.auth.decorators import login_required
# from django.db.models.loading import get_model
# Create your views here.
from django.apps import apps
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('http://127.0.0.1:8000/analytics')
            return redirect('http://127.0.0.1:8000/home')

        else:
            messages.info(request, 'Username or password is incorrect')
    return render(request, 'login1.html')
def home(request):
    if request.method == "GET": 
        entries = Count.objects.get(add = "Pratap Nagar")
        prat=entries.count
        entries = Count.objects.get(add = "Laxmi Nagar")
        lax=entries.count
        entries = Count.objects.get(add = "Sitabuldi")
        sita=entries.count
        entries = Count.objects.get(add = "Mahal")
        mah=entries.count
        entries = Count.objects.get(add = "Dharampeth")
        dhar=entries.count
        return render(request, 'home.html',{'prat' : prat,'lax' : lax, 'sita' : sita, 'mah' : mah, 'dhar' : dhar})
    else:
        nam = request.POST.get('username')
        age = request.POST.get('age')
        sou = request.POST.get('Source')
        tea = request.POST.get('Destination')
        s = apps.get_model('metro_app', 'Analytics')
        obj = s(name= nam, age=age,source=sou,destination=tea)
        obj.save()
        entries = Count.objects.get(add = sou)
        entries.count-=1
        entries.save()
        entries = Count.objects.get(add = tea)
        entries.count+=1
        entries.save()
        entries = Count.objects.get(add = "Pratap Nagar")
        prat=entries.count
        entries = Count.objects.get(add = "Laxmi Nagar")
        lax=entries.count
        entries = Count.objects.get(add = "Sitabuldi")
        sita=entries.count
        entries = Count.objects.get(add = "Mahal")
        mah=entries.count
        entries = Count.objects.get(add = "Dharampeth")
        dhar=entries.count


        # s = apps.get_model('metro_app', 'Count')

        print(nam,age,sou,tea)
        # print(nam,comp,tea,pun,pra,appr,control)
        messages.success(request, 'Thanks for choosing us !')
        return render(request, 'home.html',{'prat' : prat,'lax' : lax, 'sita' : sita, 'mah' : mah, 'dhar' : dhar})    

@login_required
def analytics(request):
    rows = Analytics.objects.all()
    user = request.user
    print(user)
    if user.is_staff:
        return render(request, 'analytics.html', {'data': rows})
    else:
        messages.info(request, 'Only staff can access this page')
    return redirect('http://127.0.0.1:8000/login')
    # return render(request, 'login1.html')
