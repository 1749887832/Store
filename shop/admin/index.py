from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render


class Index:
    def __init__(self):
        super().__init__()
        self.user = None

    @login_required
    def toIndex(self):
        user = User.objects.get(id=self.user.id)
        context = dict()
        context['date'] = user
        return render(self, 'main.html', context)
