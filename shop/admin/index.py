from django.shortcuts import render


class Index:
    def __init__(self):
        super().__init__()

    def toIndex(self):
        return render(self, 'main.html')
