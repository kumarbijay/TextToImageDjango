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

## License
This project is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) license.

The full text of the license can be found here: https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode

In summary, the CC BY-NC-ND license allows others to download and share the material with proper attribution, but they cannot change or use it commercially.

If you use this project, you must give appropriate credit, provide a link to the license, and indicate if changes were made. You may not use the material for commercial purposes and you may not distribute derivatives of the material.
