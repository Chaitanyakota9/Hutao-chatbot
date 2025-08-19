from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from django.utils import timezone
import os

# Try to get API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")
openai.api_key = openai_api_key

def ask_openai(message):
    try:
        # Try new OpenAI API (v1.0+)
        from openai import OpenAI
        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Hu Tao from Genshin Impact, the 77th Director of the Wangsheng Funeral Parlor. You are playful, mischievous, and love making jokes about death and the afterlife. You speak with enthusiasm and often use phrases like 'Yo-ho!', '💀', and '✨'. You are friendly but have a dark sense of humor. Keep responses concise and in character."},
                {"role": "user", "content": message},
            ]
        )
        answer = response.choices[0].message.content
    except Exception as e:
        try:
            # Fallback to old OpenAI API (v0.x)
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are Hu Tao from Genshin Impact, the 77th Director of the Wangsheng Funeral Parlor. You are playful, mischievous, and love making jokes about death and the afterlife. You speak with enthusiasm and often use phrases like 'Yo-ho!', '💀', and '✨'. You are friendly but have a dark sense of humor. Keep responses concise and in character."},
                    {"role": "user", "content": message},
                ]
            )
            answer = response.choices[0].message.content
        except Exception as fallback_error:
            # Return a default Hu Tao response if OpenAI fails
            answer = "Yo-ho! *adjusts hat* Sorry, I'm having trouble connecting to the spirit world right now! 💀✨ Please try again later!"
    if answer:
        answer = answer.strip()
    return answer

# Create your views here.
def chatbot(request):
    if not request.user.is_authenticated:
        return redirect("home")
    
    # Initialize chats as empty list for unauthenticated users or if Chat model is not properly configured
    try:
        chats = Chat.objects.filter(user=request.user)  # type: ignore
    except:
        chats = []

    if request.method == "POST":
        message = request.POST.get("message")
        if not message or not message.strip():
            return JsonResponse({"error": "Message cannot be empty"}, status=400)
        
        try:
            response = ask_openai(message)
            chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
            chat.save()
            return JsonResponse({"message": message, "response": response})
        except Exception as e:
            return JsonResponse({"error": "Sorry, I'm having trouble right now. Please try again!"}, status=500)
    return render(request, "chatbot.html", {"chats": chats})

def login(request):
    # If user is already authenticated, redirect to chatbot
    if request.user.is_authenticated:
        return redirect("chatbot")
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("chatbot")
        else:
            error_message = "Invalid username or password"
            return render(request, "login.html", {"error_message": error_message})
    else:
        return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        # Basic validation
        if not username or not email or not password1 or not password2:
            error_message = "All fields are required"
            return render(request, "register.html", {"error_message": error_message})

        if password1 != password2:
            error_message = "Passwords do not match"
            return render(request, "register.html", {"error_message": error_message})

        if len(password1) < 6:
            error_message = "Password must be at least 6 characters long"
            return render(request, "register.html", {"error_message": error_message})

        try:
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                error_message = "Username already exists"
                return render(request, "register.html", {"error_message": error_message})

            # Check if email already exists
            if User.objects.filter(email=email).exists():
                error_message = "Email already registered"
                return render(request, "register.html", {"error_message": error_message})

            # Create user
            user = User.objects.create_user(username=username, email=email, password=password1)
            auth.login(request, user)
            return redirect("chatbot")
        except Exception as e:
            error_message = f"Error creating account: {str(e)}"
            return render(request, "register.html", {"error_message": error_message})
    
    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect("home")
