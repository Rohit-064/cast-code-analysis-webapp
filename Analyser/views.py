# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from pylint import epylint as lint
import tinycss
from .utils import MyEncoder
import json

class TodoView(viewsets.ModelViewSet):
	serializer_class = TodoSerializer
	queryset = Todo.objects.all()

	def get(self, request):
		import ipdb;ipdb.set_trace()

class PollQuestions(View):
	title = "Questions"
	template = 'Analyser/templates/base.html'

	def get(self, request):
		questions = list(Todo.objects.all())

		context = {
		'title': self.title,
		'all_data': questions,
		}

		return render(request, self.template, context)


class code_analyser(View):
	file_dir = { "python":  "./Analyser/temp/temp.py"}
	remarks = ""
	context_dict = {}
	head_dict = {}
	body_dict = {}
	context_dict['head'] = head_dict
	context_dict['body'] = body_dict
	status, desc, errors = "", "", ""
	
	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(code_analyser, self).dispatch(*args, **kwargs)

	def get(self, request):
		result = {'apple': 'bank'}
		return JsonResponse(result)

	def post(self, request):

		try:
			#temp fix
			codestype = request.POST.get('codestype')

			if codestype == 'Python' and request.POST.get('codedata'):
				self.store_file()
				input_file = self.file_dir.get("python")				
				(pylint_stdout, pylint_stderr) = lint.py_run(input_file, return_std=True)

				self.remarks = pylint_stdout.getvalue()
				self.errors = pylint_stderr.getvalue()

			elif codestype == 'CSS' and request.POST.get('codedata'):
				parser = tinycss.make_parser('page3')
				self.remarks = "The file is valid"
				stylesheet = parser.parse_stylesheet_bytes(self.request.POST.get('codedata'))
				self.errors = MyEncoder().encode(stylesheet.errors)
				self.handle_status()

			else:
				self.context_dict['body']['errors'] = self.errors
				self.context_dict['body']['remarks'] = self.remarks
				self.context_dict['head']['status'] = 1
				self.context_dict['head']['description'] = "Please check the input and try again!"
				return JsonResponse(self.context_dict)

			if codestype not in ['Python', 'CSS']:
				self.status = 1
				self.desc = "File type not supported! only python and css are supported!"

			else:
				self.context_dict['body']['errors'] = self.errors
				self.context_dict['body']['remarks'] = self.remarks
				self.context_dict['head']['status'] = self.status
				self.context_dict['head']['description'] = self.desc

		except:
			self.context_dict['head']['status'] = 1
			self.context_dict['head']['description'] = "Error. Please check the input and try again"

		return JsonResponse(self.context_dict)


	def store_file(self):
		input_file = open(self.file_dir.get("python") , "w")
		input_file.write(self.request.POST.get('codedata'))
		input_file.close()


	def handle_status(self):

		if self.errors and self.errors != '[]':
			self.remarks = "The file is not valid"
			self.status = 1
			self.desc = "Error"

		else:
			self.status = 0
			self.desc = "Success"