# TextToImageDjango
This is a Django-based web application that allows users to input text descriptions and generates corresponding images using a text-to-image generation model.

## Requirements
- Python 3.7 or higher
- Django 3.0 or higher

## Installation
1. Clone the repository:

```
git clone https://github.com/kumarbijay/TextToImageDjango.git
```

2. Install the required packages:

```
pip install -r requirements.txt
```

3. Replace the placeholder API key with your OpenAI API key in the file generateimage/views.py, line 15:
python

```
openai.api_key = "YOUR_OPENAI_APIKEY"
```

4. Run the development server:

```
python manage.py runserver
```

The application should now be running on http://localhost:8000/.

## Usage
- Open a web browser and navigate to http://localhost:8000/.

- Input a text description in the text field and click on the "Generate Image" button.

- The generated image will be displayed below the text field.

## Demo
A live demo of the website is available at: https://kumarbijay.pythonanywhere.com

## File Structure
The repository has the following file structure:

```
TextToImageDjango/
├── manage.py
├── TextToImage
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── TextToImageApp
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    ├── models.py
    ├── static
    ├── templates
    └── views.py
```
    
## Conclusion
TextToImageDjango is a simple and easy-to-use Django-based web application that allows users to generate images from text descriptions. Feel free to use, modify and extend the code as per your needs.
