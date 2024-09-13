"""Get info on supported image types, to perform checks on."""

from __future__ import annotations

import struct


def get_jpeg_info(jpeg: bytes) -> tuple[int, int, bool]:
	SOF0 = b"\xff\xc0"
	SOF2 = b"\xff\xc2"

	idx = 0
	while idx < len(jpeg):
		if jpeg[idx] == 0xFF:
			marker = jpeg[idx : idx + 2]

			if marker in [SOF0, SOF2]:
				height = int.from_bytes(jpeg[idx + 5 : idx + 7], byteorder="big")
				width = int.from_bytes(jpeg[idx + 7 : idx + 9], byteorder="big")

				is_progressive = marker == SOF2

				return width, height, is_progressive

			idx += 2
		else:
			idx += 1

	return 0, 0, False


def get_dds_info(dds: bytes) -> tuple[int, int, bool]:
	if dds[:4] != b"DDS ":
		msg = "Not a valid DDS file."
		raise ValueError(msg)

	# Unpack the relevant parts of the header
	# Width and height are at offsets 12 and 16, FourCC at offset 84
	header = dds[:128]

	height = struct.unpack_from("<I", header, offset=12)[0]
	width = struct.unpack_from("<I", header, offset=16)[0]
	four_cc = struct.unpack_from("<4s", header, offset=84)[0]

	is_dxt1 = four_cc == b"DXT1"

	return width, height, is_dxt1
