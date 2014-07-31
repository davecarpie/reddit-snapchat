import requests

from image_editor import ImageEditor
from post import Post
from image_getter import ImageGetter

headers = {"User-Agent" : "Snaphat by ImOffTheRails"}
r = requests.get('http://www.reddit.com/r/pics.json', headers=headers)

if r.status_code == 200:
  for post in r.json()['data']['children']:
    post = Post(post['data'])
    if post.is_image():
      image_name = ImageGetter(post).get_image()
      ie = ImageEditor(image_name)
      ie.add_text_to_image(post.title)
      ie.save(image_name)
else:
  print "Not a 200 :("
