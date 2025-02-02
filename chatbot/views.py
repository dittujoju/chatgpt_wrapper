from django.shortcuts import render
from django.http import JsonResponse
from .chatgpt_api import ChatGPT
import os

chatbot = ChatGPT(api_key=os.environ.get('OPENAI_API_KEY'))

def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chatbot.ask(message)
        return JsonResponse({'response': response})
    return render(request, 'chatbot/chat.html')
