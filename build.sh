pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py setup_render_data
python manage.py createsuperuser --noinput || true