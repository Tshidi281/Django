from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    context = {
        'user': request.user
    }
    return render(request, 'dashboard/dashboard.html', context)

def view_estatement(request):
    return render(request, 'dashboard/estatement.html')

def report_issue(request):
    return render(request, 'dashboard/report_issue.html')

def how_do_i(request):
    return render(request, 'dashboard/how_do_i.html')

def contact_us(request):
    return render(request, 'dashboard/contact_us.html')
