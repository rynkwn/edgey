from PIL import Image

class Cleaner(object):
	"""A class to quickly perform some pre-processing for an image."""

	@staticmethod
	def clean(src):
		# type: (Text) -> Image
		"""
		Arguments:
			img (Text): The file location of the image.

		Specifically, we:
		1) Convert the image to Black and White.
		"""
		im = Image.open(src).convert("L")
		return im