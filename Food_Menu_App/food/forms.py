from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  
        super(ItemForm, self).__init__(*args, **kwargs)