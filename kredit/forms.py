from django import forms
from .models import Kredit

class KreditForm(forms.ModelForm):
    class Meta:
        model = Kredit
        fields = ['bank_name', 'credit_name', 'interest_rate', 'credit_char']
        labels = {
            'bank_name': 'Название банка',  # Русское имя для поля "Название банка"
            'credit_name': 'Вид кредита',  # Русское имя для поля "Вид кредита"
            'interest_rate': 'Процентная ставка',  # Русское имя для поля "Процентная ставка"
            'credit_char': 'Характеристика продукта',  # Русское имя для поля "Характеристика продукта"
        }