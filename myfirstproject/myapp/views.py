from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .models import feature

# Create your views here.
def register(request):
    if request.method == 'POSt':
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      password2 = request.POST['password2']

      if password == password2:
          if user.object.filter(email=email).exists():
            messages.info(request, 'Email already used')
            return redirect('register')
          elif User.objects.filter(username=username).exists():
            message.info(request, 'Email already used')
            return redirect('register')
          else:
            user = User.objects.create_user(username=username ,email=email, password = password)
            user.save();
            return redirect('login')
      else:
        messages.info(request, 'Password not the same')
        return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'credentials invalid')
            return render(request,'login.html')

    else:
         return render(request, 'login.html')

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request,'counter.html',{'amount': amount_of_words} )

def index(request):
  features = feature.objects.all()
  return render(request,'index.html',{'feature':features})

""" feature1 =feature()
    feature1.id =0
    feature1.name ='Fast'
    feature1.is_true = True
    feature1.details='Our service is very quick'

    feature2 =feature()
    feature2.id =1
    feature2.is_true = False
    feature2.name ='Free repair warrenty 10years '
    feature2.details='we will repair your car free'

    feature3 =feature()
    feature3.id =2
    feature3.is_true = True
    feature3.name ='Insurrance document'
    feature3.details='Everything you need to know'

    feature4 =feature()
    feature4.id =3
    feature4.is_true = True
    feature4.name ='Reviews for company'
    feature4.details='Here you will get reviews'

    features = {feature1,feature2,feature3,feature4}
    return render(request,'index.html',{'features':features})"""

    #return render(request,'index.html',{'feature1':feature1,'feature2':feature2,'feature3':feature3})
    #return render(request,'index.html',{'feature':feature1})
    #return render(request,'index.html')


    