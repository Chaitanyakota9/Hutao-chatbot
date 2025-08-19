# Hu Tao Chatbot 💀✨

A beautiful Django chatbot featuring Hu Tao from Genshin Impact as the AI assistant. The chatbot has a stunning Hu Tao-themed interface with red, gold, and brown color schemes.

## 🌐 Live Website

**Enjoy the bot here:** [https://hutao-chatbot-e6rw.onrender.com](https://hutao-chatbot-e6rw.onrender.com) 💀✨

## Features

- 🤖 **Hu Tao AI Assistant**: Chat with Hu Tao, the 77th Director of the Wangsheng Funeral Parlor
- 🎨 **Beautiful UI**: Custom Hu Tao-themed design with animations and gradients
- 👤 **User Authentication**: Register, login, and logout functionality
- 💬 **Chat History**: View and manage chat conversations
- 🔧 **Admin Panel**: Django admin interface for managing users and chats
- 📱 **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

- **Backend**: Django 4.2.10
- **AI**: OpenAI GPT-4 API
- **Database**: SQLite (current deployment) / PostgreSQL (planned)
- **Static Files**: WhiteNoise
- **Deployment**: Render
- **Python**: 3.13

## Project Workflow

### 🚀 User Journey
1. **Landing Page**: Users start at the login page
2. **Authentication**: Register new account or login with existing credentials
3. **Chat Interface**: Access the beautiful Hu Tao-themed chat interface
4. **AI Interaction**: Chat with Hu Tao AI assistant powered by GPT-4
5. **Chat History**: View and manage previous conversations
6. **Logout**: Secure logout with redirect to login page

### 🔧 Development Workflow
1. **Local Development**: Set up virtual environment and install dependencies
2. **Database Setup**: Run migrations and create superuser
3. **Testing**: Test locally with Django development server
4. **Version Control**: Commit changes and push to GitHub
5. **Deployment**: Automatic deployment to Render via GitHub integration
6. **Monitoring**: Check deployment logs and website functionality

### 🎯 Key Features Implementation
- **Authentication System**: Django's built-in auth with custom login/register views
- **AI Integration**: OpenAI API with fallback error handling
- **Static File Management**: WhiteNoise for production static file serving
- **Responsive Design**: Mobile-first CSS with Hu Tao theme
- **Admin Interface**: Custom Django admin with chat history management

## Environment Variables

Create a \.env\ file with:
\\\" >> README.md && echo 
DEBUG=True >> README.md && echo SECRET_KEY=your-secret-key >> README.md && echo OPENAI_API_KEY=your-openai-api-key >> README.md && echo DATABASE_URL=sqlite:///db.sqlite3 >> README.md && echo \\\"

## Deployment on Render

1. Push your code to GitHub
2. Connect your repository to Render
3. Configure environment variables in Render dashboard
4. Deploy!

## Admin Access

- URL: \/admin/\" >> README.md && echo 
-
Create
a
superuser
with:
\python
manage.py
createsuperuser\"

## License

This project is for educational purposes. Hu Tao is a character from Genshin Impact by miHoYo.

---
*Yo-ho! Welcome to the Wangsheng Funeral Parlor! 💀✨*
