from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from Authentication.models import User, PayGrade, Department


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'mobile', 'age', 'role', 'department', 'pay_grade',
            'is_admin')


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'mobile', 'role', 'department', 'pay_grade', 'is_admin')


class PayGradeForm(ModelForm):
    class Meta:
        model = PayGrade
        fields = '__all__'


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
