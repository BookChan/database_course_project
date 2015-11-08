from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def course_query(request):
    return render_to_response("course/course.html",\
        {"username":request.user.username})

@login_required
def mycourse(request):
    return render_to_response("course/mycourse.html",\
        {"username":request.user.username})

@login_required
def mygrade(request):
    return render_to_response("course/mygrade.html",\
        {"username":request.user.username})

@login_required
def show_course(request):
    return render_to_response("course/course_item.html",\
        {"username":request.user.username})
