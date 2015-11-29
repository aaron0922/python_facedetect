import Image
from PIL import Image
import colorsys

def get_dominant_color(image):
    #color to RGB 
    image = image.convert('RGBA')
     
	#make image small and reduce cpu loading 
    image.thumbnail((200, 200))
     
    max_score = None
    dominant_color = None
     
    for count, (r, g, b, a) in image.getcolors(image.size[0] * image.size[1]):
        # skip black
        if a == 0:
            continue
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]
       
        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)        
        y = (y - 16.0) / (235 - 16)
         
        # skip high bright color
        if y > 0.9:
            continue
			
        # Calculate the score, preferring highly saturated colors.
        # Add 0.1 to the saturation so we don't completely ignore grayscale
        # colors by multiplying the count by zero, but still give them a low
        # weight.
        score = (saturation + 0.1) * count
         
        if score > max_score:
            max_score = score
            dominant_color = (r, g, b)
     
    return dominant_color


im = Image.open("../../pic/test/Arsenal-Team-3.jpg")
print im.format, im.size, im.mode
print get_dominant_color(Image.open('../../pic/test/Arsenal-Team-3.jpg'))

