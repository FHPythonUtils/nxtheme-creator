# Process Image

[Nxtheme-creator Index](../README.md#nxtheme-creator-index) / [Nxtheme Creator](./index.md#nxtheme-creator) / Process Image

> Auto-generated documentation for [nxtheme_creator.process_image](../../../nxtheme_creator/process_image.py) module.

- [Process Image](#process-image)
  - [resize_center_crop](#resize_center_crop)
  - [resize_image](#resize_image)
  - [resize_outer_crop_letterbox](#resize_outer_crop_letterbox)
  - [resize_stretch](#resize_stretch)

## resize_center_crop

[Show source in process_image.py:9](../../../nxtheme_creator/process_image.py#L9)

Resize the image using center crop method.

#### Signature

```python
def resize_center_crop(image: Image.Image): ...
```



## resize_image

[Show source in process_image.py:35](../../../nxtheme_creator/process_image.py#L35)

Resize the image using the specified method and save the output.

#### Signature

```python
def resize_image(input_path, output_path, method="stretch"): ...
```



## resize_outer_crop_letterbox

[Show source in process_image.py:28](../../../nxtheme_creator/process_image.py#L28)

Resize the image using outer crop (letterbox) method.

#### Signature

```python
def resize_outer_crop_letterbox(image: Image.Image): ...
```



## resize_stretch

[Show source in process_image.py:5](../../../nxtheme_creator/process_image.py#L5)

Resize the image by stretching it to the target SIZE.

#### Signature

```python
def resize_stretch(image: Image.Image): ...
```