from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest, JsonResponse
from .models import Worker
from django.views import View
from .forms import AddWorkerForm
# Create your views here.

class Home(View):
    def get(self, request):
        worker_data = Worker.objects.all()
        return render(request, 'core/home.html', {'workerData':worker_data})
    
class Add_Worker(View):
    def get(self, request):
        fm = AddWorkerForm()
        return render(request, 'core/add_worker.html', {'form':fm})
    def post(self, request):
        
        fm = AddWorkerForm(request.POST)
        if fm.is_valid():
            fm.save()
            return JsonResponse({'success': True}) 
        else:
            return JsonResponse({'success': False, 'errors': fm.errors})

        
class Edit_Wroker(View):
    def get(self, request, id):
        worker_data = Worker.objects.get(id=id)
        fm = AddWorkerForm(instance=worker_data)
        return render(request, 'core/edit_worker.html', {'form':fm, 'id':id})
    
    def post(self, request,id):
        worker_data = Worker.objects.get(id=id)
        fm = AddWorkerForm(request.POST, instance=worker_data)
        if fm.is_valid():
            fm.save()
            return JsonResponse({'success': True}) 
        else:
            return JsonResponse({'success': False, 'errors': fm.errors})
         
class Delete_Worker(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        worker = Worker.objects.get(id=id)
        worker.delete()
        return redirect('/')