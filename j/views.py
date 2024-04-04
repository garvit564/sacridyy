from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.urls import reverse
from .models import ImageModel,WriteModel
from django.core.mail import send_mail
import random
from django.core.mail import EmailMessage, get_connection
from django.conf import settings




def email_form(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            words = ['ॐ दुं दुर्गायै नमः', 'सर्वमङ्गलमाङ्गल्ये शिवे सर्वार्थसाधिके। शरण्ये त्र्यम्बके गौरि नारायणि नमोऽस्तु ते॥', 'ॐ क्रीं कालिकायै नमः','नमोऽस्तु काल्यै च नमोऽस्तु कृष्णाय च। नमोऽस्तु महाकल्यै च नमोऽस्तु गरुडध्वजे॥','ॐ नमः शिवाय','ॐ त्र्यम्बकं यजामहे सुगन्धिं पुष्टिवर्धनम्। उर्वारुकमिव बन्धनान् मृत्योर्मुक्षीय मामृतात्॥','ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे','हरे कृष्ण हरे कृष्ण, कृष्ण कृष्ण हरे हरे। हरे राम हरे राम, राम राम हरे हरे॥','जय माता दी','ॐ नमो भगवते वासुदेवाय']
            random_word = random.choice(words)
            send_mail(
                'Random Word',
                f'Your randomly selected word is: {random_word}',
                'your_email@example.com',  # Your sender email address
                [email],  # List of recipient email addresses
                fail_silently=False,
            )
            return redirect(reverse('hello'))
        else:
            return HttpResponse('Email address not provided!')
    return render(request, 'index.html')


# def mantra(request):
#     mantras = ['Mantra 1', 'Mantra 2', 'Mantra 3']  # Apne mantron ki list yahan par define karein
#     return redirect('hello', {'mantras': mantras})



# Create your views here.
def hello(request):
    images = ImageModel.objects.all()
    texts=WriteModel.objects.all()
    mantras = ['ॐ दुं दुर्गायै नमः', 'सर्वमङ्गलमाङ्गल्ये शिवे सर्वार्थसाधिके। शरण्ये त्र्यम्बके गौरि नारायणि नमोऽस्तु ते॥', 'ॐ क्रीं कालिकायै नमः','नमोऽस्तु काल्यै च नमोऽस्तु कृष्णाय च। नमोऽस्तु महाकल्यै च नमोऽस्तु गरुडध्वजे॥','ॐ नमः शिवाय','ॐ त्र्यम्बकं यजामहे सुगन्धिं पुष्टिवर्धनम्। उर्वारुकमिव बन्धनान् मृत्योर्मुक्षीय मामृतात्॥','ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे','हरे कृष्ण हरे कृष्ण, कृष्ण कृष्ण हरे हरे। हरे राम हरे राम, राम राम हरे हरे॥','जय माता दी','ॐ नमो भगवते वासुदेवाय']  # Mantras ki list
    return render(request, 'index.html', {'mantras': mantras,'images': images,'texts': texts})
    
    

def home(request):
    return render(request, 'index.html')







def upload_image(request):
    

    if request.method == 'POST':    
       
        image = request.FILES.get('image')


        if image:
            ImageModel.objects.create(image=image)
            # return redirect(reverse('upload_image'))
            return HttpResponseRedirect(reverse('hello')+ '#hc')

    return render(request, 'index.html',)

















def delete_images(request):
    if request.method == 'POST':
        selected_images = request.POST.getlist('selected_images')

        # Check if any images are selected
        if selected_images:
            # Delete selected images using Django ORM
            for image_id in selected_images:
                ImageModel.objects.get(id=image_id).delete()

    return redirect(reverse('hello')+ '#after-delete')



def writetext(request):
    # texts=WriteModel.objects.all()
    if request.method == 'POST':
        text = request.POST.get('text')

        if text:
            WriteModel.objects.create(text=text)
            # return redirect(reverse('hello'))
            return HttpResponseRedirect(reverse('hello')+'#gc')

    return render(request, 'index.html', )



def delete_text(request, text_id):
    if request.method == 'POST':
        text = WriteModel.objects.get(id=text_id)
        text.delete()
    return HttpResponseRedirect(reverse('hello')+'#gc')




