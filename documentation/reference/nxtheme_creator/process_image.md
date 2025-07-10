# Process Image

[Nxtheme-creator Index](../README.md#nxtheme-creator-index) / [Nxtheme Creator](./index.md#nxtheme-creator) / Process Image

> Auto-generated documentation for [nxtheme_creator.process_image](../../../nxtheme_creator/process_image.py) module.

- [Process Image](#process-image)
  - [mode_blur](#mode_blur)
  - [resize_center_crop](#resize_center_crop)
  - [resize_image](#resize_image)
  - [resize_outer_crop_letterbox](#resize_outer_crop_letterbox)
  - [resize_stretch](#resize_stretch)

## mode_blur

[Show source in process_image.py:43](../../../nxtheme_creator/process_image.py#L43)

#### Signature

```python
def mode_blur(image: Image.Image) -> Image.Image: ...
```



## resize_center_crop

[Show source in process_image.py:15](../../../nxtheme_creator/process_image.py#L15)

Resize the image using center crop method.

#### Signature

```python
def resize_center_crop(image: Image.Image) -> Image.Image: ...
```



## resize_image

[Show source in process_image.py:47](../../../nxtheme_creator/process_image.py#L47)

Resize the image using the specified method and save the output.

#### Signature

```python
def resize_image(
    input_path: str,
    output_path: str,
    resize_method: ResizeMethod = ResizeMethod.STRETCH,
    image_mode: ImageMode | None = None,
): ...
```

#### See also

- [ResizeMethod](./datamodels.md#resizemethod)



## resize_outer_crop_letterbox

[Show source in process_image.py:35](../../../nxtheme_creator/process_image.py#L35)

Resize the image using outer crop (letterbox) method.

#### Signature

```python
def resize_outer_crop_letterbox(image: Image.Image) -> Image.Image: ...
```



## resize_stretch

[Show source in process_image.py:10](../../../nxtheme_creator/process_image.py#L10)

Resize the image by stretching it to the target SIZE.

#### Signature

```python
def resize_stretch(image: Image.Image) -> Image.Image: ...
```