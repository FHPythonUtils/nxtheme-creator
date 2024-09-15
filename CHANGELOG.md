# Changelog

All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2024.2 - 2024/09/15

- support means of image preprocessing through a `resize_method` option. It can take one of the following values:
	- **"outerCrop"**: Resizes the image to fit within the target dimensions while preserving its original aspect ratio. Any space left over is filled with black bars (letterboxing), if applicable.
	- **"innerCrop"**: Resizes the image by cropping parts of it to fit the target dimensions
	- **"stretch"**: Stretches the image to fit the target dimensions exactly, ignoring the original aspect ratio, which can lead to distortion.
	- **null**: No resizing method is applied.

## 2024.1.1 - 2024/09/13

- compress images

## 2024.1 - 2024/09/13

- default to use python sarc package for building, may still use `SwitchTheme.exe` as before
- include a copy of default layouts
- required relicensing to `gpl-2.0-or-later`

## 2024 - 2024/09/12

- first commit
