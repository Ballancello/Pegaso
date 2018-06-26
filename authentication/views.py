import requests

from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages

from authtools.views import (
	LoginView as AuthLoginView, 
	LogoutView as AuthLogoutView, 
	PasswordResetView as AuthPasswordResetView,
	PasswordResetConfirmView as AuthPasswordResetConfirmView,
	PasswordResetCompleteView as AuthPasswordResetCompleteView
)

from .forms import RegisterForm, AuthenticationForm, PasswordResetForm, SetPasswordForm

# Create your views here.


class RegisterUserBigView(FormView):

	form_class = RegisterForm
	template_name = 'registration_view.html'
	# success_url = 
	# model = User 
	# fields = ['username', 'email', 'password1', 'password2']


	def form_invalid(self, form):
		form = self.form_class(self.request.POST)
		response = super(RegisterUserBigView, self).form_invalid(form)
		# This method is called when valid form data has been POSTed.
		# It should return an HttpResponse.
		# print(form)


		return response 


	def form_valid(self, form):
		# This method is called when valid form data has been POSTed.
		# It should return an HttpResponse.
		recaptcha_response = self.request.POST.get('g-recaptcha-response')
		data = {
			'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			'response': recaptcha_response
		}
		r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
		result = r.json()
		''' End reCAPTCHA validation '''

		#Recaptcha validationg 

		if result['success']:
			form.save()
			email = self.request.POST['email']
			password = self.request.POST['password1']
			user = authenticate(username=email, password=password)
			login(self.request, user)

			next = self.request.GET.get('next', '')
			print(next)

			return HttpResponseRedirect(reverse('home'))
		else:
			messages.error(self.request, 'Invalid reCAPTCHA. Please try again.')
			return HttpResponseRedirect(reverse('auth:register'))

		# return super(RegisterUserBigView, self).form_valid(form)

		


class LoginView(AuthLoginView):

	form_class = AuthenticationForm
	authentication_form = None
	template_name = 'login_view.html'
	allow_authenticated = True

	# BBB: This is deprecated (See LoginView.get_allow_authenticated)
	disallow_authenticated = None


class LogoutView(AuthLogoutView):
	pass




class PasswordResetView(AuthPasswordResetView):

	template_name = 'password_reset_view.html'
	success_url = reverse_lazy('auth:password_reset_done')
	form_class = PasswordResetForm
	email_template_name = 'password_reset_email.html'

class PasswordResetDoneView(TemplateView):

	template_name = 'password_reset_done_view.html'


class PasswordResetConfirmView(AuthPasswordResetConfirmView):

	template_name = 'password_reset_confirm_view.html'
	form_class = SetPasswordForm
	success_url = reverse_lazy('auth:password_reset_complete')
	post_reset_login = False
	post_reset_login_backend = None


class PasswordResetCompleteView(AuthPasswordResetCompleteView):

	template_name = 'password_reset_complete_view.html'



	

# class PasswordResetCompleteView(TemplateView):
# 	template_name = 'registration/password_reset_complete.html'
# 	login_url = settings.LOGIN_URL

# 	def get_login_url(self):
# 		return resolve_url(self.login_url)	

# 	def get_context_data(self, **kwargs):
# 		kwargs = super(PasswordResetCompleteView, self).get_context_data(**kwargs)
# 		kwargs['login_url'] = self.get_login_url()
# 		return kwargs
