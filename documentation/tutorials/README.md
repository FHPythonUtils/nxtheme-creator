
# **Tutorial: Generating Nintendo Switch Themes with `nxtheme-creator`**

This tutorial will guide you through using the `nxtheme-creator` tool to generate custom themes for your Nintendo Switch. Follow these steps to create multiple themes from images (with optional configuration for layouts)

## **Step 1: Install `nxtheme-creator`**

install with python-pip nxtheme-creator

```sh
python3 -m pip install
```

## **Step 2: Prepare Your Images**

**Create an Input Directory**: Organize your images in a directory. The directory structure should look like this:

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
└── theme3/
	├── home.jpg
	├── lock.jpg
	├── apps.jpg
	├── set.jpg
	├── user.jpg
	└── news.jpg
```

Each image file should correspond to a different part of the theme (home screen, lock screen, etc.). But note these may be combined with a comma as shown above to apply one image to multiple parts of the UI

## **Step 3: \[Optional] Configure the `conf.json` File**

Create or modify a `conf.json` file in the root directory of `nxtheme-creator`. This file will specify how the tool should process your images. Here’s an example configuration:

```json
{
	"home": "DogeLayoutRounded",
	"lock": null,
	"apps": null,
	"set": null,
	"user": null,
	"news": null,
	"author_name": "JohnDoe"
}

```

Note that items ["home", "lock", "apps", "set", "user", "news"] are configured with the layout file, `.json` may be omitted from the file end, also note that if the file does not exist locally, we fallback to the copy included with `SwitchThemes.exe` if available. If not found, an error is returned

## **Step 4: Run the Tool**

### **Using the Command Line**

Open your terminal or command prompt and run the following command to generate your theme:

```bash
python3 -m nxtheme-creator --nxtheme /path/to/SwitchThemes.exe --input input_directory --output output_directory --config conf.json
```

Replace:

- `/path/to/SwitchThemes.exe` with the path to the `nxtheme` executable.
- `input_directory` with the path to your images. This defaults to the directory you run `nxtheme-creator` from
- `output_directory` with the directory where you want to save the generated theme files.This defaults to `./output/`
- `conf.json` with the path to your configuration file. Note this is optional, though needed if you wish to customise the layouts or set an `author_name`

### **Example Command**

Assuming you have the following setup:

- `SwitchThemes.exe` located at `/path/to/SwitchThemes.exe`
- Input directory is `./input_images`
- Output directory is `./themes`
- Configuration file is `./conf.json`

Run the command:

```bash
python3 -m nxtheme-creator --nxtheme /path/to/SwitchThemes.exe --input ./input_images --output ./themes --config ./conf.json
```

## **Step 5: Verify and Install Your Theme**

1. **Check the Output Directory**: After running the command, check the `output_directory` for the generated theme files (`.nxtheme` files).

2. **Install the Theme**: Follow your preferred method to install the generated theme on your Nintendo Switch. Typically, you would use an NXTheme installer or similar tool to apply the theme.

## **Troubleshooting**

- **Missing Images**: Ensure all required images are present and correctly named in your input directory.
- **Executable Issues**: Make sure the path to `SwitchThemes.exe` is correct and that you have the necessary permissions to run it.
