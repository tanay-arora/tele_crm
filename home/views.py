from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta


from home.models import *


def home_view(request):
    if request.method == 'POST':
        username = request.POST.get('your_name')
        password = request.POST.get('your_pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/') 
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

@login_required(login_url="/login")
def main_view(request):
    if request.method == 'POST':
        which_call = request.POST.get('which_call')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        alternate_phone = request.POST.get('alternate_phone')
        billing_address = request.POST.get('billing_address')
        member_of_family = request.POST.get('member_of_family')
        worth = request.POST.get('worth')
        followup = request.POST.get('followup')
        favourable_apps = request.POST.get('favourable_apps')

        print("Customer Details:")
        print("Which Call:", which_call)
        print("Name:", name)
        print("Email:", email)
        print("followup:",followup)
        print("Phone:", phone)
        print("Alternate Phone:", alternate_phone)
        print("Billing Address:", billing_address)
        print("Member of Family:", member_of_family)
        print("Worth:", worth)
        print("Favourable Apps:", favourable_apps)

        current_user = request.user
    
        customer = customer_detail(
            which_call=which_call,
            by_user = current_user,
            name=name,
            email=email,
            phone=phone,
            alternate_phone=alternate_phone,
            billing_address=billing_address,
            member_of_family=member_of_family,
            worth=worth,
            next_followup= followup,
            favourable_apps=favourable_apps,
        )
        customer.save()
        if followup:
            _reminder =reminders(for_user=current_user,time =followup,reminder="You have to call {}, call id {}, phone: {}, alternate phone {}, worth: {}".format(customer.name,customer.which_call,customer.phone,customer.alternate_phone,customer.worth))
            _reminder.save()

        return redirect("/")
    else:
        _note = notes.objects.filter(by_user=request.user).first()
        return render(request, 'customer_detail.html',{"notes":_note})

def save_content(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        user_id = request.POST.get('user_id', '')
        print(content)
        print(user_id)
        _note = notes.objects.filter(by_user=request.user).first()
        if not _note:
            _note = notes(by_user=request.user)
        
        _note.notepad = content
        _note.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
def get_reminders(request):
    if request.method == 'POST':
        current_time = timezone.now()
        reminder = reminders.objects.filter(for_user=request.user,time__lt=current_time)
        reminders_data = list(reminder.values('id', 'time','reminder'))

        return JsonResponse(reminders_data, safe=False)

@login_required(login_url="/login")
def customer_list(request):
    time_threshold = timezone.now() - timedelta(hours=24)
    customer_list = customer_detail.objects.filter(by_user=request.user, created_at__gte=time_threshold)
    
    return render(request, 'customer_list.html', {"customer_list": customer_list})