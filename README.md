## Install Virtual Environment
```As both Django and RASA work with Python Its better to create a Virtual Environment.
- virtualenv envname --python=python3
    - type this command to create a virtual environment, where envname can be any name chosen by user
- To Activate Virtual Environment
    - source envname/bin/activate
- To Deactivate Virtual Environment
    - deactivate
```

## Instal required libraries from requirements.txt
```Libraries required for smooth working of both Django and RASA, all libraries are stored in requirements.txt 
To Install type this command
- pip install -r requirements.txt    
```

Once libraries are installed Open three terminal/command prompt window


## For running Django Server
```
Go to backend_django folder.
    - python manage.py runserver
```

## For running RASA Server
```
Go to rasa_chat folder, and type
    - rasa run -m models --enable-api --cors "*"
```

## For running RASA Actions Server 
```
Go to rasa_chat folder, and type
    - rasa run actions
```
## For Seeing Chat Applicatio
```
After starting all three server.
    - Goto Browser and type : http://localhost:8000/chat/
```

For creating chat views and also webhook to django server: https://github.com/Alexmhack/Django-Rasa-Bot
was used