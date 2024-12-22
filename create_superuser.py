import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

User = get_user_model()

USERNAME = os.environ.get('DJANGO_SUPERUSER_USERNAME')
EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL')
PASSWORD = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

def create_superuser():
    if not User.objects.filter(username=USERNAME).exists():
        User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
        print(f"Superuser {USERNAME} created successfully")
    else:
        print(f"Superuser {USERNAME} already exists")

if __name__ == '__main__':
    create_superuser()