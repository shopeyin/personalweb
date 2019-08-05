from django.shortcuts import render
from django.http import JsonResponse
from personal.models import Contactus
from personal.forms import CreateMsgForm







def about_views(request):
    context = {}
    return render(request,'personal/about.html', context)




def home_views(request):
    context ={}
    return render(request,'personal/home.html',context)




def contactus_views(request):
    context = {}

    if request.is_ajax():
        form=CreateMsgForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user=request.user
            instance.save()
            data = {
               'message' : 'You will be contacted shortly'
            }
            return JsonResponse(data)
        else:
            data = {
                'message' : 'invalid email address'
            }
        return JsonResponse(data)
        context['contactus_form'] = form
    return render(request,'personal/hom.html',context)

