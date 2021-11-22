from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from Authentication.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'mobile', 'age', 'role', 'department', 'pay_grade', 'is_admin')


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'mobile', 'role', 'department', 'pay_grade', 'is_admin')
