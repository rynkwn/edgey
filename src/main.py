from clean import Cleaner
from detector import Detector

def produce_edged_image(src, dest, cleaner, edge_detector):
	# type: (Text, Text, Cleaner, Detector) -> None
	"""Creates an edged image at dest."""
	im = cleaner.clean(src)
	edge_detector.detect(im)
	
	im.show()

	im.save(dest)


def main(src, dest, cleaner, edge_detector):
	# type: (Text, Text, Cleaner, Detector) -> None
	produce_edged_image(src, dest. cleaner, edge_detector)

if __name__ == "__main__":
	main("res/duck.jpg", "res/edged_duck.jpg", Cleaner(), Detector())