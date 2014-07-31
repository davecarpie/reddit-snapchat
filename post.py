class Post():
  def __init__(self, raw_dict):
    self.id = raw_dict['id']
    self.title = raw_dict['title']
    self.url = raw_dict['url']

  def is_image(self):
    acceptable_extentions = [".jpg", ".png", ".jpeg"]
    return len(self.url) > 4 and self.url[-4:].lower() in acceptable_extentions

  def __str__(self):
    return "Post {}: {} at {}".format(self.id, self.title, self.url)
