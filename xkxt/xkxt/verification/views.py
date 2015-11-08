from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def get_group_name(user):

      if not user:
          return ""
      name = user.groups.values()[0]["name"]
      return name

def is_in_group(user,g_name):
    if not user:
        return False
    for _,name in user.groups.values():
        if name==g_name:
            return True
    return False

def login(request):
    if request.user.is_authenticated():
        if "groupname" not in request.session:
              request.session["groupname"] = get_group_name(request.user)
        print  request.session["groupname"]
        return HttpResponseRedirect('/main/',content_type=RequestContext(request))
    if "username" not in request.POST:
        return render_to_response('account/login.html',context_instance=RequestContext(request))
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        request.session["groupname"] = get_group_name(user)
        print  request.session["groupname"]
        return HttpResponseRedirect('/main/',content_type=RequestContext(request))
    else:
        return render_to_response('account/login.html',{"loginerror":True},context_instance=RequestContext(request))

def logout(request):
      auth.logout(request)
      return render_to_response('account/logout.html',context_instance=RequestContext(request))
