from django.shortcuts import render, redirect

from .forms import UserForm, LoginForm
from .models import UserDetails
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def user_register(request):
    form = UserForm()
    if request.method == 'POST':
        print(request)
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            print("form is valid")
            if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                print("both passwords are same")
                form.cleaned_data.pop('confirm_password')
                emp = UserDetails(**form.cleaned_data)
                emp.save()
                return redirect('login')
            else:
                print("passwords are different")


    return render(request, 'accounts/register.html', context = {'form': form})


from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import UserDetails

def login_view(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            try:
                emp = UserDetails.objects.get(
                    email=form.cleaned_data['email']
                )

                if emp.check_password_User(
                    form.cleaned_data['password']
                ):

                    request.session['User_id'] = emp.id
                    request.session['email'] = emp.email

                    return redirect('products:ecommercehome')

                else:
                    print("password not matched")

            except UserDetails.DoesNotExist:
                print("User not found")

    return render(request, 'accounts/login.html', {'form': form})

def home_view(request):

    if 'User_id' not in request.session:
        return redirect('login')

    return render(request, 'base.html')


# session topic:
# saving user information for some days, so users dont need to login again and again

def set_session(request):
    request.session['email'] = 'vardhanguru770@gmail.com'
    request.session['username'] = 'vardhanguru'

    return render(request, 'accounts/set.html')

def home(request):
    print(request.session.get('email'))
    return render(request, 'accounts/home.html')

# how to delete the session data, you can use del
def delete_session(request):
    request.session.flush()

    return render(request, 'accounts/delete.html')