from django.urls import path
from . import views
from . import streamlit_a_propos  # Importez votre script Streamlit

urlpatterns = [
    path('', views.index, name='index'),
    path('streamlit/', streamlit_a_propos.main, name='streamlit_a_propos'),  # Ajoutez cette ligne
]
