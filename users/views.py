from django.shortcuts import render
from django.contrib.auth import login, authenticate
from users.forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def home(request):

    return render(request, 'home.html')


def dashboard(request):

    return render(request, 'dashboard/dashboard.html')

# def signup(request):
#     form = UserCreationForm()
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             '''redirects user to home page after login'''
#             return redirect('dashboard')
#         else:
#             form = UserCreationForm()
#     return render(request, 'users/signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				print(f'welcome {username}')
				return redirect("dashboard")
			else:
				print('invalid username or password')
		else:
			print('invalid username or password')
	form = AuthenticationForm()
	return render(request, 'users/login.html',{'form':form})
