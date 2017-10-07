from django.views.generic import DetailView
from .models import Diary


class DiaryDetailView(DetailView):
    model = Diary
