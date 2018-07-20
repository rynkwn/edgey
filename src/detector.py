from PIL import ImageFilter

class Detector(object):
	"""Perform edge detection and return the Image."""

	@staticmethod
	def detect(img):
		# type: (Image) -> Image
		"""Mark edges in the image."""
		return img

class DummyDetector(Detector):
	"""Super simple edge detection. Specifically:

	1) Naively smooth the image.
	2) For each pixel, look at cardinally adjacent pixels.
	3) If there's a large differential in r, g, b with any adjacent
	pixel, leave alone.
	4) Otherwise, color white.
	"""

	DIFFERENCE_THRESHOLD = 10

	@staticmethod
	def naive_smoother(img):
		# type: (Image) -> Image
		"""Go through the image with a naive smoother"""
		return img.filter(ImageFilter.SMOOTH)
	
	@staticmethod
	def detect(img):
		# type: (Image) -> Image
		"""Mark edges in the image."""
		img = DummyDetector.naive_smoother(img)

		width, height = img.size
		copyimg = img.copy()
		for x in [val + 1 for val in range(width - 2)]:
			for y in [val + 1 for val in range(height - 2)]:
				bw = img.getpixel((x, y))
				suspected_border = False

				for x_local in [x - 1, x + 1]:
					if abs(img.getpixel((x_local, y)) - bw) > DummyDetector.DIFFERENCE_THRESHOLD and not suspected_border:
						suspected_border = True

				for y_local in [y - 1, y + 1]:
					if abs(img.getpixel((x, y_local)) - bw) > DummyDetector.DIFFERENCE_THRESHOLD and not suspected_border:
						suspected_border = True

				if not suspected_border:
					copyimg.putpixel((x, y), 255)

		return copyimg