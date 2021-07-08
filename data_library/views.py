from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import DataLibrary, CommentToDataLibrary
from profiles.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import DataLibraryCreateForm


class DataLibraryCreateView(CreateView, LoginRequiredMixin):
    form_class = DataLibraryCreateForm
    model = DataLibrary
    template_name = 'data_library/create.html'
    success_url = reverse_lazy('data_library:list')

    def form_valid(self, form):
        data_library = form.save(commit=False)
        data_library.uploader = self.request.user
        data_library.save()
        return super().form_valid(form)


class DataLibraryUpdateView(UpdateView, LoginRequiredMixin):
    form_class = DataLibraryCreateForm
    model = DataLibrary
    template_name = 'data_library/update.html'
    success_url = reverse_lazy('data_library:list')


class DataLibraryListView(ListView, LoginRequiredMixin):
    model = DataLibrary
    template_name = 'data_library/list.html'
    pagenate_by = 20

    def get_queryset(self):
        data_libraries = DataLibrary.objects.all().order_by('-created_at')
        return data_libraries


class DataLibraryDetailView(DetailView):
    model = DataLibrary
    template_name = 'data_library/detail.html'

    """
    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_data_library = DataLibrary.objects.get(pk=pk)
        return view_data_library
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # good function
        pk = self.kwargs.get('pk')
        data_object = DataLibrary.objects.get(pk=pk)
        evaluators = data_object.good.all()
        good_number = evaluators.count()
        context['good_number'] = good_number
        # comment function
        comment_list = CommentToDataLibrary.objects.filter(
            comment_to=data_object)
        context['comment_list'] = comment_list
        return context


def good_count(request):
    if request.method == 'POST':
        pk = request.POST.get('good_count')
        data_object = DataLibrary.objects.get(pk=pk)
        evaluator = request.user
        evaluators = data_object.good.all()
        if evaluator in evaluators:
            data_object.good.remove(evaluator)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            data_object.good.add(evaluator)
            return redirect(request.META.get('HTTP_REFERER'))
    return redirect('data_library:list')


def comment(request):
    if request.method == 'POST':
        # get data object
        data_object_pk = request.POST.get('data_object_pk')
        data_object = DataLibrary.objects.get(pk=data_object_pk)
        resopnse_from = request.user
        comment_content = request.POST.get('comment')
        # checkdata
        if not comment_content:
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            pass
        # saving process
        comment_to_data_library = CommentToDataLibrary()
        comment_to_data_library.comment_to = data_object
        comment_to_data_library.content = comment_content
        comment_to_data_library.comment_from = resopnse_from
        comment_to_data_library.save()
        return redirect('data_library:list')

    else:
        return redirect('data_library:list')
