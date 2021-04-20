from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1><a href="https://www.google.com"target="_blank">Open Google</a></h1><h1><a href="https://www.facebook.com"target="_blank">Open Facebook</a></h1><h1><a href="https://www.gmail.com">Open Gmail</a></h1><h1><a href="https://www.yahoo.com">Open yahoo</a></h1>')