from django.urls import path, include
from Main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
    path('career/', views.career, name='career'),
    path('career/<slug:slug>/', views.career_detail, name='career_detail'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),


    path('automation-testing/', views.automation, name='automation'),
    path('functional-Testing/', views.functional, name='functional'),
    path('performance-Testing/', views.performance, name='performance'),
    path('application-Testing/', views.application, name='application'),
    path('cloud-testing/', views.cloud, name='cloud'),
    path('mobile-app-testing/', views.mobile, name='mobile'),
    path('data-analytics-testing/', views.data, name='data'),
    path('cx-testing/', views.cx, name='cx'),
    path('game-testing/', views.game, name='game'),
    path('integration-and-testing/', views.integration, name='integration'),
    path('iot-testing/', views.iot, name='iot'),
    path('devops/', views.devops, name='devops'),
    path('sales/', views.sales, name='sales'),
    path('rpa/', views.rpa, name='rpa'),
    path('accessibility/', views.accessibility, name='accessibility'),
]