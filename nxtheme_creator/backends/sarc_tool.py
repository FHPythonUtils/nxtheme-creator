"""Python implementation of SwitchTheme.exe using the sarc lib to do a lot of the heavy lifting."""

from __future__ import annotations

import io
import json
import typing
from pathlib import Path

import oead
from sarc import sarc

from nxtheme_creator import img_info

# ruff: noqa: T201


def _write_sarc(writer: sarc.SARCWriter, dest_stream: typing.BinaryIO) -> None:
	buf = io.BytesIO()
	alignment: int = writer.write(buf)
	buf.seek(0)
	dest_stream.write(
		oead.yaz0.compress(buf.getbuffer(), data_alignment=(alignment if alignment > 0x20 else 0))
	)


def sarc_create(files: dict[str, bytes], dest_file: str) -> None:
	writer = sarc.SARCWriter(be=False)

	writer.set_align_for_nested_sarc(False)

	dest_stream: typing.BinaryIO = open(dest_file, "wb")

	for file, contents in files.items():
		writer.add_file(file, contents)

	_write_sarc(writer, dest_stream)


def execute(
	component_name: str,
	image_path: str,
	layout_path: str | None,
	theme_name: str,
	author_name: str,
	out: str,
) -> None:
	"""Python implementation of SwitchTheme.exe using the sarc lib to do a lot of the heavy lifting.

	:param str component_name: component to build. eg. home, apps etc
	:param str image_path: path to the source image
	:param dict layout_path: path to the layout file
	:param str name: theme name
	:param str author_name: author name
	:param str out: destination file name
	"""
	img = Path(image_path)

	width, height, is_progressive, is_dxt1 = 0, 0, False, True

	if img.suffix == ".jpg":
		width, height, is_progressive = img_info.get_jpeg_info(img.read_bytes())
	if img.suffix == ".dds":
		width, height, is_dxt1 = img_info.get_dds_info(img.read_bytes())

	if not is_dxt1:
		print("Image must be encoded as DXT1")
		return

	if is_progressive:
		print("Image may not be a progressive JPEG")
		return

	if (width, height) != (1280, 720):
		print(
			"Image must have a width of 1280px and height of 720px, actual "
			f"({width=}px, {height=}px) "
		)
		return

	info = {
		"Version": 15,
		"Author": author_name,
		"ThemeName": theme_name,
	}

	files = {
		f"image{img.suffix}": img.read_bytes(),
	}

	if layout_path:
		layout_json = json.loads(Path(layout_path).read_bytes())
		info["LayoutInfo"] = layout_json["PatchName"] + " by " + layout_json["AuthorName"]
		files["layout.json"] = dump_dict(layout_json)

	info["Target"] = component_name

	files["info.json"] = dump_dict(info)
	sarc_create(files=files, dest_file=out)

	print("Done!")


def dump_dict(json_data: dict) -> bytes:
	"""Format the json files as similar to exelix11/SwitchThemeInjector as possible.

	known issues: elements like "X": 1E-05, are encoded as "X": 1e-05, this is
	reasonable per the json spec https://www.json.org/json-en.html. And has been
	confirmed as working with version 15
	"""
	d = clean_dict(json_data)
	return json.dumps(d, separators=(",", ":")).encode("utf-8")


def clean_dict(d: dict | list | typing.Any) -> dict | list | typing.Any:
	"""
	Recursively removes entries with None or 0 values from a dictionary, including
	nested dictionaries and lists.
	"""

	def cmp(item: typing.Any) -> bool:
		return bool(item) or str(item) == "False"

	if isinstance(d, dict):
		return {k: clean_dict(v) for k, v in d.items() if cmp(v)}
	if isinstance(d, list):
		return [clean_dict(item) for item in d if cmp(item)]

	return d
