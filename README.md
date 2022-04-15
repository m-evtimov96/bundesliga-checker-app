# bundesliga-checker-app
Small project using the OpenLigaDB API to display Bundesliga information.

### 1. Setup
1. Clone the repo in a new folder: `git clone https://github.com/m-evtimov96/bundesliga-checker-app.git`
2. In the *bundesliga-checker-app* folder create new venv using: `python -m venv my_venv_name`
3. Activate the virtual environment by running: `my_venv_name\Scripts\activate`
4. With active venv, run the following to install all required packages: `pip install -r requirements.txt`
5. Generate a **SECRET_KEY** using this command: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
6. Open *bundesliga-checker-app\bundesliga_checker*, create **.env** file and place in the first line `SECRET_KEY=your_generated_secret_key` without quotation marks
7. With active venv while in folder *bundesliga-checker-app* run the server: `python manage.py runserver`

