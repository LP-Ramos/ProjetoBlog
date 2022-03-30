from urllib import request
from webbrowser import get
from django.forms import ModelForm
from .models import Comentario
import requests


class FormComentario(ModelForm):
    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={'secret': '6Lf2tC0fAAAAAK1vbBwmjE41OynhLeF3GmYHP1ph',
            'response': recaptcha_response})

        recaptcha_result = recaptcha_request.json()

        if not recaptcha_result.get('success'):
            self.add_error('comentario', 'Desculpe-me robô, houve um erro.')            

        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome_comentario')
        email = cleaned_data.get('email_comentario')
        comentario = cleaned_data.get('comentario')

        if len(nome) < 5:
            self.add_error('nome_comentario', 'Nome precisa ter mais que 5 caracteres.')


    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario',)
