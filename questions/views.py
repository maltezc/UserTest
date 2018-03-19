from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404
import requests
from django.utils import timezone
from django.shortcuts import redirect


from .forms import QuestionForm
from .models import Question

# Create your views here.
from . import models
from .forms import QuestionForm
# from braces.views import SelectRelatedMixin

from django.contrib.auth import get_user_model
User = get_user_model()

#views go here

class QuestionList(generic.ListView):
    # ^ took out SelectRelatedMixin, replace when ready
    model = models.Question


class CreateQuestion(generic.CreateView):
    model = models.Question
    # model = models.Answer
    form = QuestionForm
    fields = ('question', 'answer')
    success_url = reverse_lazy('questions:all')


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class QuestionDetail(generic.DetailView):
    model = models.Question
    # template_name = 'questions/question_detail.html'


class QuestionUpdate(generic.UpdateView):
    model = models.Question
    form_class = QuestionForm
    # context_object_name = 'question'
    # success_url = reverse_lazy('questions:single')
    # fields = ('question', 'answer')
    # template_name_suffix = '_form'




class QuestionDelete(generic.DeleteView):
    model = models.Question
    success_url = reverse_lazy('questions:all')

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Question Deleted")
        return super().delete(*args, **kwargs)