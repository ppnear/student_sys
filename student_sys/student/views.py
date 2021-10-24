from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

# Create your views here.

from .models import Student
from .forms import StudentForm

# def index(request):
#     students = Student.get_all()
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         print(form)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('index'))       #reverse方法对应的是url中定义的name=index，拿到对应url
#     else:
#         form = StudentForm()
#     context = {
#         'students': students,
#         'form': form,
#     }
#     return render(request, 'index.html', context=context)


class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        context = {
            'students': students,
        }
        return context

    def get(self, request):
        context = self.get_context()
        form = StudentForm()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)


