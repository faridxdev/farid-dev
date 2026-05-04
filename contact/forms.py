from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Votre nom complet',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'votre@email.com',
                'class': 'form-control'
            }),
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Décrivez votre projet ou votre demande...',
                'class': 'form-control'
            }),
        }
        labels = {
            'name': 'Nom complet',
            'email': 'Adresse email',
            'subject': 'Sujet',
            'message': 'Message',
        }

    def clean_message(self):
        message = self.cleaned_data.get('message', '')
        if len(message) < 20:
            raise forms.ValidationError("Votre message doit faire au moins 20 caractères.")
        return message