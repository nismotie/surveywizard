from django.shortcuts import render
from django.http import HttpResponse
from .forms import MentorCall 


def mentor_call(request):
    if request.method == 'POST':
        form = MentorCall(request.POST) 

        if form.is_valid():
            return HttpResponse('Thank you for your response!')

    else:
        form = MentorCall() 

    context = {
            'title':'Mentor Call Report',
            'form':form
            }
    return render(request, 'surveys/mentor_calls.html', context=context)

# Create your views here.
