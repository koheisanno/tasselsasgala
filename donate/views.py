from django.shortcuts import render, redirect
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from donate.models import Donation, DonationCount
from . import donateform
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def donation_done(request):
    donationtype = request.session.get('donation_type')
    donation_id = request.session.get('donation_id')
    donation = Donation.objects.get(pk=donation_id)
    donation.complete = True
    if donationtype == 'item1':
        DonationCounter = DonationCount.objects.first()
        DonationCounter.item1 += donation.your_donation #should be AFTER IT REDIRECTS
        DonationCounter.general += donation.your_donation #should be AFTER IT REDIRECTS
        DonationCounter.save()
    elif donationtype == 'item2':
        DonationCounter = DonationCount.objects.first()
        DonationCounter.item2 += donation.your_donation #should be AFTER IT REDIRECTS
        DonationCounter.general += donation.your_donation #should be AFTER IT REDIRECTS
        DonationCounter.save()
    elif donationtype == 'item3':
        DonationCounter = DonationCount.objects.first()
        DonationCounter.item3 += donation.your_donation #should be AFTER IT REDIRECTS
        DonationCounter.general += donation.your_donation
        DonationCounter.save()
    elif donationtype == 'item4':
        DonationCounter = DonationCount.objects.first()
        DonationCounter.item4 += donation.your_donation #should be AFTER IT REDIRECTS
        DonationCounter.general += donation.your_donation
        DonationCounter.save()
    elif donationtype == 'general':
        DonationCounter = DonationCount.objects.first()
        DonationCounter.general += donation.your_donation #should be AFTER IT REDIRECTS
        DonationCounter.save()
    return redirect(reverse('donation'))

@csrf_exempt
def donation_canceled(request):
    return render(request, 'tickets/payment_canceled.html')

'''def payment_process(request):
    firstname = request.session.get('first_Name')
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

def donation(request):
    '''if request.method == 'POST':
        if 'item1' in request.POST:
            form=donateform.Donate(request.POST)
            if form.is_valid():
                request.session['donation_type']='item1'
                request.session['donation_num']=form.cleaned_data.get('number')
                donation=form.save()
                donation.donation_type='item1'
                donation_id=donation.pk
                donation.save()
                request.session['donation_id']=donation_id
                form_General=donateform.DonateGeneral()
                return redirect(reverse('donation_process'))
        elif 'item2' in request.POST:
            form=donateform.Donate(request.POST)
            if form.is_valid():
                request.session['donation_type']='item2'
                request.session['donation_num']=form.cleaned_data.get('number')
                donation=form.save()
                donation.donation_type='item2'
                donation_id=donation.pk
                donation.save()
                request.session['donation_id']=donation_id
                form_General=donateform.DonateGeneral()
                return redirect(reverse('donation_process'))
        elif 'item3' in request.POST:
            form=donateform.Donate(request.POST)
            if form.is_valid():
                request.session['donation_type']='item3'
                request.session['donation_num']=form.cleaned_data.get('number')
                donation=form.save()
                donation.donation_type='item3'
                donation_id=donation.pk
                donation.save()
                request.session['donation_id']=donation_id
                form_General=donateform.DonateGeneral()
                return redirect(reverse('donation_process'))
        elif 'item4' in request.POST:
            form=donateform.Donate(request.POST)
            if form.is_valid():
                request.session['donation_type']='item4'
                request.session['donation_num']=form.cleaned_data.get('number')
                donation=form.save()
                donation.donation_type='item4'
                donation_id=donation.pk
                donation.save()
                request.session['donation_id']=donation_id
                form_General=donateform.DonateGeneral()
                return redirect(reverse('donation_process'))
        elif 'generaldonations' in request.POST:
            form_General=donateform.DonateGeneral(request.POST)
            if form_General.is_valid():
                request.session['donation_type']='general'
                request.session['donation_amount']=form_General.cleaned_data.get('amount')
                donation=form_General.save()
                donation.donation_type='general'
                donation_id=donation.pk
                donation.save()
                request.session['donation_id']=donation_id
                form=donateform.Donate()
                return redirect(reverse('donation_process'))
        else:
            form=donateform.Donate()
            form_General=donateform.DonateGeneral()
    else:
        form=donateform.Donate()
        form_General=donateform.DonateGeneral()
    donationCounter=DonationCount.objects.first()'''
    if request.method=='POST':
        form=donateform.Donate(request.POST)
        if form.is_valid():
            donation=form.save()
            donation_type=form.cleaned_data.get('donation_type')
            request.session['donation_num']=form.cleaned_data.get('number_of_items')
            request.session['donation_amount']=form.cleaned_data.get('your_donation')
            donation_id=donation.pk
            request.session['donation_type']=donation_type
            request.session['donation_id']=donation_id
            return redirect(reverse('donation_process'))
    else:
        form=donateform.Donate()
    return render(request, 'donate/donate.html', {'form': form})
    #return render(request, 'donate/donate.html', {'form_General':form_General, 'form': form, 'count':donationCounter})

def donation_process(request):
    donationtype = request.session.get('donation_type')
    donationnum = request.session.get('donation_num')
    donationamount = request.session.get('donation_amount')
    donation_id = request.session.get('donation_id')
    donation = Donation.objects.get(pk=donation_id)
    fee = donation.cover_the_transaction_fee
    host = request.get_host()
    paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            #'amount': amount,
            'item_name': 'SAS-TASSEL Gala Night',
            'invoice': str(donation_id),
            'currency_code': 'USD',
            'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host, reverse('donation_done')),
            'cancel_return': 'http://{}{}'.format(host, reverse('donation_canceled')),
        }
    if donationtype == 'item1':
        donation.your_donation = donationnum*75
        donation.save()
        if fee==True:
            paypal_dict['amount']=(donationnum*75)/0.976
        else:
            paypal_dict['amount']=donationnum*75
    elif donationtype == 'item2':
        donation.your_donation = donationnum*100
        donation.save()
        if fee==True:
            paypal_dict['amount']=(donationnum*100)/0.976
        else:
            paypal_dict['amount']=donationnum*100
    elif donationtype == 'item3':
        donation.your_donation = donationnum*125
        donation.save()
        if fee==True:
            paypal_dict['amount']=(donationnum*125)/0.976
        else:
            paypal_dict['amount']=donationnum*125
    elif donationtype == 'item4':
        donation.your_donation = donationnum*150
        donation.save()
        if fee==True:
            paypal_dict['amount']=(donationnum*150)/0.976
        else:
            paypal_dict['amount']=donationnum*150
    elif donationtype == 'general':
        donation.your_donation = donationamount
        donation.save()
        if fee==True:
            paypal_dict['amount']=(donationamount)/0.976
        else:
            paypal_dict['amount']=donationamount
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'donate/donation_process.html', {'form': form})

def donate_progress(request):
    donationCounter = DonationCount.objects.first()
    return render(request, 'donate/donation_progress.html', {'count':donationCounter})