from PIL import Image

from tempfile import 

def preprocessing(img):
	# type: (Text) -> Image
	"""
	Arguments:
		img (Text): The file location of the image.

	Specifically, we:
	1) Convert the image to Black and White.
	"""
	
	im = Image.open(img).convert("L")
	return im

def processing(img):
	# type: (Image) -> Image
	""""""
	pass

def produce_edged_image(src, dest):
	# type: (Text, Text) -> None
	"""Creates an edged image at dest."""
	im = preprocessing(src)
	processing(im)
	
	im.show()

	im.save(dest)


def main(src, dest):
	# type: (Text, Text) -> None
	produce_edged_image(src, dest)

if __name__ == "__main__":
	main("res/duck.jpg", "res/edged_duck.jpg")