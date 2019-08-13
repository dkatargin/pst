from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from . import models
from .forms import DataForm



@csrf_exempt
def post(request):
    form = DataForm()
    if request.method == 'POST':
        if not request.POST.get('data'):
            return render(request, 'index.html', {'form': form})
        obj = models.Post(data=request.POST.get('data'))
        obj.save()
        return redirect('/{}/'.format(obj.id))
    return render(request, 'index.html', {'form': form})


def get_post(request, *args, **kwargs):
    post_obj = models.Post.objects.filter(id=kwargs.get('post_id')).first()
    if not post_obj:
        return HttpResponseNotFound('Post not found')
    return render(request, 'data.html', {'data': post_obj.data})
