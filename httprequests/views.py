from django.shortcuts import render

class Avatar:
    def __init__(self, number, name):
        self.number = number
        self.name = name
    def __str__(self):
        return self.name+"'s favourite number is "+self.number
    
def home(request):
    return render(request, 'httprequests/home.html')

def hello(request):
    the_name = request.GET.get('name')
    the_number = request.GET.get('number')
    ava = Avatar(the_number, the_name)
    return render(request, 'httprequests/hello.html', {'name':ava})