from django.shortcuts import render
from Eron_app.forms import contactForm,ServiceForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):

    form=contactForm()

    if request.method=='POST':
        form= contactForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return thankyou(request)
        else:
            print('ERROR FORM INVALID ')    
   
    return render(request,'contact.html',{'form':form})




def FQa(request):
    return render(request ,'FQA.html')

def Policy(request):
    return render(request ,'Policy.html')

def Privacy(request):
    return render(request, 'Privacy.html')

def Service(request):

    formm=ServiceForm()

    if request.method=='POST':
        formm= ServiceForm(request.POST)

        if formm.is_valid():
            formm.save(commit=True)
            return thankyou(request)
        else:
            print('INVALID SELECTION ')    
   

    return render(request ,'Service.html',{'formm':formm})



def Servicedeal(request):
    return render(request, 'Servicedeal.html')

def thankyou(request):
    return render(request,'thanks.html')
