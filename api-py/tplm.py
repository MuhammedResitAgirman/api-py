from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://jsonplaceholder.typicode.com/photos'
    response = requests.get(url)
    
    if response.status_code == 200:
        photos = response.json()
        photos = photos[:5]
    else:
        photos = []
    
    html = """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Photo Gallery</title>
        <style>
          body { font-family: Arial, sans-serif; }
          .photo { margin: 20px; }
          .photo img { max-width: 100px; }
          .photo h3 { margin: 5px 0; }
        </style>
      </head>
      <body>
        <h1>Photo Gallery</h1>
        <div>
          {% for photo in photos %}
            <div class="photo">
              <h3>{{ photo.title }}</h3>
              <img src="{{ photo.thumbnailUrl }}" alt="{{ photo.title }}">
              <p><a href="{{ photo.url }}" target="_blank">View Full Image</a></p>
            </div>
          {% endfor %}
        </div>
      </body>
    </html>
    """
    
    return render_template_string(html, photos=photos)

if __name__ == '__main__':
    app.run(debug=True)
