
from django.http import HttpResponse, JsonResponse
from django import forms
from django.shortcuts import render
from todo_app.models import Todo
from django.conf import settings
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

class TodoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        user_model = get_user_model()
        user_choices = ((user.id, user.username) for user in user_model.objects.all())

        self.fields['author'].choices = user_choices

    author = forms.ChoiceField(required=True)
    title = forms.CharField(required=True, max_length=255)
    completed = forms.BooleanField(required=False, initial=False)

@csrf_exempt
def todo_view(request):
    context = {"form": TodoForm(), "todos": Todo.objects.all()}

    if request.method == "POST":
        print(request.POST)
        form = TodoForm(request.POST)
        
        if form.is_valid():
            author_id = form.cleaned_data.pop("author")
            user_model = get_user_model()
            author = user_model.objects.get(pk=author_id)

            Todo.objects.create(author=author, **form.cleaned_data)
            return render(request, 'index.html', context)

    return render(request, 'index.html', context)

def users(request):

    users = get_user_model().objects.all().values("id", "username")
    return JsonResponse(list(users), safe=False)
