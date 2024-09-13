"""Use python subprocess to drive the user defined SwitchTheme.exe"""

import os
import subprocess


def execute(
	nxthemebin: str,
	component_name: str,
	image_path: str,
	config: dict,
	name: str,
	author_name: str,
	out: str,
):
	cmd = [
		nxthemebin,
		"buildNX",
		component_name,
		image_path,
		config.get(component_name) or "",
		f"name={name}",
		f"author={author_name}",
		f"out={out}",
	]
	if os.name != "nt":  # Not Windows, so run with mono
		cmd = ["mono", *cmd]
	subprocess.run(
		cmd,
		check=False,
	)
