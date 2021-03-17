from django.shortcuts import render,redirect
from .models import storage

def home(request):
    template = 'home.html'
    context = {}
    if request.method == 'POST':
        obj = storage()
        obj.url = request.POST['link']
        obj.save()
        context['thisisresult'] = True
        context['output'] = 'http://'+str(request.get_host())+'/s/'+str(obj.id)
    return render(request,template,context)

def goto_url(request,a):
    obj = storage.objects.get(pk=a)
    if obj.url.startswith('http://') or obj.url.startswith('https://'):
        return redirect(obj.url)
    else:
        return redirect('http://'+obj.url)