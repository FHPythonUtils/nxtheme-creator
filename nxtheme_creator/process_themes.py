import os
import re
import subprocess
from pathlib import Path

SCREEN_TYPES = ["home", "lock", "apps", "set", "user", "news"]


def walkfiletree(inputdir: str) -> dict:
	theme_image_map = {}

	# Walk over directories under inputdir
	for root, dirs, files in os.walk(inputdir):
		for file in files:
			if file.endswith((".jpg", ".dds")):
				# Extract theme name from the directory structure
				theme_name = os.path.basename(root)

				if theme_name not in theme_image_map:
					theme_image_map[theme_name] = {}

				# Extract the screen types from the image name (e.g., 'home,lock.jpg')
				screen_types = re.match(r"(\w+(,\w+)*)", file).group(1)

				# Split by comma and map each screen type to the image path
				for screen_type in screen_types.split(","):
					if screen_type in SCREEN_TYPES:
						theme_image_map[theme_name][screen_type] = os.path.join(root, file)

	return theme_image_map


def resolveConf(nxthemebin: str, conf: dict):
	for screen_type in SCREEN_TYPES:
		fname = conf.get(screen_type)
		if fname is None:
			break
		layout = Path(fname)
		if not layout.exists():
			layout = Path(nxthemebin).parent / "Layouts" / layout.name
			if not layout.exists():
				layout = Path(fname + ".json")
				if not layout.exists():
					layout = Path(nxthemebin).parent / "Layouts" / layout.name
					if not layout.exists():
						raise RuntimeError(f"{conf[screen_type]} or {layout} does not exist :(")
		conf[screen_type] = layout
	return conf


def processImages(nxthemebin: str, inputdir: str, outputdir: str, config: dict):
	themeimgmap = walkfiletree(inputdir=inputdir)
	config = resolveConf(nxthemebin, conf=config)

	theme_name = config.get("theme_name") or "MyCustomTheme"
	author_name = config.get("author_name") or "JohnDoe"

	for theme_name, theme in themeimgmap.items():
		for component_name, image_path in theme.items():
			name = f"{theme_name}_{component_name}"
			(Path(outputdir) / theme_name).mkdir(exist_ok=True, parents=True)
			subprocess.run(
				[
					nxthemebin,
					"buildNX",
					component_name,
					image_path,
					config.get(component_name) or "",
					f"name={name}",
					f"author={author_name}",
					f"out={outputdir}/{theme_name}/{name}.nxtheme",
				],
				check=False,
			)
