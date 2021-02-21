from django.shortcuts import render


# Create your views here.
class Login:
    def __init__(self):
        self.POST = None

    def login(self):
        return render(self, 'login.html')

    def uLogin(self):
        username = self.POST.get('username')
        password = self.POST.get('password')
        print(username, password)
        return render(self, 'login.html')
