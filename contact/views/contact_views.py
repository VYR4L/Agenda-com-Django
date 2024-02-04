from django.shortcuts import render, get_object_or_404
from contact.models import Contact
from django.http import Http404


def index(request):
    contacts = Contact.objects\
        .filter(show=True)\
            .order_by('-id')[:10]

    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request, contact_id):
    singe_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
        )

    context = {
        'contact': singe_contact,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )
