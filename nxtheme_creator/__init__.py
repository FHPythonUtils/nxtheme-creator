"""Generate custom themes for your Nintendo Switch from your images, with optional
configuration for layout adjustments. Specify the path to the `nxtheme` executable
and provide the directory for your input images, output files, and an optional
configuration file."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from nxtheme_creator.process_themes import processImages

THISDIR = Path(__file__).resolve().parent


def cli() -> None:  # pragma: no cover
	"""Cli entry point."""
	parser = argparse.ArgumentParser(description=__doc__)

	parser.add_argument(
		"--nxtheme",
		help="Nxtheme command to use [optional]. eg /path/to/SwitchThemes.exe, obtain from https://github.com/exelix11/SwitchThemeInjector",
	)
	parser.add_argument("--input", help="input directory", default=".")
	parser.add_argument("--output", help="output directory", default="./output")
	parser.add_argument("--config", help="conf.json")

	args = parser.parse_args()

	conf = args.config or str(THISDIR / "conf.json")

	config = json.loads(Path(conf).read_text("utf-8"))

	processImages(
		nxthemebin=args.nxtheme, inputdir=args.input, outputdir=args.output, config=config
	)
