from django.shortcuts import render

# Create your views here.

def loop(request):
    d={"Name":"Santak","age":23,"Hobbies":["cricket","football","f1"]}
    return render(request,"loop.html",context=d)

def condition(request):
    d={"Name":"Santak","age":23,"Hobbies":["cricket","football","f1"]}
    return render(request,"condition.html",context=d)
