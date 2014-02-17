from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, Template
from api_client import get_full_url

# Create your views here.
def index(request):
        template = loader.get_template('shortener_home.html')
        return HttpResponse(template.render(Context(None)))

def redirect_user_to_page(request,short_hash):
    short_url_accessed = request.get_full_path()
    shortened_url = get_full_url(short_hash)
    if (shortened_url):
        return HttpResponseRedirect("http://"+shortened_url)
    else:
        return HttpResponse("{error:URL does not exist")
    
    