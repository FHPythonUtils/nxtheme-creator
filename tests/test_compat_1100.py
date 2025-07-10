"""Here we are testing compart between nxtheme-creator output and that from driving
SwitchThemes.exe from a release build.


Findings:
- Updating the version number and adding TargetFirmware=1100  results in a pass for most layouts

Failing layouts
- lock/Side Lock (native seems to add OriginY and ParentOriginY)

Further investigation reveals that the following are not supported

The layout patcher doesn't support all the properties of bflyt files, this is to avoid
compatibility issues in the future, if you changed values not included in the following list
they won't be detected by the differ :
- `Position`
- `Rotation`
- `Scale`
- `Size`
- `Visible`
- `OriginX`
- `OriginY`
- `ParentOriginX`
- `ParentOriginY`

Only for picture panes (pic1) and text panes (txt1) :
- `ColorTL` : Top left color
- `ColorTR` : Top right color
- `ColorBL` : Bottom left color
- `ColorBR` : Bottom right color
"""

from __future__ import annotations

import json
import random
from pathlib import Path

import oead
from sarc import sarc

from nxtheme_creator.datamodels import Config
from nxtheme_creator.process_themes import THISDIR as nxdir
from nxtheme_creator.process_themes import processImages

THISDIR = Path(__file__).resolve().parent


LATEST_VERSION = "4.8.1"
SWITCH_THEMES_EXE = r"C:\Users\Dell\Downloads\Release4.8.1\SwitchThemes.exe"


def test_me():
	input_dir = str(THISDIR / "data/input")
	output_dir = str(THISDIR / "data/output")

	home_layout_name = random.choice([p.name for p in (nxdir / "layouts/home").iterdir()])
	lock_layout_name = random.choice([p.name for p in (nxdir / "layouts/lock").iterdir()])
	apps_layout_name = random.choice([p.name for p in (nxdir / "layouts/apps").iterdir()])
	psl_layout_name = random.choice([p.name for p in (nxdir / "layouts/psl").iterdir()])

	config = Config.model_validate(
		{
			"home": home_layout_name,
			"lock": lock_layout_name,
			"apps": apps_layout_name,
			"psl": psl_layout_name,
			"author_name": "JohnDoe",
			"resize_method": "stretch",
		}
	)

	# 'Native" with nxtheme-creator
	processImages(
		nxthemebin=None, inputdir=input_dir, outputdir=output_dir + "_native", config=config
	)

	# # With SWITCH_THEMES_EXE
	processImages(
		nxthemebin=SWITCH_THEMES_EXE, inputdir=input_dir, outputdir=output_dir, config=config
	)

	switch_themes_exe = {}
	for file in Path(output_dir + "/example").iterdir():
		if file.suffix == ".nxtheme":
			switch_themes_exe[file.name] = read_nxtheme(file)

	native = {}
	for file in Path(output_dir + "_native/example").iterdir():
		if file.suffix == ".nxtheme":
			native[file.name] = read_nxtheme(file)

	for file_name in native:
		assert to_json(switch_themes_exe, file_name, "info.json") == to_json(
			native, file_name, "info.json"
		)
		assert to_json(switch_themes_exe, file_name, "layout.json") == to_json(
			native, file_name, "layout.json"
		)


def read_nxtheme(file: Path) -> dict[str:bytes]:
	data = file.read_bytes()
	data = oead.yaz0.decompress(data)
	sfile = sarc.SARC(data)
	return {name: sfile.get_file_data(name).tobytes() for name in sfile.list_files()}


def to_json(d: dict, file_name: str, fpointer: str):
	raw: bytes = d.get(file_name, {}).get(fpointer, b"{}")
	return json.loads(raw)
