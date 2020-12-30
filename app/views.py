from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from app.forms import reg_form
from app.models import reg

# Create your views here.

def home(request):
    return render(request,'app/home.html',{})

def login_user(request):

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'You have Logged In!!')
            return redirect('home')

        else:
            messages.success(request,'Sorry Invalid Input!!')
            #return redirect('index')
            return render(request,'Login/index.html')

    else:
        return render(request,'Login/index.html')

def logout_user(request):
    logout(request)
    messages.success(request,'You have Been Logged OUT...')
    return redirect('home')

def register(request):
    if request.method=='post':

        form=reg_form(request.post)
        if form.is_valid():
            name=request.post.get('name','')
            gender=request.post.get('gender','')
            email_reg=request.post.get('email_reg','')
            username_reg=request.post.get(username_reg,'')
            password_reg=request.post.get('password_reg','')
            reg_obj = reg(name = name,gender=gender,email_reg=email_reg,username_reg=username_reg,password_reg=password_reg)
            reg_obj.save()

        else:
            form = reg_form

    return render(request, 'registeration/index.html')


def crypto_home(request):
    import requests
    import json

    #For Price
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,LTC,XLM,ADA,USDT&tsyms=INR")
    price = json.loads(price_request.content)

    #For news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request,'Crypto/home.html',{'api':api,'price':price})

def prices(request):

    if request.method == 'POST':
        import requests
        import json

        quote = request.POST['quote']
        quote = quote.upper()
        cry_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=INR")
        crypto = json.loads(cry_request.content)


        return render(request,'Crypto/prices.html',{'quote':quote,'crypto':crypto})

    else:
        return render(request,'Crypto/prices.html',{})


def tic_tac(request):

    return render(request, 'Tic_tac/test3.html')


def map(request):
    return render(request,'map.html',{})    
