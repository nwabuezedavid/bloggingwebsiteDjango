from ast import Num
from turtle import title
from  django.contrib.auth.models import User
from django.contrib.auth import logout,login
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect, render
from numpy import datetime_data, sort
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
# Create your views here.
from  . formCreate import detailMoldelForm

def homepage (request):
   
    if request.method == "GET":
        obj = request.GET.get('obj')
        if obj:
            serch = blogDetail.objects.filter(title__startswith = obj)
            print(serch.first() )
            return redirect("linkview", serch)
            
            
            


    if request.user.is_authenticated:
         return redirect('adminView', pk = request.user.id)
    
    linkap =[]
    allItemxc = blogDetail.objects.all()
    allItemxc2 = blogDetail.objects.all()
    entainment__sec = blogDetail.objects.filter(category = 'entertainment')
    sport__sec = blogDetail.objects.filter(category = 'sport')
    recent__sec = blogDetail.objects.all().order_by( '-dateCreated'  )
    
    for allItemxc in allItemxc:
        linkap.append(allItemxc.category)

    finalh = set(linkap)
    allItemImga = blogDetail.objects.all()
   
    

    
    
   

    conx = {
        'allItemImga':allItemImga,
        'allItemxc2':allItemxc2,
        'entainment__sec':entainment__sec,
        'sport__sec':sport__sec,
        'recent__sec':recent__sec,
        'finalh':finalh,
        # 'allItemImga':allItemImga,

     

    }
    return render(request, 'html/homePage.html',conx)


def linkView (request, pk):
    filtedNs = blogDetail.objects.filter( category=pk  )
    filtedvide = blogDetail.objects.filter( category=pk  )
    linkap =[]
    # pagina5 = Paginator(filtedvide, 10)
  
    
    allItemxc = blogDetail.objects.all()
    for allItemxc in allItemxc:
        linkap.append(allItemxc.category)

    finalh = set(linkap)

    
    
        
   


    conx ={
        'filtedNs':filtedNs,
        'filtedvide':filtedvide,
        'finalh':finalh,

    }



    return render(request, 'html/main_overallcon.html', conx)

def adminView(request, pk):
    if not request.user.is_authenticated:
        return redirect('loginUser')
    allItemxc2 = blogDetail.objects.all()
    linkap =[]
    allItemxc = blogDetail.objects.all()
    entainment__sec = blogDetail.objects.filter(category = 'entertainment')
    sport__sec = blogDetail.objects.filter(category = 'sport')
    recent__sec = blogDetail.objects.all().order_by( '-dateCreated'  )[ :13]
    
    for allItemxc in allItemxc:
        linkap.append(allItemxc.category)

    finalh = set(linkap)
    allItemImga = blogDetail.objects.all()
   
    conx = {
        'allItemImga':allItemImga,
        'allItemxc2':allItemxc2,
        'entainment__sec':entainment__sec,
        'sport__sec':sport__sec,
        'recent__sec':recent__sec,
        'finalh':finalh,
        # 'allItemImga':allItemImga,

     

    }

    return render(request, 'html/homePage.html',conx)


def loginUser(request):

    try:
        if request.method == "POST":

            username = request.POST['username']
            email = request.POST['email']
            passwords = request.POST['password']
            password =  make_password(passwords) 


            user = User.objects.get(username = username,  email=email)

            if user:
                login(request, user)
                return redirect('adminView', pk = user.id)
            else: 
                return redirect('loginUser')
    except:
        print('sorry')            
        if request.user.is_authenticated:
            return redirect('adminView', pk = request.user.id)
    return render(request, 'html/login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')

def CreatePost(request):
    alldetail_create = detailMoldelForm()
    if request.method == "POST":
        alldetail_create = detailMoldelForm(request.POST, request.FILES)
        if alldetail_create.is_valid():
            alldetail_create.save()
            return redirect('adminView', pk = request.user.id)

        # Imglent = []
        # mapMp4 = ""
        # videoImagfe = request.FILES.post['video']
        # title = request.POST['title']
        # text = request.POST['text']
        # category = request.POST['category']
        # # for username in videoImagfe:
        #     Imglent.append(username)
        # mapMp4 += Imglent[-3]
        # mapMp4 += Imglent[-2] 
        # mapMp4 += Imglent[-1]
        print(alldetail_create) 
        
        # saveDetailVide = blogDetail.objects.create(title = title, text= text, category=category, videoSl = videoImagfe)
        # saveDetailVide.save()   
        # if mapMp4 == "mp4":
        #     saveDetailVide.save()   

        #     return redirect('adminView', pk = request.user.id)

        # else:
        #     saveDetailVide = blogDetail.objects.create(title = title, text= text, category=category, imgae = videoImagfe)
        #     saveDetailVide.save()   
        #     return redirect('adminView', pk = request.user.id)
 
    
    co = {
        'form':alldetail_create
    }
    return render(request, 'html/adminCreate.html', co)
    


def viewPage(request, pk):
    
    itemGet = blogDetail.objects.get(id = pk)
    itemGet.like+=2
    itemGet.save()
    print(itemGet.like)
    
    con = {
        'itemGet':itemGet
    }
    return render(request, "html/view.html",con)
def edit(request, pk):
    itemGet = blogDetail.objects.get(id = pk)
    alldetail_create = detailMoldelForm(instance=itemGet)
    if request.method == "POST":
        alldetail_create = detailMoldelForm(request.POST, request.FILES,instance=itemGet)
        if alldetail_create.is_valid():
            alldetail_create.save()
            return redirect('adminView', pk = request.user.id)

    

    con = {
        'form':alldetail_create
        
    }
    return render(request, "html/adminCreate.html",con)
def delete(request, pk):
    itemGet = blogDetail.objects.get(id = pk)
    itemGet.delete()
    return redirect('adminView', pk = request.user.id)
    