from django.contrib import admin

from django import forms

from .models import Food


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = []
        widgets = {
            'name': forms.Textarea(),
            'tags': forms.Textarea(),
        }


class FoodAdmin(admin.ModelAdmin):
    form = FoodForm


admin.site.register(Food)
# Uncomment to experiment with modelforms
# admin.site.register(Food, FoodAdmin)
