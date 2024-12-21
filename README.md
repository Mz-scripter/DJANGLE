# DJANGLE
**DJANGLE** is a specialized search engine built using Django and Scrapy, designed to provide curated search results exclusively for Django-related content. It indexes resources from popular websites such as Stack Overflow, GitHub, W3Schools, and the official Django documentation, offering developers a streamlined way to find way to find tutorials, documentation, repositories, and more.

## Features

### Core Features
- **Search Funtionality:**
    - Full-text search powered by PostgreSQL.
    - Supports ranking of results based on relevance, including titles, content, and keywords.
    - Filter results by type: Questions, Documentation, Tutorials, and Repositories.
- **Autocomplete Suggestions:**
    - Dynamic suggestions as users type in the search bar.
    - Suggestions are generated from indexed titles.
- **Pagination:**
    - Results are paginated for easy navigation.
- **Search Statistics:**
    - Displays the number of results and the time taken to fetch them.
- **Result Previews:**
    - Each result displays a truncated snippet of content for quick reference.

### Styling
- **Tailwind CSS:**
    - Clean, responsive, and modern UI.
    - Styled search bar, tabs, and autocomplete dropdown.
- **Tabs Navigation:**
    - Users can filter results by categories with visually distinct tabs.
- **Sticky Footer:**
    - Footer stays at the bottom of the page, providing links to social media profiles.


## Technologies Used

### Backend
- **Django:** For handling search logic, indexing, and database interactions.
- **Scrapy:** For web scraping and data extraction.
- **PostgreSQL:** As the database and search engine backend, using full-text search features.

### Frontend
- **Tailwind CSS:** For responsive and modern styling.
- **JavaScript:** For dynamic functionalities like autocomplete and AJAX-based search.


## Setup Instructions

### Prerequisites
1. Python 3.8+
2. Node.js and npm (for Tailwind CSS)
3. PostgreSQL
4. Git
5. Django environment setup

### Installation Steps

1. Clone the Repository
    ```
    git clone https://github.com/Mz-scripter/DJANGLE.git
    cd DJANGLE
    ```
2. Set Up a Virtual Environment
    ```
    python -m venv venv
    source venv/Scripts/activate 
    ```
3. Install Dependencies
    ```
    pip install -r requirements.txt
    npm install -D tailwindcss postcss autoprefixer
    npx tailwindcss init
    ```
4. Configure PostgreSQL
    - Create a database and user in PostgreSQL.
    - Update the `DATABASES` setting in `settings.py`:
        ```
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'your_database_name',
                'USER': 'your_database_user',
                'PASSWORD': 'your_password',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }
        ```
5. Run migrations
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Scrape data
    - Run Scrapy spiders to scrape data from supported websites:
    ```
    scrapy crawl stackspider -o stack_django.json
    scrapy crawl w3-spider -o w3schools.json
    scrapy crawl git-spider -o github.json
    scrapy crawl dj-docs -o django.json
    ```
    - Import the scraped data into the databses:
    ```
    python manage.py import_scraped_data
    ```
    - Update the index:
    ```
    python manage.py update_search_index
    ```
7. Build Tailwind CSS
    ```
    npx tailwindcss -i ./static/css/styles.css -o ./static/css/tailwind_output.css --watch
    ```
8. Run the server
    ```
    python manage.py runserver
    ```

## Screenshots

### Home Page
![home-page](https://github.com/user-attachments/assets/ec97c6ac-9a8b-406f-9f52-7059e0222770)

### Search Results
![search-page](https://github.com/user-attachments/assets/63cfe94a-aded-4895-9cb9-25ad22c3f6b1)

### Autocomplete Suggestions
![auto-suggestions](https://github.com/user-attachments/assets/045481b0-3d96-4077-8760-9e2f304ff3cf)


