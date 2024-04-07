import time
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view # type: ignore
from django.urls import reverse


def index(request):
    return render(request, 'index.html')

def chatView(request, chat_model):
    return render(request, 'chat.html')


@csrf_exempt
@api_view(['POST'])
def AskAgentView(request, chat_model):
    if request.method == 'POST':
        try:
            received_data = request.data
            # print(received_data)
            message = received_data.get('message', '')
            model = received_data.get('model', '')
            print(model)
            # print(message)
            print('----------------------------------------------------------------')
            if model == 'gpt-3.5':
                response = "hi"
            
            elif model == 'claude':
                response = "Hi there"
            
            elif model == 'zephyr':
                response = "Hi once again"
            
            else:
                response = "Sorry"

            # For simplicity, let's just return a dummy response
            bot_response = response

            return JsonResponse({'botResponse': bot_response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)