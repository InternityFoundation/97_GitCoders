from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
User = get_user_model()
class UsernameOrEmailBackend(object):
    def authenticate(self,request, username=None, password=None):
        try:
           # Try to fetch the user by searching the username or email field
#            user = User.objects.get(Q(email=username))
            user = User.objects.get(Q(mobile=username)|Q(email=username))
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        except:
            return None
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
#            User().set_password(password)

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
