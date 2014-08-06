import requests

class ImageGetter():

  def __init__(self, post):
    self.post = post


  def get_image(self):
    r = requests.get(self.post.url)
    base, image_name = self.post.url.rsplit('/', 1)
    print image_name

    with open(image_name, 'wb') as f:
      f.write(r.content)

    return image_name
