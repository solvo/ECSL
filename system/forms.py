# -*- coding: utf-8 -*-
from registration.forms import *
from django.forms import HiddenInput
from django.utils.text import slugify
from system.models import *


#formulario de creacion de usuarios  quitar al final
class ProfileForm(RegistrationForm):
    name = forms.CharField(label='Name', required=True, )
    last_name = forms.CharField(label='Last name', required=True)
    gender = forms.ChoiceField(label='Gender', required=True, choices=[('m', 'Male'), ('f', 'Female'), ])
    born_date = forms.DateField(label='Born date', required=True)
    nationality = forms.CharField(label='Nationality', max_length=12, required=True)
    institution = forms.CharField(label='Institution', max_length=12, required=True)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)


class ModelFormWithSlugBase(forms.ModelForm):
    """Base ModelForm form models with a slug field."""

    def __init__(self, *args, **kwargs):
        super(ModelFormWithSlugBase, self).__init__(*args, **kwargs)
        self.fields['slug'].required = False

    class Meta:
        fields = '__all__'
        widgets = {
            'slug': HiddenInput
        }

    def clean_slug(self):
        """
        Auto-generate slug from name if left in blank.
        """
        return self.generate_slug_from_field()

    def generate_slug_from_field(self, target_field='name', default_value=None):
        """
        Auto-generate slug from a field if left in blank. Call this in clean_slug method.

        If slug exist, try by incrementing a suffix number.

        :param target_field: field name of the target field to generate slug (default: 'name')
        :param default_value: if subclass form provides a default value for target_field, specify it in this
            param (default: None)

        Usage::
            class YourModelForm(ModelFormWithSlugBase):

                class Meta(ModelFormWithSlugBase.Meta):
                    model = YOUR_MODEL

                def clean_slug(self):
                    return self.generate_slug_from_field('name')
        """
        data = self.cleaned_data['slug'] or slugify(self.cleaned_data[target_field]) or default_value
        # Validate unique
        slug_exists_count = self._meta.model.objects.filter(slug__regex=r'^%s(-\d+)?$' % data).count()
        if slug_exists_count:
            data += '-%s' % slug_exists_count
        return data




class InsertTopic(ModelFormWithSlugBase):

    class Meta(ModelFormWithSlugBase.Meta):
        model = Topic

    def __init__(self, *args, **kwargs):
        super(InsertTopic, self).__init__(*args, **kwargs)
        self.fields['name'].required = False

    def clean_slug(self):
        """
        Auto-generate slug from title if left in blank.
        """
        return self.generate_slug_from_field(target_field='name', default_value="Untitled")

    def clean_title(self):
        return self.cleaned_data['name'] or "Untitled"


class InsertSpeech(forms.ModelForm):

    class Meta:
        model = Speech
        fields = ['title', 'description', 'notes', 'speaker_information','audience', 'skill_level', 'speech_type', 'topic']
