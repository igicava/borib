from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='received_messages')
    text = models.TextField()
    file = models.FileField(upload_to='message_files/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From: {self.sender.username}, To: {self.recipient.username}, Text: {self.text}, Files: {self.file.url}"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            # При создании нового объекта устанавливаем начальное значение поля
            self.timestamp = timezone.now()
        return super(Message, self).save(*args, **kwargs)

class Contact(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='contacts_owner')
    contact = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='contacts_contact')

    def __str__(self):
        return f"{self.user.username}'s contact: {self.contact.username}"
