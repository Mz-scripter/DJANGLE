#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Compile tailwindcss
npx tailwindcss -i ./static/css/styles.css -o ./static/css/tailwind_output.css --minify

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py makemigrations
python manage.py migrate

python create_superuser.py

# Update the database
python manage.py import_scraped_data web_crawler/dj-docs.json
python manage.py import_scraped_data web_crawler/dj-index2.json
python manage.py import_scraped_data web_crawler/git-results.json
python manage.py import_scraped_data web_crawler/w3-results.json
python manage.py import_scraped_data web_crawler/stack_django2.json

# Add Index
python manage.py update_search_index
