from logging import PlaceHolder
from click import style
from django import forms
from crispy_forms.helper import FormHelper
from django.utils.translation import gettext_lazy as _
from matplotlib.pyplot import title
from .models import (
        Entry, Person
    )
from crispy_forms.layout import (
        Layout, Fieldset, HTML, 
        MultiField, Div, Field,
        Submit, Hidden, Button, Reset,
        ButtonHolder
    )
from crispy_forms.bootstrap import (
        InlineCheckboxes, InlineRadios,
        StrictButton, Tab, TabHolder,
        FieldWithButtons, FormActions,
        AppendedText, PrependedText, PrependedAppendedText,
        Accordion, AccordionGroup, Alert,
        Modal, UneditableField,
    )



class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length = 100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [
                    'headline', 
                    'authors',
                    'body_text', 
                    'rating', 
                    'pub_date', 
                    'mod_date', 
                    'number_of_comments', 
                    'number_of_pingbacks',
                    'blog'
                ]
        labels = {
            'headline': _('Title'), 
            'authors': _('Writer'),
            'body_text': _('Content'), 
            'rating': _('Ratings'), 
            'pub_date': _('Created at'), 
            'mod_date': _('Modified at'), 
            'number_of_comments': _('Comments'), 
            'number_of_pingbacks': _('Pingbacks'),
            'blog': _('Blog Title'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper

        self.helper.layout = Layout(
            Div(
                Field('headline', title='NewField'),
                ButtonHolder(
                    HTML('<span class = "hidden">X Saved data</span>'),
                    Submit('submit', 'Submit'),
                ),
                css_class = 'container',
                style = 'background:rgb(15, 16, 52); padding:30px; color:white;'
            ),
            Div(
                Hidden('hidden', 'Hidden'),
                Button('button', 'Button'),
                Reset('reset', 'Reset'),
                css_class = 'container',
                style = 'padding:30px; background:rgb(33, 71, 146);'
            ),
            FormActions(
                Submit('save', 'Save changes'),
                Button('cancel', 'Cancel'),
                css_class = 'container',
                style = 'background:black; color:white; padding:30px;'
                # wrapper_class = 'container',
            ),
            Div(
                AppendedText('headline', '$', active = True),
                PrependedText('headline', '@', placeHolder='username'),
                PrependedAppendedText('headline', '$', '@'),
                css_class = 'container',
                style = 'padding:30px; background:green;'
            ),
            Div(
                InlineCheckboxes('authors'),
                InlineRadios('authors'),
                FieldWithButtons('headline', StrictButton("Go!"), input_size='input-group-sm'),
                StrictButton('Success', css_class='btn-success'),
                css_class = 'container',
                style = 'padding:30px; background:blue;',
            ),
            Div(
                TabHolder(
                    Tab(
                        'First Tab',
                        'headline',
                        Div('body_text'),
                    ),
                    Tab(
                        'Second Tab',
                        Field('heading', css_class='extra')
                    ),
                    css_class = 'container',
                    style = 'padding:30px; background:black;'
                ),
                Accordion(
                    AccordionGroup(
                        'First Group',
                        InlineRadios('authors'),
                    ),
                    AccordionGroup(
                        'Second Group',
                        'headline',
                    ),
                ),
                Alert(content="<strong>Warning!</strong> Best check yo self."),
                UneditableField('headline', css_class='form-control-lg'),
                css_class = 'container',
                style = 'padding:30px; background:black;'
            ),
            Modal(
                Field('headline', placeholder='Headline'),
                Button(
                    'submit',
                    'Set headline',
                ),
            )
        )


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'first_name',
            'last_name',
            'shirt_size'
        ]

# class EntryForm(forms.ModelForm):
#     class Meta:
#         model = Entry
#         fields = []



class FavForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label = 'Do you like this website?',
        choices = ((1, 'Yes'), (0, 'No')),
        coerce = lambda x : bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )
    favorite_food = forms.CharField(
        label = 'What is your Favorite Food?',
        max_length = 80,
        required = True,
    )
    favorite_color = forms.CharField(
        label = 'What is your favorite Color',
        max_length = 80,
        required = True,
    )
    favorite_number = forms.IntegerField(
        label = 'Favorite Number',
        required = False,
    )
    notes = forms.CharField(
        label = 'Additional notes or feedback',
        required = False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'event-form'
        self.helper.form_class = 'event-blue'
        self.helper.form_method = 'post'
            
        self.helper.layout = Layout(
            # MultiField(
            #     'Tell us of your favorite stuff {{username}}',
            #     Div(
            #        InlineRadios('like_website'),
            #         'favorite_number',
            #         css_id = 'special-fields'
            #     ),
            #     'favorite_color',
            #     'favorite_food',
            #     HTML("""
            #     <p>We use notes to get better, <strong>please help us {{username}}</strong></p>
            #     """),
            #     'notes'
            # ),
            Fieldset(
                'Tell us of your favorite stuff {{username}}',
                'like_website',
                'favorite_number',
                'favorite_color',
                'favorite_food',
                HTML("""
                <p>We use notes to get better, <strong>please help us {{username}}</strong></p>
                """),
                'notes',
            ),
            Submit('submit', 'Submit', css_class='button-white')
        )