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
  return HttpResponse(html) 

    
def ajax(request):
  print "----------- ajax processing -------------->"
  my_response = {'ajax_resp':'Hello, webapp World!'}
  datos = json.dumps(my_response)
  return HttpResponse(datos, mimetype='application/json')    
  


