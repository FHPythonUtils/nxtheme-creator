from __future__ import annotations
from pydantic import BaseModel, Field, model_validator


from enum import Enum


SCREEN_TYPES = ["home", "lock", "apps", "set", "user", "news", "psl"]


class ResizeMethod(Enum):
	NORESIZE = "NONE"
	STRETCH = "stretch"
	CENTERCROP = "centerCrop"
	OUTERCROP = "outerCrop"


class ImageMode(Enum):
	BLUR = "blur"
	COLOR = "color"


class LayoutConfig(BaseModel):
	layout: str | None = None
	mode: ImageMode | None = None


class Config(BaseModel):
	home: LayoutConfig = LayoutConfig()
	lock: LayoutConfig = LayoutConfig()
	apps: LayoutConfig = LayoutConfig()
	set: LayoutConfig = LayoutConfig()
	user: LayoutConfig = LayoutConfig()
	news: LayoutConfig = LayoutConfig()
	psl: LayoutConfig = LayoutConfig()
	author_name: str
	resize_method: ResizeMethod = ResizeMethod.NORESIZE

	@model_validator(mode="before")
	@classmethod
	def convert_strings_to_layouts(cls, data:dict):
		for key in SCREEN_TYPES:
			if isinstance(data.get(key), str):
				data[key] = {"layout": data[key]}
		return data
