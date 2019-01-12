from django.contrib.auth.models import User

from user_details.models import UserDetails


def create_test_user_and_user_details(username, password):
    """ Quick method for creating Django User to login in App """
    user, created = User.objects.get_or_create(username=username)
    user.set_password(password)
    user.save()

    details, _ = UserDetails.objects.get_or_create(user=user)
    return user, details
