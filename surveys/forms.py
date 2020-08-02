from django import forms

class MentorCall(forms.Form):

    learners_name = forms.CharField(
            label = 'Learners Name',
            widget = forms.TextInput
            )
    learners_email = forms.EmailField(
            label='Learner\'s Email', 
            widget = forms.EmailInput
            )
    mentors_name = forms.CharField(
            label = 'Mentors Name',
            widget = forms.TextInput
            )
    learners_email = forms.EmailField(
            label='Mentor\'s Email',
            widget = forms.EmailInput
            )
    subject = forms.CharField(
            label='What did you want to discuss in this call',
            widget=forms.Textarea
            )
    response = forms.CharField(
            label='What did you want to discuss in this call',
            widget=forms.Textarea
            )


        
