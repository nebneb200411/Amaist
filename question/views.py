from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CommentToQuestion, Question, QuestionTag
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import QuestionCreateForm


class QuestionCreateView(CreateView, LoginRequiredMixin):
    model = Question
    form_class = QuestionCreateForm
    template_name = 'question/create.html'
    success_url = reverse_lazy('question:list')

    def form_valid(self, form):
        question = form.save(commit=False)
        question.contributor = self.request.user
        question.save()
        pk = question.pk
        created_question = Question.objects.get(pk=pk)
        # tag saving process
        tags = self.request.POST.getlist('tags')
        tag_created = []
        for tag in tags:
            created_tag = QuestionTag.objects.create(tag_name=tag)
            created_tag.save()
            tag_created.append(created_tag)
        for tags in tag_created:
            created_question.tag.add(tags)
            created_question.save()
        return super().form_valid(form)


class QuestionListView(ListView):
    model = Question
    template_name = 'question/list.html'
    pagenate_by = 20
    order_by = '-created_at'


class QuestionDetailView(DetailView, LoginRequiredMixin):
    model = Question
    template_name = 'question/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # gain pk
        pk = self.kwargs.get('pk')
        context['pk'] = Question.objects.filter(pk=pk)
        # count good
        quetion = Question.objects.get(pk=pk)
        evaluators = quetion.good_from.all()
        good_number = evaluators.count()
        context['good_number'] = good_number
        # display comment
        comment_objects = CommentToQuestion.objects.filter(comment_to=quetion)
        context['comment_objects'] = comment_objects
        # Tagの取得
        tags = quetion.tag.all()
        context['tags'] = tags
        return context


def good_count(request):
    if request.method == 'POST':
        pk = request.POST.get('good_count')
        question = Question.objects.get(pk=pk)
        evaluator = request.user
        evaluators = question.good_from.all()
        if evaluator in evaluators:
            question.good_from.remove(evaluator)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            question.good_from.add(evaluator)
            return redirect(request.META.get('HTTP_REFERER'))
    return redirect('index')


# comment funvtion
def comment(request):
    if request.method == 'POST':
        # gain data
        question_pk = request.POST.get('question_pk')
        question = Question.objects.get(pk=question_pk)
        response_from = request.user
        comment_content = request.POST.get('comment')
        # check data
        if not comment_content:
            return redirect(request.META.get('HTTP_REFERER'))
        # save process
        comment = CommentToQuestion()
        if 'User' in request.POST.get('response_to'):
            response_to = request.POST.get('response_to')
            comment.response_to = response_to
        else:
            pass
        comment.comment_to = question
        comment.comment_from = response_from
        comment.content = comment_content
        comment.save()
        return redirect(request.META.get('HTTP_REFERER'))

    else:
        return redirect('index')
