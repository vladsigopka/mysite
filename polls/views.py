from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from .models import Person
from .forms import UserRegistrationForm
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic import UpdateView
from polls.models import Person
from polls.forms import PersonForm
from django.contrib.auth.forms import UserCreationForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'вы не сделали выбор'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def show_home(request):

        return render(request, 'catalog/index.html')


# Функция регистрации


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'catalog/register_done.html', {'new_user': new_user})
    else:
         user_form = UserRegistrationForm()
    return render(request, 'catalog/register.html', {'user_form': user_form})
def login(request):
    return render(request, 'catalog/login.html')
class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'job_title', 'bio')

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'catalog/person_update_form.html'


