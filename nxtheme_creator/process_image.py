from PIL import Image, ImageOps

SIZE = (1280, 720)


def resize_stretch(image: Image.Image):
	"""Resize the image by stretching it to the target SIZE."""
	return image.resize(SIZE, Image.Resampling.LANCZOS)


def resize_center_crop(image: Image.Image):
	"""Resize the image using center crop method."""
	# Find the aspect ratio of the target SIZE and original image
	aspect_ratio_target = SIZE[0] / SIZE[1]
	aspect_ratio_original = image.width / image.height

	if aspect_ratio_original > aspect_ratio_target:
		# Image is wider than target, crop horizontally
		new_width = int(aspect_ratio_target * image.height)
		offset = (image.width - new_width) // 2
		cropped_image = image.crop((offset, 0, offset + new_width, image.height))
	else:
		# Image is taller than target, crop vertically
		new_height = int(image.width / aspect_ratio_target)
		offset = (image.height - new_height) // 2
		cropped_image = image.crop((0, offset, image.width, offset + new_height))

	return cropped_image.resize(SIZE, Image.Resampling.LANCZOS)


def resize_outer_crop_letterbox(image: Image.Image):
	"""Resize the image using outer crop (letterbox) method."""
	# Add padding if necessary (letterbox)
	image.thumbnail(SIZE, Image.Resampling.LANCZOS)
	letterbox_image = ImageOps.pad(image, SIZE, color=(0, 0, 0))
	return letterbox_image


def resize_image(input_path, output_path, method="stretch"):
	"""Resize the image using the specified method and save the output."""
	image = Image.open(input_path)

	if method == "stretch":
		resized_image = resize_stretch(image)
	elif method == "centerCrop":
		resized_image = resize_center_crop(image)
	elif method == "outerCrop":
		resized_image = resize_outer_crop_letterbox(image)
	else:
		return input_path

	resized_image.save(output_path, progressive=False)
	return output_path
