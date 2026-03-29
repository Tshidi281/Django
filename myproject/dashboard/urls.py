from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('estatement/', views.view_estatement, name='view_estatement'),
    path('report-issue/', views.report_issue, name='report_issue'),
    path('how-do-i/', views.how_do_i, name='how_do_i'),
    path('contact-us/', views.contact_us, name='contact_us'),
]
