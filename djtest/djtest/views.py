# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template,Context,RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import json

#doc
#Cross Site Request Forgery protection https://docs.djangoproject.com/en/dev/ref/contrib/csrf/

def test(request):
  fp = open('djtest/test.html')  
  t = Template(fp.read())  
  fp.close()  
  html = t.render(Context({"id":1}))  
  print ".test. "
  return HttpResponse(html) 

def test2(request):
  fp = open('djtest/test2.html')  
  t = Template(fp.read())  
  fp.close()  
  html = t.render(Context({"id":1}))  
  print ".test. "
  return HttpResponse(html) 


    
def ajax(request):
  if request.is_ajax():
    print "----------- ajax processing -------------->"
    print request.GET  #pass args using "url: '/ajax?name=test',"
    my_response = {'ajax_resp':'Hello, webapp World!'}
    datos = json.dumps(my_response)
    return HttpResponse(datos, mimetype='application/json')
    #return HttpResponseRedirect('/test2') 
  else:
    print "----------- not ajax -------------->"
    return HttpResponse('it is not ajax.')
  


