from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        listing = request.POST['listing']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have made inquiries for this apartment")
                return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, user_id=user_id, message=message)
        contact.save()

        messages.success(request, "You have submitted the form")
        return redirect('/listings/' + listing_id)
