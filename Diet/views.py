from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Food
from .forms import FoodForm, UserRegistrationForm, UserLoginForm


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'წარმატებით შეხვედით')
                return redirect('home')
            else:
                messages.error(request, 'არასწორი პაროლი ან სახელი')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})




def home(request):
    if request.method == 'POST':
        filter_date = request.POST.get('filter_date')
        filter_hour = request.POST.get('filter_hour')

        filtered_foods = Food.objects.filter(date_of_reception__date=filter_date, date_of_reception__hour=filter_hour)

        return render(request, 'home.html', {'foods': filtered_foods})
    else:
        all_foods = Food.objects.all()
        return render(request, 'home.html', {'foods': all_foods})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'უკვე არსებობს.სხვა სცადეთ')
        elif password != confirm_password:
            messages.error(request, 'პაროლი არ ემთხვევა')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            messages.success(request, 'რეგისტრაცია წარმატებულია')
            return redirect('home')
    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'წარმატებით შეხვედით')
            return redirect('home')
        else:
            messages.error(request, 'არასწორი პაროლი ან სახელი')

    return render(request, 'login.html')


def view_food(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    return render(request, 'food.html', {'food': food})


def edit_food(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FoodForm(instance=food)

    return render(request, 'edit_food.html', {'form': form, 'food': food})


def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FoodForm()

    return render(request, 'add_food.html', {'form': form})
