from django.shortcuts import render
from listings.models import Band 
from listings.models import Listing
from listings.forms import BandForm, ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect  


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands':bands})

def band_detail(request, id):  # notez le paramètre id supplémentaire
    band = Band.objects.get(id=id)
    return render(request,'listings/band_detail.html',{'band': band}) # nous passons l'id au modèle


def about(request):
    return render(request, 'listings/about.html',)
    

def contact(request):
    
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us Form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['williams.kouton@groupecerco.com'],
            )
        return redirect('email-sent')  # ajoutez cette instruction de retour
        
        
    else:
        form = ContactUsForm()
        
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    
    form = ContactUsForm()
    
    return render (request, 'listings/contact.html', {'form':form})

def email_sent(request):
    return render(request, 'listings/email_sent.html')

def band_create(request):
    form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})



def listing(request):
    listings = Listing.objects.all()
    return render (request, 'listings/listings.html', {'listings':listings})

