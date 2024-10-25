from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_superuser

# @login_required
# @user_passes_test(is_admin)
# @require_GET
def get_users(request):
    users = User.objects.all().values('id', 'username', 'email','date_joined')
    users_list = list(users)
    return JsonResponse(users_list, safe=False)
