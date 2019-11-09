import uuid
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
# from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from django.template.loader import render_to_string

User = get_user_model()

from .forms import (
    RegisterForm,
    UserProfileForm
)

from .models import (
    USER_TYPE,
    UserToken,
)
from django.views.generic.base import TemplateView

class ProfileEdit(TemplateView):
    '''
    View for the home page - home.html (main page)
    '''
    template_name = "dashboard/user-edit.html"

def login_page(request):
    if request.user.is_authenticated:
        # return HttpResponse("Home page redirect")
        return redirect('main:dashboard')
    else:
        return redirect('main:home')
        # return render(request, 'user/login.html')

def auth_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username,password=password) #here username can be email or phone number
    if user is not None:
        if user.is_active:
            login(request,user)
        else:
            return render(request,'error.html',{'message': 'Please activate your account.'})
        return redirect("main:dashboard")

        # return redirect('ui:home')
    else:
        return HttpResponse("invalid")

        # return redirect('user:invalid')

def invalid(request):
    display_message = "Invalid User!"
    return render(request, 'emptypage.html', {'img_error': 'invalid_user',
                                              'error_message': display_message,
                                              'button_text': 'Continue Shopping'})

def logout_user(request):
    logout(request)
    # return HttpResponse("Login")
    return redirect('main:home')

def activate(request, token):
    if token:
        token_obj = UserToken.objects.filter(token = token)
        if token_obj.exists():
            token_obj = token_obj.first()
            if token_obj.expire_date > datetime.now(token_obj.expire_date.tzinfo) and token_obj.active == False and token_obj.token_type == 1:
                user_obj = token_obj.user
                user_obj.is_active = True
                user_obj.save()
                token_obj.active = True
                token_obj.save()
                return HttpResponse("Now you can login your account.")
                # return render(request,'success.html',{'message': 'Thank you for your email confirmation. Now you can login your account.'})
        return HttpResponse("Invalid Token or Token Expired")

def register_user(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        user = form.save(commit=False)
        # to activate the user by defalut
        user.is_active = True
        user.save()
        token_obj = UserToken.objects.create(user = user, token = uuid.uuid1(), token_type =1)

        # current_site = get_current_site(request)
        # mail_subject = 'Activate your account.'
        # message = render_to_string('user/activation_email.html', {
        #         'user': user,
        #         'domain': current_site.domain,
        #         'token': token_obj.token,

        #     })
        # to_email = form.cleaned_data.get('email')
        # email = EmailMessage(
        #             mail_subject, message, to=[to_email]
        # )
        # email.send()
#        if user is not None:
#            login(request,user)

        # display_message = 'Thank you for creating your account. ' \
        #                   'Please activate your account by the link send to you on your email.'
        # return render(request, 'emptypage.html', {'img_error': 'email_sent',
        #                                           'error_message': display_message,
        #                                           'button_text': 'Continue Shopping'})



    return HttpResponse("Please register again.")
    # return render(request, "user/register.html",context)


@login_required(login_url='/user/login')
def profile(request):
    context={}
    context['user_obj'] = request.user
    return render(request,'user/profile/profile.html', context)


@login_required(login_url='/user/login')
def edit_profile(request):
    user_obj = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_obj)
        if form.is_valid():
            form.save()
        return redirect('user:profile')
    else:
        form = UserProfileForm(instance=user_obj)
        context = {
            'form': form,
        }
        return render(request, 'user/profile/edit_profile.html', context)
