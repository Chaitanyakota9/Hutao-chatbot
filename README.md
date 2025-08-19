# Hu Tao Chatbot 💀✨

A beautiful Django chatbot featuring Hu Tao from Genshin Impact as the AI assistant. The chatbot has a stunning Hu Tao-themed interface with red, gold, and brown color schemes.

## Features

- 🤖 **Hu Tao AI Assistant**: Chat with Hu Tao, the 77th Director of the Wangsheng Funeral Parlor
- 🎨 **Beautiful UI**: Custom Hu Tao-themed design with animations and gradients
- 👤 **User Authentication**: Register, login, and logout functionality
- 💬 **Chat History**: View and manage chat conversations
- 🔧 **Admin Panel**: Django admin interface for managing users and chats
- 📱 **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

- **Backend**: Django 3.2.25
- **AI**: OpenAI GPT-4 API
- **Database**: PostgreSQL (production) / SQLite (development)
- **Static Files**: WhiteNoise
- **Deployment**: Render

## Local Development

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\\Scripts\\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with your OpenAI API key
6. Run migrations: `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`
8. Start the server: `python manage.py runserver`

## Environment Variables

Create a `.env` file with:
```
DEBUG=True
SECRET_KEY=your-secret-key
OPENAI_API_KEY=your-openai-api-key
DATABASE_URL=sqlite:///db.sqlite3
```

## Deployment on Render

1. Push your code to GitHub
2. Connect your repository to Render
3. Configure environment variables in Render dashboard
4. Deploy!

## Admin Access

- URL: `/admin/`
- Create a superuser with: `python manage.py createsuperuser`

## License

This project is for educational purposes. Hu Tao is a character from Genshin Impact by miHoYo.

---
*Yo-ho! Welcome to the Wangsheng Funeral Parlor! 💀✨*
