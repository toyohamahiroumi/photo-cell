from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import User


class MyUserChangeForm(UserChangeForm):
    # User情報を変更するフォーム
    class Meta:
        model = User
    # 全ての情報を変更可能
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    # Userを作成するフォーム
    class Meta:
        model = User
        fields = ('email',)


class MyUserAdmin(UserAdmin):
    # カスタムユーザーモデルのAdmin
    fieldsets = (
        (None, {'fields': ('email', 'username', 'icon')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
                                       'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, MyUserAdmin)
