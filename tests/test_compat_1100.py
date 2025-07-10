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


def test_centerCrop():
	conf = {
		"home": aux_rand_layout("home"),
		# "lock": aux_rand_layout("lock"),
		"apps": aux_rand_layout("apps"),
		"psl": aux_rand_layout("psl"),
		"author_name": "JohnDoe",
		"resize_method": "centerCrop",
	}
	aux_testcase("center_crop", conf)


def test_stretch():
	conf = {
		"home": {"layout": aux_rand_layout("home"), "mode": "color"},
		# "lock": aux_rand_layout("lock"),
		"apps": aux_rand_layout("apps"),
		"psl": aux_rand_layout("psl"),
		"author_name": "JohnDoe",
		"resize_method": "stretch",
	}
	aux_testcase("stretch", conf)


def test_outerCrop():
	conf = {
		"home": {"layout": aux_rand_layout("home"), "mode": "blur"},
		# "lock": aux_rand_layout("lock"),
		"apps": aux_rand_layout("apps"),
		"psl": aux_rand_layout("psl"),
		"author_name": "JohnDoe",
		"resize_method": "outerCrop",
	}
	aux_testcase("outer_crop", conf)


def aux_rand_layout(layout: str) -> str:
	return random.choice([p.name for p in (nxdir / "layouts" / layout).iterdir()])


def aux_testcase(_input_dir: str, config: dict):
	input_dir = str(THISDIR / "data" / _input_dir)
	output_dir = str(THISDIR / "data/output" / _input_dir)

	config = Config.model_validate(config)

	# 'Native" with nxtheme-creator
	print(
		processImages(
			nxthemebin=None, inputdir=input_dir, outputdir=output_dir + "_native", config=config
		)
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
