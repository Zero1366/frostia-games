Set-Content -Path .\build.sh -Encoding UTF8 -Value @(
"pip install -r requirements.txt",
"",
"python manage.py collectstatic --noinput",
"python manage.py migrate --noinput",
"python manage.py createsuperuser --noinput || true"
)