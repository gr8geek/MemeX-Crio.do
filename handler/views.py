from django.conf.urls import url
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MyModel
import ast
# Create your views here.
@csrf_exempt
def handle_api(request):
    if request.method == "POST":        
        print(type(request.body))
        value = request.body
        value = value.decode().replace("\'","\"")
        print(value)
        value = ast.literal_eval(value)
        print(value)
        print("Name: "+value["name"])
        print("URL: "+value["url"])
        print("Caption "+value["caption"])
        p = MyModel(owner = value["name"],caption =value["caption"],url = value["url"] )
        p.save()
        print(p)
        print()
        resp ={}
        resp["id"] = str(p.id)
        #print(value)
        return JsonResponse(resp)
    if request.method == "GET":
        print("-----INSIDE GET")
        all_memes = list(MyModel.objects.all())
        if(len(all_memes)<100):
            temp =[]
            for i in all_memes:
                resp = {}
                resp["id"] = str(i.id)
                resp["name"] = str(i.owner)
                resp["url"] = str(i.url)
                resp["caption"] = str(i.caption)
                temp.append(resp)
            return JsonResponse(temp,safe=False)
        all_memes = all_memes[len(all_memes)-100:len(all_memes)]
        temp =[]
        for i in all_memes:
            resp = {}
            resp["id"] = str(i.id)
            resp["name"] = str(i.owner)
            resp["url"] = str(i.url)
            resp["caption"] = str(i.caption)
            temp.append(resp)
        return JsonResponse(temp,safe=False)

   
def handle_id(request,id):
    print("Inside id funct", id)
    if request.method == "GET":
        res = list(MyModel.objects.filter(id = id))[0]
        resp = {}
        resp["id"] = str(res.id)
        resp["name"] = str(res.owner)
        resp["url"] = str(res.url)
        resp["caption"] = str(res.url)
        return JsonResponse(resp)
        #return HttpResponse("This is a HTTP request GET "+str(id))
    #return HttpResponse("THis is a response")
