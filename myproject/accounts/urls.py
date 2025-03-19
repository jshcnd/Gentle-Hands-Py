from django.urls import path
from .views import dashboard_view
from django.views.generic import TemplateView

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('childrecord/', TemplateView.as_view(template_name='childrecord.html'), name='childrecord'),
    path('registerchild/', TemplateView.as_view(template_name='registerchild.html'), name='registerchild'),
]