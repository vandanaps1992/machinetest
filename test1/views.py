from django.shortcuts import render

# Create your views here.
def loginform(request):
    return render(request,'loginform.html')

def registrationform(request):
    return render(request,'registrationform.html')


def surveyform(request):
    return render(request,'surveyform.html')