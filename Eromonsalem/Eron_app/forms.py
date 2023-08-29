from django.forms import ModelForm,Textarea
from Eron_app.models import contactModel,ServiceModel

class contactForm(ModelForm):
    class Meta():
        model=contactModel
        fields=("fullname" ,"email" ,"message")
        widgets={
            'message':Textarea(attrs={'cols':35,'rows':5}),
        }


class ServiceForm(ModelForm):
    class Meta():
        model=ServiceModel
        fields='__all__'