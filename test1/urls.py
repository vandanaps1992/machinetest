from django.urls import path
from .import views
urlpatterns = [
    path('',views.loginform,name='loginform'),
    path('registration',views.registrationform,name='registrationform'),
    path('survey',views.surveyform,name='surveyform'),
    

]