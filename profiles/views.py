from django.views.generic import UpdateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .models import Profile
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect

User = get_user_model()


class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'

    def get_queryset(self):
        return Profile.objects.exclude(user=self.request.user)


class UserProfileDetailView(DetailView, LoginRequiredMixin):
    template_name = 'profiles/profile_detail.html'
    model = Profile

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Profile.objects.get(pk=pk)
        return view_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_object()
        my_profile = Profile.objects.get(user=self.request.user)
        if view_profile in my_profile.following.all():
            follow = False
        else:
            follow = True
        context["follow"] = follow
        return context


class UserProfileUpdateView(UpdateView, LoginRequiredMixin):
    model = User
    template_name = 'profile/profile_update.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, 'プロフィールの編集に成功しました．')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'プロフィールの編集に失敗しました．')
        return super().form_invalid(form)


def follow_unfollow_view(request):
    if request.method == 'POST':
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)

        if obj.user in my_profile.following.user:
            my_profile.following.remove(obj.user)
        else:
            my_profile.following.add(obj.user)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('index')
