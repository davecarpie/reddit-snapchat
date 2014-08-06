from snapchat import Snapchat
from config import snapchat_password

class Snapchatter():

  def __init__(self):
    self.s = Snapchat()
    self.s.login('r-pics', snapchat_password)

  def get_recipients(self):
    verbose_friends = self.s.get_updates()['updates_response']['added_friends']
    return [str(friend['name']) for friend in verbose_friends]

  def send(self, image_name):
    media_id = self.s.upload(Snapchat.MEDIA_IMAGE, image_name)
    self.s.send(media_id, self.get_recipients())
