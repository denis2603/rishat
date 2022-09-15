
python -m venv .venv
.venv/scripts/activate.bat
python -m pip install -requrements.txt

python manage.py makemigrations
python manage.py migrate

python runserver
