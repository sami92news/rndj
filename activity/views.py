from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response

from activity import methods
# from activity.forms import StudentCreateForm
from activity.models import Student


def hi(request):
    return HttpResponse('yes')


class RestTesView(APIView):
    @never_cache
    def get(self, request):
        time_now = methods.now_str('%Y-%m-%d %H:%M:%S')
        res = {'now': time_now, 'more': 2}
        return Response(res)


class StudentDetail(DetailView):
    model = Student
    template_name = 'student_detail.html'

    def get(self, request, *args, **kwargs):
        test = 1
        if request.META['HTTP_SEC_FETCH_MODE'] == 'cors' or test:
            values = Student.objects.filter(id=kwargs['pk']).values()
            data = {}
            if len(values):
                data = values[0]
            res = {'status': 'success', 'data': data}
            res = JsonResponse(res)
            return res
        context = super().get(request, args, kwargs)
        return context


class StudentList(ListView):
    model = Student
    template_name = 'student_list.html'

    def get(self, request, *args, **kwargs):
        context = super().get(request, args, kwargs)
        test = 1
        if request.META['HTTP_SEC_FETCH_MODE'] == 'cors' or test:
            values = list(context.context_data['object_list'].values())
            a = 1
            for val in values:
                val['id'] = str(val['id'])
            res = {'status': 'success', 'data': values}
            res = JsonResponse(res)
            return res
        return context


class StudentCreate(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        data = {}
        for key in request.data:
            if key != 'encoding':
                data[key] = request.data[key]
        obj = Student(**data)
        obj.save()
        res = {'status': 'error', 'data': 'Could not save'}
        if obj.id:
            res = {'status': 'success', 'data': ''}
        return JsonResponse(res)


class StudentUpdate(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        data = {}
        for key in request.data:
            if key != 'encoding':
                data[key] = request.data[key]
        res = {'status': 'error', 'data': 'Could not save'}
        if not data.get('key'):
            res['data'] = 'No if given'
        else:
            obj = Student(**data)
            obj.save()
            res = {'status': 'success', 'data': ''}
        return JsonResponse(res)


class StudentCreate1(CreateView):
    model = Student
    template_name = 'student_form.html'
    fields = ('student_name', 'student_phone_number', 'student_email')
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()

    def post(self, request, *args, **kwargs):
        context = super().post(request, args, kwargs)
        return context


class StudentDelete(DeleteView):
    model = Student
    template_name = 'student_form.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        context = super().post(request, args, kwargs)
        test = 1
        if request.META['HTTP_SEC_FETCH_MODE'] == 'cors' or test:
            res = {'status': 'success', 'data': ''}
            res = JsonResponse(res)
            return res
        return context