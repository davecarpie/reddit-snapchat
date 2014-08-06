import json
import requests
import time

from post import Post
from snapchatter import Snapchatter
from image_getter import ImageGetter
from image_editor import ImageEditor

class RedditScraper():

	def __init__(self):
		self.minified_posts = []
		self.snapchatter = Snapchatter()

	def run(self):
		while True:
			try:
				headers = {"User-Agent" : "Snaphat by ImOffTheRails"}
				r = requests.get('http://www.reddit.com/r/pics.json', headers=headers)
				if r.status_code == 200:
					top_posts = [Post(post['data']) for post in r.json()['data']['children'][:3]]
					for post in top_posts:
						if not self.post_is_already_saved(post):
							self.save_post(post)
							time.sleep(10) # this is used to stop too many requests to snapchat at once
			except Exception as e:
				print (e)
			time.sleep(60)

	def post_is_already_saved(self, post):
		for saved_post in self.minified_posts:
			if post.id == saved_post.id:
				return True
		return False

	def save_post(self, post):
		self.minified_posts.append(post)
		if post.is_image():
			image_name = ImageGetter(post).get_image()
			ie = ImageEditor(image_name)
			ie.add_text_to_image(post.title)
			ie.save(image_name)
			self.snapchatter.send(image_name)
		else:
			print("isn't image: " + post.title)

def main():
	r = RedditScraper().run()

if __name__ == "__main__":
	main()
