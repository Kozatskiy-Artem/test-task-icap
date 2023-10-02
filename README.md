# Test task ICAP Group Gmbh

## Getting started

Cloning repository:
```
git clone git@github.com:Kozatskiy-Artem/test-task-icap.git
```
Or
```
git clone https://github.com/Kozatskiy-Artem/test-task-icap.git
```

Create a `.env` file in the root of the project, with keys as in the `.env_example` file

Or

Use the following command:

For Windows:
```
copy .env_example .env
```

For UNIX:
```
cp .env_example .env
```

And fill in your own values

If you haven't previously created a project with a virtual environment, for example, in PyCharm, you can do it using the following commands:

To create a virtual environment, execute the command:
```
python -m venv venv
```

To activate the virtual environment in Unix-like systems, execute the command:
```
source venv/bin/activate
```

To activate the virtual environment in Windows, execute the command:
```
venv\Scripts\activate
```
This will allow you to create and activate a virtual environment for your project.

Install the necessary dependencies:
```
pip install -r requirements.txt
```

Create:
```
python manage.py makemigrations
```

And apply migrations:
```
python manage.py migrate
```

### Project Launch

Start the Django development server:
```
python manage.py runserver
```

Open your web browser and navigate to http://localhost:8000/.