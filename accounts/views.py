from django.shortcuts import render,redirect, get_object_or_404
from .forms import UserLoginForm, UserRegisterForm, UserChangeForm, UserChangePassForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

#reCaptcha
import urllib
import json
from core import settings

def user_register(request):
    ''' User register function

    use captcha 
    '''
    if request.method == 'POST' :
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            ## CAPTCHA ##########################
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response' : recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ## CAPTCHA ######################
            if result['success']:
                cd = form.cleaned_data
                user = User.objects.create_user( cd['email'], cd['password1'], cd['image'] ,cd['full_name'], cd['national_code'], cd['mobile'], cd['address'] )
                user.save()
                login(request, user)
                messages.success(request,'ثبت نام با موفقیت انجام شد','success')
                return redirect('doshop:home')         
            else:
                messages.error(request,'لطفا گزینه من ربات نیستم را ثبت نمایید','danger')
    else :
        form = UserRegisterForm()
    context = {
        'form' : form
    }
    return render(request,'accounts/register.html',context)

"""
def user_register(request):
    if request.method == 'POST' :
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user( cd['email'], cd['password1'], cd['full_name'], cd['national_code'], cd['mobile'], cd['address'] )
            user.save()
            login(request, user)
            messages.success(request,'ثبت نام با موفقیت انجام شد','success')
            return redirect('doshop:home')
    else :
        form = UserRegisterForm()
    context = {
        'form' : form
    }
    return render(request,'accounts/register.html',context)

"""

def user_login(request):
    next = request.GET.get('next')
    if request.method == 'POST' :
        form = UserLoginForm(request.POST)
        if form.is_valid():
            ## CAPTCHA ##########################
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response' : recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ## CAPTCHA ######################
            if result['success']:
                cd = form.cleaned_data
                user = authenticate(request, email=cd['email'], password=cd['password'])
                if user is not None :
                    login(request, user)
                    messages.success(request,'ورود با موفقیت انجام شد','success')
                    if next :
                        return redirect(next)
                    return redirect('doshop:home')
                else :
                    messages.success(request,'ایمیل یا رمز عبور صحیح نمی باشد','danger')
            else:
                messages.error(request,'لطفا گزینه من ربات نیستم را ثبت نمایید','danger')
    else :
        form = UserLoginForm()
    context = {
        'form' : form
    }
    return render (request,'accounts/login.html',context)

"""
def user_login(request):
    next = request.GET.get('next')
    if request.method == 'POST' :
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None :
                login(request, user)
                messages.success(request,'ورود با موفقیت انجام شد','success')
                if next :
                    return redirect(next)
                return redirect('doshop:home')
            else :
                messages.success(request,'ایمیل یا رمز عبور صحیح نمی باشد','danger')
    else :
        form = UserLoginForm()
    context = {
        'form' : form
    }
    return render (request,'accounts/login.html',context)
"""

@login_required
def user_logout(request):
    logout(request)
    messages.success(request,'شما با موفقیت از سیستم خارج شدید','success')
    return redirect('doshop:home')



@login_required
def user_edit(request):
    myid = request.user.id
    me = get_object_or_404(User, id = myid)
    if request.method =='POST':
        form = UserChangeForm(request.POST, request.FILES, instance=me)
        if form.is_valid():
            form.save()
            messages.success(request,'ویرایش مشخصات با موفقیت انجام شد','success')
            return redirect('accounts:user_profile')
    else :
        form = UserChangeForm(instance=me)
    context = {
        'form' : form
    }
    return render (request,'accounts/user_edit.html',context)



@login_required
def user_profile(request):
    user_id = request.user.id
    the_user = get_object_or_404(User, id = user_id)
    context = {
        'the_user' : the_user
    }
    return render(request,'accounts/user_profile.html', context)

    


@login_required
def user_change_pass(request):
    user_id = request.user.id
    the_user = get_object_or_404(User, id = user_id)
    if request.method == 'POST' :
        form = UserChangePassForm(request.POST, instance=the_user)
        if form.is_valid():
            ## CAPTCHA ##########################
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response' : recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ## CAPTCHA ######################
            if result['success']:
                cp = form.cleaned_data['current_password']
                em = request.user.email
                user = authenticate(request, email=em, password=cp)
                if user is not None :
                    fm = form.save(commit=False)
                    fm.password1 = form.cleaned_data['password1']
                    fm.save()
                    login(request,the_user)
                    messages.success(request, 'رمز عبور با موفقیت تغییر کرد', 'success')
                    return redirect('accounts:user_profile')
                else :
                    messages.error(request,'رمز عبور فعلی خود را اشتباه وارد کرده اید','danger')
            else:
                messages.error(request,'لطفا گزینه من ربات نیستم را ثبت نمایید','danger')
    else:
        form = UserChangePassForm(instance = the_user)
    context = {'form': form}
    return render(request,'accounts/user_change_pass.html', context)


"""
@login_required
def user_change_pass(request):
    user_id = request.user.id
    the_user = get_object_or_404(User, id = user_id)
    if request.method == 'POST' :
        form = UserChangePassForm(request.POST, instance=the_user)
        if form.is_valid():
            ## CAPTCHA ##########################
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response' : recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ## CAPTCHA ######################
            if result['success']:
                fm = form.save(commit=False)
                fm.password1 = form.cleaned_data['password1']
                fm.save()
                login(request,the_user)
                messages.success(request, 'رمز عبور با موفقیت تغییر کرد', 'success')
                return redirect('accounts:user_profile')
            else:
                messages.error(request,'لطفا گزینه من ربات نیستم را ثبت نمایید','danger')
    else:
        form = UserChangePassForm(instance = the_user)
    context = {'form': form}
    return render(request,'accounts/user_change_pass.html', context)

"""

def list_api(request):
    return render(request,'accounts/list_api.html')




# ------------------------------------ #
# Reset Password # Forget Password

class UserPassReset(auth_views.PasswordResetView):
    template_name = 'accounts/password/password_reset_form.html'
    success_url = reverse_lazy('accounts:reset_pass_done')
    email_template_name = 'accounts/password/password_reset_email.html'


class UserPassResetDone(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password/password_reset_done.html'


class UserPassResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:reset_pass_complete')


class UserPassResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password/password_reset_complete.html'




