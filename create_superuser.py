import os
import django
from django.contrib.auth import get_user_model

# Configure o ambiente Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "loja.settings")
django.setup()

# Defina os detalhes do superusuário
User = get_user_model()
username = 'admin'
email = 'admin@gmail.com'
password = '1234'

# Criação do superusuário
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superusuário criado com sucesso!")
else:
    print("Superusuário já existe.")
