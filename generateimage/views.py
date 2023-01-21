import json
import requests
from django.shortcuts import render

def generate_image(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        size_option = request.POST.get('size_option')
        if size_option == "small":
            size = "256x256"
        elif size_option == "medium":
            size = "512x512"
        else:
            size = "1024x1024"
        api_key = "YOUR_OPENAI_APIKEY"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }
        data = """
        {
            """
        data += f'"model": "image-alpha-001",'
        data += f'"prompt": "{prompt}",'
        data += f'"size":"{size}",'
        data += """
            "num_images":1,
            "response_format":"url"
        }
        """

        resp = requests.post('https://api.openai.com/v1/images/generations',
                             headers=headers,
                             data=data)

        image_url = json.loads(resp.text)['data'][0]['url']
        return render(request, 'image.html', {'image_url': image_url, 'prompt': prompt})
    return render(request, 'index.html')
