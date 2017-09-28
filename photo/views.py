from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Photo
from django.views.generic.dates import YearArchiveView
from django.views.generic import DetailView, ListView


def my_photo_redirect(request):
    last_photo = Photo.objects.latest('photo_at')
    year = last_photo.photo_at.year

    return HttpResponseRedirect(reverse('photo:list_year', args=(year, )))


class MyPhotoYearView(YearArchiveView):
    model = Photo
    date_field = 'photo_at'
    make_object_list = True
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(MyPhotoYearView, self).get_context_data(**kwargs)
        context['now_year'] = self.get_year()
        context['year_list'] = Photo.objects.dates('photo_at', 'year', order='DESC')
        return context


class MyPhotoDetailView(DetailView):
    model = Photo
