from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib import messages
#from django.contrib.auth.decorators import user_passes_test
from event.models import Person
from django.core.mail import EmailMultiAlternatives
from django.core.mail.message import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import JsonResponse
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

'''@csrf_exempt
def payment_done(request):
    firstname = request.session.get('first_Name')
    lastname = request.session.get('last_Name')
    e_mail = request.session.get('email')
    num_of_Guests = request.session.get('number_of_Guests')
    name = firstname + " " + lastname
    the_user = Person.objects.filter(first_Name=firstname).filter(last_Name=lastname).filter(email=e_mail).filter(number_of_Guests=num_of_Guests).first()
    the_user.payment_complete = True
    the_user.save()
    msg = EmailMessage()
    msg.subject = "Ticket Purchase Confirmation - " + name
    msg.body = 'Dear ' + name +", \n \n Thank you for your interest in our gala night! On the day of the event, please bring the attached QR code – it can be digital or printed. We sincerely appreciate your support and look forward to seeing you there! \n \nSincerely,\nTASSEL SAS Chapter Team" 
    msg.from_email = "tasselsas@gmail.com"
    msg.to = [the_user.email]
    msg.attach_file("media/qrcodes/qr-"+str(the_user.userid)+".jpg")
    msg.send()
    return render(request, 'tickets/payment_done.html')'''
def payment_done(request):
    return render(request, 'tickets/payment_done.html')
    
'''@csrf_exempt
def payment_canceled(request):
    firstname = request.session.get('first_Name')
    lastname = request.session.get('last_Name')
    e_mail = request.session.get('email')
    num_of_Guests = request.session.get('number_of_Guests')
    name = firstname + " " + lastname
    the_user = Person.objects.filter(first_Name=firstname).filter(last_Name=lastname).filter(email=e_mail).filter(number_of_Guests=num_of_Guests).first()
    return render(request, 'tickets/payment_canceled.html')'''

def payment_process(request):
    '''firstname = request.session.get('first_Name')
    lastname = request.session.get('last_Name')
    e_mail = request.session.get('email')
    num_of_guests = request.session.get('number_of_Guests')
    user = Person.objects.filter(first_Name=firstname).filter(last_Name=lastname).filter(email=e_mail).filter(number_of_Guests=num_of_guests).first()
    amount = user.number_of_Guests * 100.00
    userid = user.userid
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': amount,
        'item_name': 'Tickets',
        'invoice': str(userid),
        'currency_code': 'SGD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_canceled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'tickets/payment_process.html', {'form': form})'''
    return render(request, 'tickets/payment_process.html')

def buy(request):
    if request.method=='POST':
        form=forms.Purchase(request.POST)
        if form.is_valid():
            form.save()
            '''request.session['first_Name']=form.cleaned_data.get('first_Name')
            request.session['last_Name']=form.cleaned_data.get('last_Name')
            request.session['email']=form.cleaned_data.get('email')
            request.session['number_of_Guests']=form.cleaned_data.get('number_of_Guests')'''
            name = form.cleaned_data.get('first_Name') + " " + form.cleaned_data.get('last_Name')
            email = EmailMessage()
            email.subject = "Ticket Purchase Confirmation - " + name
            email.body = form.cleaned_data.get('first_Name') + form.cleaned_data.get('last_Name') + " signed up"
            email.from_email = "tasselsas@gmail.com"
            email.to = ['kohei.sanno@gmail.com']
            email.send()
            return redirect(reverse('payment_process'))
    else:
        form=forms.Purchase()

    return render(request, 'tickets/buy.html', {'form': form})

'''@user_passes_test(lambda u: u.is_staff)
def profile(request, userid):
    the_user = get_object_or_404(Person, userid=userid)
    if request.method=='POST':
        the_user.attended = True
        the_user.save()
        return redirect('event-home')
    return render(request, 'tickets/profile.html', {'the_user': the_user})'''

'''def thankyou(request):
    return render(request, 'tickets/thankyou.html')'''

"""def change_attendence(request, user_id):
    the_user = get_object_or_404(Person, user_id=user_id)
    the_user.attended= True
    return redirect('event-home')"""



""""attended = request.GET.get('attended', False)
user_id = request.GET.get('user_id', False)
user = Person.objects.get(pk=user_id)
try:
    user.attended = attended
    user.save()
    return JsonResponse({"success": True})
except Exception as e:
    return JsonResponse({"success": False})
return JsonResponse(data)"""





"""    form.save()
    user = Person.objects.filter(first_name=form.cleaned_data.get('first_name')).filter(last_name=form.cleaned_data.get('last_name')).first()
    name=form.cleaned_data.get('first_name') + form.cleaned_data.get('last_name')
    messages.success(request, f'Payment completed for {name}')
    subject, from_email, to = 'Subject test1234', 'tasselsas@gmail.com', form.cleaned_data.get('email')
    html_content = render_to_string('tickets/mail_template.html', {'first_name':user.first_name, 'imagelink':user.qr_image})
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return redirect('thankyou')"""