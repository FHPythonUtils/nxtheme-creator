# Datamodels

[Nxtheme-creator Index](../README.md#nxtheme-creator-index) / [Nxtheme Creator](./index.md#nxtheme-creator) / Datamodels

> Auto-generated documentation for [nxtheme_creator.datamodels](../../../nxtheme_creator/datamodels.py) module.

- [Datamodels](#datamodels)
  - [Config](#config)
    - [Config.convert_strings_to_layouts](#configconvert_strings_to_layouts)
  - [ImageMode](#imagemode)
  - [LayoutConfig](#layoutconfig)
  - [ResizeMethod](#resizemethod)

## Config

[Show source in datamodels.py:27](../../../nxtheme_creator/datamodels.py#L27)

#### Signature

```python
class Config(BaseModel): ...
```

### Config.convert_strings_to_layouts

[Show source in datamodels.py:38](../../../nxtheme_creator/datamodels.py#L38)

#### Signature

```python
@model_validator(mode="before")
@classmethod
def convert_strings_to_layouts(cls, data: dict): ...
```



## ImageMode

[Show source in datamodels.py:18](../../../nxtheme_creator/datamodels.py#L18)

#### Signature

```python
class ImageMode(Enum): ...
```



## LayoutConfig

[Show source in datamodels.py:22](../../../nxtheme_creator/datamodels.py#L22)

#### Signature

```python
class LayoutConfig(BaseModel): ...
```



## ResizeMethod

[Show source in datamodels.py:11](../../../nxtheme_creator/datamodels.py#L11)

#### Signature

```python
class ResizeMethod(Enum): ...
```