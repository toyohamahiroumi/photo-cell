from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, PhotoForm
from .models import Photo
# from django.views.generic.edit import CreateView, UpdateView
# from django.views.generic.detail import DetailView,
from django.views.generic import ListView, CreateView, UpdateView, DetailView, TemplateView
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views import generic
from users.models import User


# def index(request):
#     model = Post
#     template_name='posts/index.html'

#     return render(request, 'app/index.html')


# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             input_email = form.cleaned_data['email']
#             input_password = form.cleaned_data['password1']
#             new_user = authenticate(email=input_email, password=input_password)
#             if new_user is not None:
#                 login(request, new_user)
#                 return redirect('app:index')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'app/signup.html', {'form': form})

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'app/signup.html'

    def get_success_url(self):
        form = self.get_form()

        user = User.objects.get(username=form.data.get('username'))

        login(self.request, user)
        return reverse('app:userdetail',
                       kwargs={'username': user.username})


# アカウント詳細画面設定
class UserDetailView(DetailView):
    # template_name = 'app/user_detail.html'
    model = User
    # urlのパスクエリを引数に取る(後述)
    slug_field = 'username'
    slug_url_kwarg = 'username'
    # テンプレートに渡すデータにログイン中のユーザ情報を追加

    def get_context_data(self, **kywargs):
        context = super().get_context_data()
        context['login_user'] = self.request.user
        return context

# アイコン変更


class IconEdit(UpdateView):
    model = User
    template_name = 'app/icon_edit.html'
    fields = ['icon']

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        form = self.get_form()
        return reverse(
            'app:userdetail',
            kwargs={'username': self.request.user.username}
        )


class PhotoCreate(CreateView):
    template_name = 'app/photos_form.html'
    # model = Photo
    form_class = PhotoForm
    # fields = ['image', 'comment', 'tags', ]
    success_url = reverse_lazy('app:index')

    def form_valid(self, form):
        # バリデーションを通った時
        messages.success(self.request, "保存しました")
        form.instance.user_id = self.request.user.id
        return super(PhotoCreate, self).form_valid(form)

    def form_invalid(self, form):
        # バリデーションに失敗した時
        messages.warning(self.request, "保存できませんでした")
        return super().form_invalid(form)


class Index(ListView):
    model = Photo
    context_object_name = 'post_list'
    template_name = 'app/index.html'
    paginate_by = 100
    user = User.objects.
    queryset = Photo.objects.distinct('user').order_by('created_at')
