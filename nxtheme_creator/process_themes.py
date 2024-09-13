"""Underlying machineary to generate custom themes for your Nintendo Switch from your images."""

from __future__ import annotations

import os
import re
from pathlib import Path

from nxtheme_creator.backends import nxtheme, sarc_tool

SCREEN_TYPES = ["home", "lock", "apps", "set", "user", "news"]

THISDIR = Path(__file__).resolve().parent


def walkfiletree(inputdir: str) -> dict:
	"""Create a theme_image_map from an input directory by walking the dir and getting
		theme names and corresponding images for each component.

		:param str inputdir: the directory to walk
		:return dict: the final theme_image_map

		**Example**:
	Given the following directory structure:
	```
	input_directory/
	├── ThemeA/
	│   ├── home.jpg
	│   ├── lock.jpg
	│   └── apps,news.jpg
	└── ThemeB/
		├── home.dds
		└── lock.dds
	```
	Calling `walkfiletree("input_directory")` would produce:
	```json
	{
		"ThemeA": {
			"home": "/path/to/input_directory/ThemeA/home.jpg",
			"lock": "/path/to/input_directory/ThemeA/lock.jpg",
			"apps": "/path/to/input_directory/ThemeA/apps,news.jpg",
			"news": "/path/to/input_directory/ThemeA/apps,news.jpg"
		},
		"ThemeB": {
			"home": "/path/to/input_directory/ThemeB/home.dds",
			"lock": "/path/to/input_directory/ThemeB/lock.dds"
		}
	}
	```
	"""
	theme_image_map = {}

	# Walk over directories under inputdir
	for root, _dirs, files in os.walk(inputdir):
		for file in files:
			if file.endswith((".jpg", ".dds")):
				# Extract theme name from the directory structure
				theme_name = Path(root).name

				if theme_name not in theme_image_map:
					theme_image_map[theme_name] = {}

				# Extract the screen types from the image name e.g., 'home,lock.jpg'
				matches = re.match(r"(\w+(,\w+)*)", file)
				if matches:
					screen_types = matches.group(1)

					# Split by comma and map each screen type to the image path
					top_level_theme = False
					for screen_type in screen_types.split(","):
						if screen_type in SCREEN_TYPES:
							theme_image_map[theme_name][screen_type] = os.path.join(root, file)
						else:
							top_level_theme = True
					if top_level_theme:
						theme_image_map[screen_types] = {}
						for default_screen_type in SCREEN_TYPES:
							theme_image_map[screen_types][default_screen_type] = os.path.join(
								root, file
							)

	return theme_image_map


def resolveConf(nxthemebin: str | None, conf: dict) -> dict:
	"""
	Resolve the file paths for layout configurations specified in the `conf` dictionary.
	This function checks if the specified layout files exist. If they do not, it attempts
	to find the files in a default `Layouts` directory relative to the `nxthemebin` executable.
	If the files are still not found, it tries to append `.json` to the filenames and checks again.

	:param str nxthemebin: The path to the `nxtheme` executable, used to locate the default
		`Layouts` directory.
	:param dict conf: A dictionary containing layout configuration. The keys should be screen types
		(e.g., 'home', 'lock') and the values should be file paths or filenames.

	:return dict: The updated `conf` dictionary with resolved file paths.
	"""

	if nxthemebin is not None:
		layouts_dir = Path(nxthemebin).parent / "Layouts"
	else:
		layouts_dir = THISDIR / "layouts"

	for screen_type in SCREEN_TYPES:
		fname = conf.get(screen_type)
		if fname is None:
			break
		layout = Path(fname)
		if not layout.exists():
			layout = layouts_dir / layout.name
			if not layout.exists():
				layout = Path(fname + ".json")
				if not layout.exists():
					layout = layouts_dir / layout.name
					if not layout.exists():
						msg = f"{conf[screen_type]} or {layout} does not exist :("
						raise RuntimeError(msg)
		conf[screen_type] = str(layout)
	return conf


def processImages(nxthemebin: str | None, inputdir: str, outputdir: str, config: dict) -> None:
	"""
	Process images from the specified input directory to generate Nintendo Switch themes. This
		function handles the following tasks:
	1. Walks through the input directory to collect images and associate them with themes.
	2. Resolves and validates configuration paths for layout files.
	3. Iterates over each theme and its components, and builds the theme files using the `nxtheme`
		executable.

	:param str nxthemebin: The path to the `nxtheme` executable used for building themes.
	:param str inputdir: The directory containing the input images for the themes.
	:param str outputdir: The directory where the generated theme files will be saved.
	:param dict config: A dictionary containing configuration options such as the author name,
	and paths to layout files.

	:return: None
	"""
	themeimgmap = walkfiletree(inputdir=inputdir)
	config = resolveConf(nxthemebin, conf=config)

	author_name = config.get("author_name") or "JohnDoe"

	for theme_name, theme in themeimgmap.items():
		for component_name, image_path in theme.items():
			full_theme_name = f"{theme_name}_{component_name}"
			out = f"{outputdir}/{theme_name}/{full_theme_name}.nxtheme"
			print(f"Processing '{out}' ...")  # noqa: T201

			(Path(outputdir) / theme_name).mkdir(exist_ok=True, parents=True)

			if nxthemebin is not None:
				nxtheme.execute(
					nxthemebin=nxthemebin,
					component_name=component_name,
					image_path=image_path,
					layout_path=config.get(component_name) or "",
					theme_name=full_theme_name,
					author_name=author_name,
					out=out,
				)

			else:
				sarc_tool.execute(
					component_name=component_name,
					image_path=image_path,
					layout_path=config.get(component_name),
					theme_name=full_theme_name,
					author_name=author_name,
					out=out,
				)
