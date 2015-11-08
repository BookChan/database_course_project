#coding=utf8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def main(request):
      g_name = request.session.get("groupname","")
      print g_name
      if g_name==u"学生":
          return render_to_response("student/main.html",\
        {"username":request.user.username})
      elif  g_name==u"教师":
        return render_to_response("teacher/main.html",\
        {"username":request.user.username})
      else:
          return HttpResponseRedirect('/admin/',content_type=RequestContext(request))


def index(request):
      return HttpResponseRedirect('/accounts/login',content_type=RequestContext(request))

