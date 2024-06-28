# views.py

from django.shortcuts import render
import subprocess

def index(request):
    if request.path == '/streamlit/':
        try:
            subprocess.Popen(["streamlit", "run", "E:/Projets/Demoapp/a_propos/streamlit_a_propos.py"])
        except FileNotFoundError:
            raise FileNotFoundError("Streamlit n'est pas installé ou le chemin d'accès est incorrect.")
        return render(request, 'a_propos/index.html')
    return render(request, 'a_propos/index.html')
