from django.urls import path

from .views import IndexView, DadosJSONView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dado/', DadosJSONView.as_view(), name='dados'),
]
