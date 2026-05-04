from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            # Récupération IP pour sécurité
            x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
            msg.ip_address = x_forwarded.split(',')[0] if x_forwarded else request.META.get('REMOTE_ADDR')
            msg.save()

            # Email de notification
            try:
                context = {'msg': msg}
                html = render_to_string('contact/email_notification.html', context)
                send_mail(
                    subject=f"[Portfolio] Nouveau message : {msg.get_subject_display()}",
                    message=f"De : {msg.name}\nEmail : {msg.email}\n\n{msg.message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    html_message=html,
                    fail_silently=True,
                )
                # Email de confirmation à l'expéditeur
                send_mail(
                    subject="Message reçu — Portfolio",
                    message=f"Bonjour {msg.name},\n\nVotre message a bien été reçu. Je vous répondrai sous 48h.\n\nCordialement.",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[msg.email],
                    fail_silently=True,
                )
            except Exception:
                pass

            messages.success(request, "Message envoyé avec succès ! Je vous répondrai sous 48h.")
            return redirect('contact')
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})