from collections import defaultdict
from http import client
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from team.models import team
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
from django.conf import settings




def Home(request):
    
    
    return render(request,"index.html")
def AboutUs(request):
    
    
    return render(request,"aboutus.html")
 
def Login(request):
    
    if request.method=="POST": 
        uname=request.POST.get("username")
        pass1=request.POST.get("password")
        user=authenticate(request,username=uname,password=pass1) 

        
        if not User.objects.filter(username=uname).exists():
        # if not user.objects.filter(username=uname).exists():
        #     # Display an error message if the username does not exist
         
            messages.error(request, 'Invalid Username')
            return redirect('login')
             
        # # Authenticate the user with the provided username and password
        user =authenticate(username=uname, password=pass1)
        
        if user is None:
        #     # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
        #     # Log in the user and redirect to the home page upon successful login
         
            login(request, user)
            # messages.info(request,a)
            return redirect('/')
    
    
    return render(request,"signin.html")


def Signup(request):
    if request.method =="POST":
        uname=request.POST.get('username')
        email=request.POST.get("email")
        pass1=request.POST.get("password")
        # pass2=request.POST.get("password2")
         
        my_user=User.objects.filter(username=uname)
            # print(my_user)
        
        if my_user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('login')
          
        else:
                
        # # Create a new User object with the provided information
            my_user=User(username=uname,email=email,password=pass1)
        
        # # Set the user's password and save the user object
        
            my_user.save()
        
        # # Display an information message indicating successful account creation
            messages.info(request, "Account created Successfully!")
        
            return redirect('login')
    
    
    return render(request,"signup.html")


def Contact(request):
    
     context = {}
     
     if request.method == 'POST':
        address = request.POST.get('email')   
        fname = request.POST.get('fullname')
        subject = request.POST.get('subject')
        number = request.POST.get('number')
        message = request.POST.get('message')
      
        subject= "Subject: "+subject+"Name: "+fname+ " Phone number : "+number 
        
        if subject and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
                
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
                
        else:
            context['result'] = 'All fields are required'
    
    
    
     return render(request,"contact.html")


def Team(request):
    
    
     data=team.objects.all()
     key={
         'key':data
         
     }
    
    
    
     return render(request,"team.html",key)

# def AboutUs(request):
    
    
#     return render(request,"aboutus.html")

def Logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    
    
    
    return render(request,'signin.html')
def Profile(request):
    
    
    return render(request,'profile.html')
def Profiledetails(request):
    
    return render(request,"profiledetails.html")
 

from django.shortcuts import render
from chatbot.models import ClassTimetable, ExamSchedule, Faculty
from itertools import groupby
from openai import OpenAI
import json
 

def Exam(request):
     # Fetch all data
    timetable = ClassTimetable.objects.select_related('course').all()
    exams = ExamSchedule.objects.select_related('course').all()
    faculty_list = Faculty.objects.all().order_by('department', 'name')

    # Group timetable by day for easier rendering
    grouped_timetable = []
    # 
    # The 'timetable' queryset is already ordered by day_of_week (by model Meta)
    # We use a simple way to get the display value for the day choice
    display_day = dict(ClassTimetable.DAY_CHOICES) 
    
    for day, entries in groupby(timetable, key=lambda x: x.day_of_week):
        grouped_timetable.append({
            'day': display_day.get(day, day),
            'entries': list(entries)
        })

    context = {
        'grouped_timetable': grouped_timetable,
        'exam_schedule': exams,
        'faculty_contacts': faculty_list,
    }
      
   
    return render(request, 'exam.html',context)



def Facult(request):
     # Fetch all data
    timetable = ClassTimetable.objects.select_related('course').all()
    exams = ExamSchedule.objects.select_related('course').all()
    faculty_list = Faculty.objects.all().order_by('department', 'name')

    # Group timetable by day for easier rendering
    grouped_timetable = []
    # 
    # The 'timetable' queryset is already ordered by day_of_week (by model Meta)
    # We use a simple way to get the display value for the day choice
    display_day = dict(ClassTimetable.DAY_CHOICES) 
    
    for day, entries in groupby(timetable, key=lambda x: x.day_of_week):
        grouped_timetable.append({
            'day': display_day.get(day, day),
            'entries': list(entries)
        })

    context = {
        'grouped_timetable': grouped_timetable,
        'exam_schedule': exams,
        'faculty_contacts': faculty_list,
    }
      
   
    return render(request, 'faculty.html',context)



def Classtime(request):
     # Fetch all data
    timetable = ClassTimetable.objects.select_related('course').all()
    exams = ExamSchedule.objects.select_related('course').all()
    faculty_list = Faculty.objects.all().order_by('department', 'name')

    # Group timetable by day for easier rendering
    grouped_timetable = []
    # 
    # The 'timetable' queryset is already ordered by day_of_week (by model Meta)
    # We use a simple way to get the display value for the day choice
    display_day = dict(ClassTimetable.DAY_CHOICES) 
    
    for day, entries in groupby(timetable, key=lambda x: x.day_of_week):
        grouped_timetable.append({
            'day': display_day.get(day, day),
            'entries': list(entries)
        })

    context = {
        'grouped_timetable': grouped_timetable,
        'exam_schedule': exams,
        'faculty_contacts': faculty_list,
    }
      
   
    return render(request, 'classtime.html',context)

# def exam_schedule_view(request):
#     # Fetch all exams, ordered by date
#     exams = ExamSchedule.objects.all().select_related('course')
#     context = {'exams': exams}
#     return render(request, 'college_info/exam_schedule.html', context)

# def faculty_contacts_view(request):
#     # Fetch all faculty, ordered by name
#     faculty_list = Faculty.objects.all().order_by('name')
#     context = {'faculty_list': faculty_list}
#     return render(request, 'college_info/faculty_contacts.html', context)



# chatbot/views.py

import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from openai import OpenAI
from chatbot.models import ChatMessage # Import the model

# Initialize the OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY)

# Define the AI's persona (The 'Brain' of the chatbot)
SYSTEM_PROMPT = (
    "You are an AI Campus Assistant for a university. Your role is to provide accurate, "
    "concise, and friendly information regarding academic queries (courses, exam schedules, "
    "faculty office hours, registration) and general campus queries (library hours, student "
    "services, campus events). If you do not know the answer, politely suggest contacting "
    "the relevant administrative office."
)

# Renders the main chat interface
def chat_interface(request):
    # Ensure a session is created to track the conversation
    if not request.session.session_key:
        request.session.create()
    session_id = request.session.session_key
    
    # Optional: Load previous messages for context
    history = ChatMessage.objects.filter(session_id=session_id).order_by('timestamp')
    
    return render(request, 'chatview.html', {'history': history, 'session_id': session_id})

@csrf_exempt
def get_ai_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message')
            session_id = request.session.session_key
            
            if not user_message:
                return JsonResponse({'error': 'No message provided'}, status=400)
            
            # 1. Build Conversation History (for context)
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            
            # Fetch previous messages for continuity (optional, but recommended)
            past_messages = ChatMessage.objects.filter(session_id=session_id).order_by('timestamp')
            for msg in past_messages:
                messages.append({"role": msg.role, "content": msg.content})

            messages.append({"role": "user", "content": user_message})
            
            # 2. Save user message to DB
            ChatMessage.objects.create(role='user', content=user_message, session_id=session_id)

            # 3. Call the OpenAI API
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=300, 
                temperature=0.6 
            )
            
            ai_response = completion.choices[0].message.content
            
            # 4. Save AI response to DB
            ChatMessage.objects.create(role='ai', content=ai_response, session_id=session_id)

            # 5. Return the response
            return JsonResponse({'response': ai_response})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            print(f"API Error: {e}")
            return JsonResponse({'error': f'An internal error occurred: {e}'}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=404)