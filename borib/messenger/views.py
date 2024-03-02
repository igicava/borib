from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from messenger.models import Message, Contact
from users.models import User
from django.db.models import Q
from users import models
from django.urls import reverse

def send(request, recipienter):
    if request.method == 'POST':
        text = request.POST['text']
        sender = request.user
        recipients = User.objects.filter(username=recipienter).first()
        msg = Message(text=text, sender=sender, recipient=recipients)
        msg.save()
        return HttpResponseRedirect(f'/messenger/chat/{recipienter}/')
    else:
        return HttpResponseRedirect(reverse('users:profile'))

def add_contact(request):
    if request.method == 'POST':
        contact_name = request.POST['username']
        user = request.user
        if contact_name == user.username:
            return HttpResponseRedirect(reverse('users:profile'))
        contact_user = User.objects.filter(username=contact_name).first()
        if contact_user == None:
            return HttpResponse("<h1>Пользователя с таким именем не существует</h1>")
        contact = Contact(user=user, contact=contact_user)
        contacts = Contact.objects.filter(user=user)
        for i in contacts:
            if i.contact.username == contact.contact.username:
                return HttpResponseRedirect(reverse('users:profile'))
        re_contact = Contact(user=contact_user, contact=user)
        re_contacts = Contact.objects.filter(user=contact_user)
        for i in re_contacts:
            if i.contact.username == re_contact.contact.username:
                return HttpResponseRedirect(reverse('users:profile'))
        contact.save()
        re_contact.save()
        return HttpResponseRedirect(reverse('users:profile'))
    else:
        return HttpResponseRedirect(reverse('users:profile'))
        

def chat(request, recipient):
    if request.user.is_authenticated:
        contacts = Contact.objects.filter(user=request.user)
        contact = User.objects.filter(username=recipient).first()
        if contact == None:
            return HttpResponse("User undefined")
        a = False
        for i in contacts:
            if contact.username == i.contact.username:
                a = True
                break
        if a:
            sender_query = Q(sender=request.user, recipient=models.User.objects.filter(username=recipient).first())
            recipient_query = Q(sender=models.User.objects.filter(username=recipient).first(), recipient=request.user)
            messages = Message.objects.filter(sender_query | recipient_query).all()
            context = {
                'messages': messages.order_by('-timestamp'),
                'contact': recipient,
            }
            return render(request, 'messenger/chat.html', context)
        else:
            return HttpResponse("Chat undefined")
    else:
        return HttpResponse("Please authenticated")
