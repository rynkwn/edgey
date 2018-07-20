class Detector(object):
	"""Perform edge detection and return the Image."""

	@staticmethod
	def detect(img):
		# type: (Image) -> Image
		"""Mark edges in the image."""
		return img

class DummyDetector(Detector):
	"""Super simply edge detection."""
	
	@staticmethod
	def detect(img):
		# type: (Image) -> Image
		"""Mark edges in the image."""
		width, height = img.size
		for x in range(width):
			for y in range(height):
				pass

		return img