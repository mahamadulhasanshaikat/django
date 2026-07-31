from django.http import HttpResponse

# Create your views here.
def home(response):
    return HttpResponse("Shop Home Page")

def Products(request):
    return HttpResponse('Shop Products Page')

