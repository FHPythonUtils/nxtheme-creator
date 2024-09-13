"""Use python subprocess to drive the user defined SwitchTheme.exe."""

import os
import subprocess


def execute(
	nxthemebin: str,
	component_name: str,
	image_path: str,
	layout_path: str,
	theme_name: str,
	author_name: str,
	out: str,
) -> None:
	"""Use python subprocess to drive the user defined SwitchTheme.exe.

	:param str nxthemebin: path to SwitchTheme.exe
	:param str component_name: component to build. eg. home, apps etc
	:param str image_path: path to the source image
	:param dict layout_path: path to the layout file
	:param str name: theme name
	:param str author_name: author name
	:param str out: destination file name
	"""
	cmd = [
		nxthemebin,
		"buildNX",
		component_name,
		image_path,
		layout_path,
		f"name={theme_name}",
		f"author={author_name}",
		f"out={out}",
	]
	if os.name != "nt":  # Not Windows, so run with mono
		cmd = ["mono", *cmd]
	subprocess.run(
		cmd,
		check=False,
	)
