from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('childrecord/', views.child_record, name='childrecord'),
    path('registerchild/', views.register_child, name='registerchild'),
    path('immunization/', views.immunization_list, name='immunization_list'),
    path('medic/', views.medic, name='medic'),
    path('growth_data/', views.growth_data, name='growth_data'),
    path('growth_data/<int:child_id>/', views.growth_data, name='growth_data'),
    path('changeuser/', views.change_user, name='changeuser'),
    path('growth-record/', views.growth_record, name='growth_record'),
    path('growth-record/<int:child_id>/', views.growth_record, name='growth_record_child'),
    path('change-username/', views.change_username, name='change_username'),
    path('change-email/', views.change_email, name='change_email'),
    path('change-password/', views.change_password, name='change_password'),
    path('register/', views.register, name='register'),
    path('edit_child/', views.edit_child, name='edit_child'),
    path('dental-record/<int:child_id>/', views.dental_record_view, name='dental_record'),
    path("medication_list/", views.medication_list, name="medication_list"),
    path('medication_list/<int:child_id>/', views.medication_list, name='child_medication_list'),
    path('illness_list/', views.illness_list, name='illness_list'),
    path('illness_list/<int:child_id>/', views.illness_list, name='child_illness_list'),
    path('appointment_list/', views.appointment_list, name='appointment_list'),
]