from PIL import Image, ImageDraw, ImageFont
import textwrap

class ImageEditor():

  def __init__(self, image_name):
    self.im = Image.open(image_name)
    self.image_name = image_name
    self.font_name = 'Avenir.ttc'

  def generate_lines(self, text):
    return textwrap.wrap(text, width = 35)

  def get_widest_line(self, lines):
    size = 15
    font = ImageFont.truetype(self.font_name, size)

    widest_line = lines[0]
    for line in lines[1:]:
      if font.getsize(line)[0] > font.getsize(widest_line)[0]:
        widest_line = line

    return widest_line

  def get_ideal_font(self, lines):
    ideal_width = self.im.size[0]-40
    widest_line = self.get_widest_line(lines)
    size = 8
    font = ImageFont.truetype(self.font_name, size)

    while font.getsize(widest_line)[0] < ideal_width:
      size += 2
      font = ImageFont.truetype(self.font_name, size)

    size -= 2
    return ImageFont.truetype(self.font_name, size)

  def get_text_height(self, lines, font):
    total_height = 0
    for line in lines:
      width, height = font.getsize(line)
      total_height += height

    return total_height

  def draw_lines_on_image(self, lines, font):
    # going to use a 20px buffer below and above text
    text_height = self.get_text_height(lines, font)
    new_image_height = self.im.size[1] + 40 + text_height
    new_image_width = self.im.size[0]
    new_im = Image.new("RGBA", (new_image_width, new_image_height), (0,0,0))


    new_im.paste(self.im, (0,0,self.im.size[0], self.im.size[1]))
    draw = ImageDraw.Draw(new_im)

    y = self.im.size[1] + 20
    for line in lines:
      width, height = font.getsize(line)
      draw.text((20, y), line, (255, 255, 255), font=font)
      y += height
    self.im = new_im

  def add_text_to_image(self, text):
    lines = self.generate_lines(text)
    font = self.get_ideal_font(lines)
    self.draw_lines_on_image(lines, font)

  def save(self, new_name):
    self.im.save(new_name)
