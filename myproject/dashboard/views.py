from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def dashboard(request):
    context = {
        'user': request.user
    }
    return render(request, 'dashboard/dashboard.html', context)

def view_estatement(request):
    # Sample statement data for university project
    statements = [
        {
            'id': 1,
            'date': '2026-03-01',
            'period': 'March 2026',
            'amount': 'R 2,450.00',
            'status': 'Paid',
            'type': 'Water Services'
        },
        {
            'id': 2,
            'date': '2026-02-01',
            'period': 'February 2026',
            'amount': 'R 2,100.00',
            'status': 'Paid',
            'type': 'Electricity Services'
        },
        {
            'id': 3,
            'date': '2026-01-01',
            'period': 'January 2026',
            'amount': 'R 1,980.00',
            'status': 'Paid',
            'type': 'Water Services'
        }
    ]
    
    return render(request, 'dashboard/estatement.html', {'statements': statements})

def report_issue(request):
    if request.method == 'POST':
        issue_type = request.POST.get('issue_type')
        description = request.POST.get('description')
        contact_info = request.POST.get('contact_info')
        
        # Simple validation
        if issue_type and description and contact_info:
            # Here you would normally save to database or send email
            # For university project, we'll just show success message
            messages.success(request, 'Your issue has been reported successfully. We will contact you soon.')
            return redirect('report_issue')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'dashboard/report_issue.html')

def how_do_i(request):
    faq_data = [
        {
            'id': 1,
            'question': 'How do I reset my password?',
            'answer': 'Click on "Forgot Password" link on login page and follow the instructions sent to your email.'
        },
        {
            'id': 2,
            'question': 'How do I update my contact information?',
            'answer': 'Navigate to your profile settings and update your details in the personal information section.'
        },
        {
            'id': 3,
            'question': 'How do I view my statements?',
            'answer': 'Click on "View E-Statement" from the dashboard menu to access your electronic statements.'
        },
        {
            'id': 4,
            'question': 'How do I report a problem?',
            'answer': 'Use the "Report an Issue" option from the dashboard menu to submit your concern.'
        }
    ]
    
    return render(request, 'dashboard/how_do_i.html', {'faq_data': faq_data})

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Simple validation
        if name and email and subject and message:
            # Here you would normally send email or save to database
            # For university project, we'll just show success message
            messages.success(request, f'Thank you {name}! Your message has been received.')
            return redirect('contact_us')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'dashboard/contact_us.html')
