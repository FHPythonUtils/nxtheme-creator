
# **Tutorial: Generating Nintendo Switch Themes with `nxtheme-creator`**

This tutorial will guide you through using the `nxtheme-creator` tool to generate custom themes for
your Nintendo Switch. Follow these steps to create multiple themes from images (with optional
configuration for layouts)

## **Step 1: Install `nxtheme-creator`**

install with python-pip nxtheme-creator

```sh
python3 -m pip install
```

## **Step 2: Prepare Your Images**

**Create an Input Directory**: Organize your images in a directory. The directory structure should
look like this:

```sh
themes_directory/
├── theme1/
│   ├── home.jpg
│   ├── lock.jpg
│   ├── apps.jpg
│   ├── set.jpg
│   ├── user.jpg
│   └── news.jpg
├── theme2/
│   ├── home,lock.jpg
│   ├── apps,set,user.jpg
│   └── news.jpg
└── theme3.jpg

```

Each image file should correspond to a different part of the theme (home screen, lock screen, etc.).
These may be combined with a comma as shown above to apply one image to multiple parts of the UI.
Alternatively one image e.g. `theme3.jpg` may be used to create all parts of a theme.

## **Step 3: \[Optional] Configure the `conf.json` File**

Create a `conf.json` file in the root directory of `nxtheme-creator`. This file will specify how the tool should process your images. Here’s an example configuration:

```json
{
	"home": "DogeLayoutRounded",
	"lock": null,
	"apps": null,
	"set": null,
	"user": null,
	"news": null,
	"author_name": "JohnDoe",
	"resize_method": "outerCrop"
}
```

| Key           | Value               | Descriptionscreen                                                                                                                    |
| ------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| home          | "DogeLayoutRounded" | \[optional] Path to the layout.json for the home screen or a preset layout, e.g. the "DogeLayoutRounded" provided by nxtheme-creator |
| lock          | null                | \[optional] Path to the layout.json for the lock screen                                                                              |
| apps          | null                | \[optional] Path to the layout.json for the apps screen                                                                              |
| set           | null                | \[optional] Path to the layout.json for the settings screen                                                                          |
| user          | null                | \[optional] Path to the layout.json for the user section                                                                             |
| news          | null                | \[optional] Path to the layout.json for the news section                                                                             |
| author_name   | "JohnDoe"           | Name of the author                                                                                                                   |
| resize_method | "outerCrop"         | \[optional] The method used for image resizing. One of \["outerCrop", "innerCrop", "stretch", null]                                  |

Note that items ["home", "lock", "apps", "set", "user", "news"] are configured with a layout file,
`.json` may be omitted from the file end. Also note that if the path does not exist, we use to the
copy included with either the `SwitchThemes.exe`, or the `nxtheme-creator` backend if available.
If not found, an error is returned

The `resize_method` option defines how an image is resized. It can take one of the following values:

- **"outerCrop"**: Resizes the image to fit within the target dimensions while preserving its original aspect ratio. Any space left over is filled with black bars (letterboxing), if applicable.
- **"innerCrop"**: Resizes the image by cropping parts of it to fit the target dimensions
- **"stretch"**: Stretches the image to fit the target dimensions exactly, ignoring the original aspect ratio, which can lead to distortion.
- **null**: No resizing method is applied.

## **Step 4: Run the Tool**

### **With the SwitchThemes.exe backend**

Open your terminal or command prompt and run the following command to generate your theme:

```bash
python3 -m nxtheme-creator --nxtheme /path/to/SwitchThemes.exe --input input_directory --output output_directory --config conf.json
```

Replace:

- `/path/to/SwitchThemes.exe` with the path to the `nxtheme` executable.
- `input_directory` with the path to your images. This defaults to the directory you run `nxtheme-creator` from
- `output_directory` with the directory where you want to save the generated theme files.This defaults to `./output/`
- `conf.json` with the path to your configuration file. Note this is optional, though needed if you wish to customise the layouts or set an `author_name`

### **With the nxtheme-creator backend**

Open your terminal or command prompt and run the following command to generate your theme:

```bash
python3 -m nxtheme-creator --input input_directory --output output_directory --config conf.json
```

Replace:

- `input_directory` with the path to your images. This defaults to the directory you run `nxtheme-creator` from
- `output_directory` with the directory where you want to save the generated theme files.This defaults to `./output/`
- `conf.json` with the path to your configuration file. Note this is optional, though needed if you wish to customise the layouts or set an `author_name`

## **Step 5: Verify and Install Your Theme**

1. **Check the Output Directory**: After running the command, check the `output_directory` for the generated theme files (`.nxtheme` files).
2. **Install the Theme**: Follow your preferred method to install the generated theme on your Nintendo Switch. Typically, you would use an NXTheme installer or similar tool to apply the theme. For example, https://github.com/exelix11/SwitchThemeInjector

## **Troubleshooting**

- **Missing Images**: Ensure all required images are present and correctly named in your input directory.
- **Executable Issues**: Make sure the path to `SwitchThemes.exe` is correct and that you have the necessary permissions to run it.
