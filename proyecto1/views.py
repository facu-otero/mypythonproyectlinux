from django.http import HttpResponse

def saluda(req):
    
    return HttpResponse("Hi! World")