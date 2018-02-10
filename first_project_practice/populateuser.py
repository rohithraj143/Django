import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project_practice.settings")

import django
django.setup()

from first_project_app.models import User
from faker import Faker

fakegen = Faker()

def populateUser(N=5):
    for user in range(N):
        fakename = fakegen.name().split()
        fake_first_name = fakename[0]
        fake_last_name = fakename[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_first_name,
                                          last_name=fake_last_name,
                                          email=fake_email)[0]

if __name__=='__main__':
    print('populating user date')
    populateUser(20)
    print('populating user data complete')
