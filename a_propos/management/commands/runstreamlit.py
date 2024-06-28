from django.core.management.base import BaseCommand
import subprocess

class Command(BaseCommand):
    help = 'Run Streamlit for a_propos'

    def handle(self, *args, **kwargs):
        subprocess.run(["streamlit", "run", "a_propos/streamlit_a_propos.py"])
