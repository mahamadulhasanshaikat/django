from django.http import HttpResponse

# Create your views here.
def home(response):
    return HttpResponse("Blog Home Page")

def about(request):
    return HttpResponse('Blog About Page')

