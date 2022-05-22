from django.views.generic import UpdateView, DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic.base import TemplateView
# import model
from .models import Profile
from question.models import Question
from article.models import Article
from data_library.models import DataLibrary
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Q
from PIL import Image

User = get_user_model()


class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    pagenate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        profile_keyword = self.request.GET.get('profile_search')
        if profile_keyword:
            queryset = Profile.objects.filter(
                Q(user__username__icontains=profile_keyword))
        else:
            queryset = Profile.objects.all()
        return queryset


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Profile.objects.get(pk=pk)
        if self.request.user.user.pk != pk:
            return redirect('article:list')
        return view_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_object()
        my_profile = Profile.objects.get(user=self.request.user)
        if view_profile.user in my_profile.following.all():
            follow = True
        else:
            follow = False
        context["follow"] = follow
        # ログイン中のユーザーのフォロー情報を取得
        login_user_follow_count = my_profile.following.all().count()
        login_user_follower_count = my_profile.follower.all().count()
        context["login_user_follow_count"] = login_user_follow_count
        context["login_user_follower_count"] = login_user_follower_count
        questions = Question.objects.filter(contributor=self.request.user)
        context['questions'] = questions
        # filter published article
        published_articles = Article.objects.filter(
            author=self.request.user, is_published=True)
        context['published_articles'] = published_articles
        draft_articles = Article.objects.filter(
            author=self.request.user, is_published=False)
        context['draft_articles'] = draft_articles
        # get datalibrary's data user posted
        posted_data = DataLibrary.objects.filter(uploader=self.request.user)
        context['data_libraries'] = posted_data
        return context


class OtherUserProfileView(DetailView):
    model = Profile
    template_name = 'profiles/otheruser_profile.html'

    def get_objects(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Profile.objects.get(pk=pk)
        return view_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_object()
        my_profile = Profile.objects.get(user=self.request.user)
        if view_profile.user in my_profile.following.all():
            follow = True
        else:
            follow = False
        context["follow"] = follow
        # ログイン中のユーザーのフォロー情報を取得
        login_user_follow_count = view_profile.following.all().count()
        login_user_follower_count = view_profile.follower.all().count()
        context["login_user_follow_count"] = login_user_follow_count
        context["login_user_follower_count"] = login_user_follower_count
        # Get viewing profile's article
        article_object = Article.objects.filter(
            author=view_profile.user, is_published=True)
        context['articles'] = article_object
        # get datalibrary's data user posted
        posted_data = DataLibrary.objects.filter(uploader=view_profile.user)
        context['data_libraries'] = posted_data
        return context


class UserProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/create_userprofile.html'

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        # crop image
        cropping_image = Image.open(profile.icon)
        width, height = cropping_image.size
        crop_size = height
        cropped_image = cropping_image.crop(
            ((width - crop_size) // 2, (height - crop_size) // 2, (width + crop_size) // 2, (height + crop_size) // 2))
        cropped_image.save(profile.icon.path)
        messages.success(self.request, "プロフィールの作成に成功しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "プロフィールの作成に失敗しました")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('article:list')


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profiles/profile_update.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy('article:list')

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.save()
        # crop image
        cropping_image = Image.open(profile.icon)
        width, height = cropping_image.size
        crop_size = height
        cropped_image = cropping_image.crop(
            ((width - crop_size) // 2, (height - crop_size) // 2, (width + crop_size) // 2, (height + crop_size) // 2))
        cropped_image.save(profile.icon.path)
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
        follower_list = my_profile.following.all()
        # this process will add user to following
        if obj.user in follower_list:
            my_profile.following.remove(obj.user)
        else:
            my_profile.following.add(obj.user)
        # this process will add user to follower
        following_list = obj.follower.all()
        if my_profile.user in following_list:
            obj.follower.remove(my_profile.user)
        else:
            obj.follower.add(my_profile.user)

        return redirect('profiles:profile_list')
    return redirect('profiles:profile_list')

"""
if user have an account but haven't made profile -> profile_make
if user haven't accout -> registration create
"""
def profile_not_found(request):
    try:
        if Profile.objects.filter(user=request.user).exists():
            user = Profile.objects.get(user=request.user)
            pk = user.pk
            return redirect('profiles:profile_detail', pk=pk)
        
        else:
            return redirect('profiles:profile_create')
    
    except:
        return redirect('registration:sign_up')

"""
we will display follower and following user

FollowerListView -> display who you are follow
FollowingListView -> display who you are following

we are going to make the system to see another user's follower
"""
class FollowerListView(LoginRequiredMixin, ListView): 
    model = Profile
    template_name = "profiles/follower_list.html"
    pagenate_by = 20
    context_object_name = 'follower_list'

    def get_queryset(self):
        queryset = super().get_queryset() 
        queryset = Profile.objects.filter(following = self.request.user)
        return queryset

class FollowingListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = "profiles/following_list.html"
    pagenate_by = 20
    context_object_name = 'following_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Profile.objects.filter(follower = self.request.user)
        return queryset