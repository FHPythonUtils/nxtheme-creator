from __future__ import annotations

from PIL import Image, ImageFilter, ImageOps

from nxtheme_creator.datamodels import ImageMode, ResizeMethod

SIZE = (1280, 720)


def _resize_max(image: Image.Image, max_size: tuple[int, int]) -> Image.Image:
    image_ratio = image.width / image.height
    target_ratio = max_size[0] / max_size[1]

    if image_ratio > target_ratio:
        new_width = max_size[0]
        new_height = round(new_width / image_ratio)
    else:
        new_height = max_size[1]
        new_width = round(new_height * image_ratio)

    return image.resize((new_width, new_height), Image.Resampling.LANCZOS)


def resize_stretch(image: Image.Image) -> Image.Image:
	"""Resize the image by stretching it to the target SIZE."""
	return image.resize(SIZE, Image.Resampling.LANCZOS)


def resize_center_crop(image: Image.Image) -> Image.Image:
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


def resize_outer_crop_letterbox(image: Image.Image) -> Image.Image:
	"""Resize the image using outer crop with blurred background."""
	# Resize image to fit in target size, preserving aspect ratio
	fg = _resize_max(image, SIZE)

	# Create a blurred background from the original image
	bg = image.resize(SIZE, Image.Resampling.LANCZOS)
	bg = bg.filter(ImageFilter.GaussianBlur(radius=20))

	# Paste the resized image onto the center of the blurred background
	offset = (
		(SIZE[0] - fg.width) // 2,
		(SIZE[1] - fg.height) // 2
	)
	bg.paste(fg, offset)
	return bg



def mode_blur(image: Image.Image) -> Image.Image:
	return image.filter(ImageFilter.GaussianBlur(radius=20))

def mode_dominant_color(image: Image.Image, colors:int=8):
	quantized = image.convert("RGB").quantize(colors=colors)
	palette = quantized.getpalette()
	color_counts = quantized.getcolors()

	# Extract RGB tuples
	rgb_palette = [
		((palette[i * 3], palette[i * 3 + 1], palette[i * 3 + 2]), count)
		for count, i in color_counts
	]

	# Return the color with the highest count
	dominant=max(rgb_palette, key=lambda x: x[1])[0]
	return Image.new("RGB", SIZE, dominant)



def resize_image(
	input_path: str,
	output_path: str,
	resize_method: ResizeMethod = ResizeMethod.STRETCH,
	image_mode: ImageMode | None = None,
):
	"""Resize the image using the specified method and save the output."""
	image = Image.open(input_path)

	if resize_method == ResizeMethod.STRETCH:
		transformed_image = resize_stretch(image)
	elif resize_method == ResizeMethod.CENTERCROP:
		transformed_image = resize_center_crop(image)
	elif resize_method == ResizeMethod.OUTERCROP:
		transformed_image = resize_outer_crop_letterbox(image)

	# Apply effects here
	if image_mode == ImageMode.BLUR:
		transformed_image = mode_blur(transformed_image)
	if image_mode == ImageMode.COLOR:
		transformed_image = mode_dominant_color(transformed_image)

	transformed_image.save(output_path, progressive=False)
	return output_path
