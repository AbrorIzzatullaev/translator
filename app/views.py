from django.shortcuts import render
from googletrans import Translator
translator = Translator()

def main(request):
    word = request.GET.get('word','')
    if translator.detect(word).lang == 'uz':
        translated_word = translator.translate(word, dest='en').text
    else:
        translated_word = translator.translate(word, dest='uz').text


    return render(request,'index.html',{'word':word, 'translated_word':translated_word})
