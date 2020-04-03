from PIL import Image, ImageDraw, ImageFont

# set drawing text ratio
MAX_RATIO = 0.8

# font size
FONT_MAX_SIZE = 256
FONT_MIN_SIZE = 24

# you should fix font path
FONT_NAME = '~/Library/Fonts/Hack Bold Nerd Font Complete.ttf'
FONT_COLOR_WHITE = (255, 255, 255, 0)

# output
OUTPUT_NAME = 'output.png'
OUTPUT_FORMAT = 'PNG'

def save_with_message(fp, message):
    image = Image.open(fp)
    draw = ImageDraw.Draw(image)
    
    image_width, image_height = image.size
    message_area_width, message_area_height = image_width * MAX_RATIO, image_height * MAX_RATIO
    
    # get moderate font size reducing one by one
    for font_size in range(FONT_MAX_SIZE, FONT_MIN_SIZE, -1):
        font = ImageFont.truetype(FONT_NAME, font_size)
        text_width, text_height = draw.textsize(message, font=font)
        w = message_area_width - text_width
        h = message_area_height - text_height
        
        if w > 0 and h > 0:
            position = ((image_width - text_width) / 2, (image_height - text_height) / 2)
            # draw message
            draw.text(position, message, fill=FONT_COLOR_WHITE, font=font)
            break
    
    image.save(OUTPUT_NAME, OUTPUT_FORMAT)