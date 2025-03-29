from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('childrecord/', TemplateView.as_view(template_name='childrecord.html'), name='childrecord'),
    path('registerchild/', TemplateView.as_view(template_name='registerchild.html'), name='registerchild'),
    path('medication/', views.medication_view, name='medication'),
    path('illness/', views.illness_list, name='illness_list'),
    path('appointment/', views.appointment_list, name='appointment_list'),
    path('immunization/', views.immunization_list, name='immunization_list'),
    path('medic/', views.medic, name='medic'),
    path('growth_data/', views.growth_data, name='growth_data'),
    path('changeuser/', views.change_user, name='changeuser'),
    path('medication-list/', views.medication_list, name='medication_list'),
    path('growth-record/', views.growth_record, name='growth_record'),
    path('change-username/', views.change_username, name='change_username'),
    path('change-email/', views.change_email, name='change_email'),
    path('change-password/', views.change_password, name='change_password'),
]