 
python manage.py loaddata plant.json

python manage.py loaddata disease.json

python manage.py createsuperuser

from user.models import *
a = User.objects.first()
a.is_staff = True
a.is_active = True
a.save()
