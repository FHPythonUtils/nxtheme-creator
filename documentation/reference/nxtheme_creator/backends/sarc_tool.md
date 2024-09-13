# Sarc Tool

[Nxtheme-creator Index](../../README.md#nxtheme-creator-index) / [Nxtheme Creator](../index.md#nxtheme-creator) / [Backends](./index.md#backends) / Sarc Tool

> Auto-generated documentation for [nxtheme_creator.backends.sarc_tool](../../../../nxtheme_creator/backends/sarc_tool.py) module.

- [Sarc Tool](#sarc-tool)
  - [clean_dict](#clean_dict)
  - [dump_dict](#dump_dict)
  - [execute](#execute)
  - [sarc_create](#sarc_create)

## clean_dict

[Show source in sarc_tool.py:115](../../../../nxtheme_creator/backends/sarc_tool.py#L115)

Recursively removes entries with None or 0 values from a dictionary, including
nested dictionaries and lists.

#### Signature

```python
def clean_dict(d: dict | list | typing.Any) -> dict | list | typing.Any: ...
```



## dump_dict

[Show source in sarc_tool.py:104](../../../../nxtheme_creator/backends/sarc_tool.py#L104)

Format the json files as similar to exelix11/SwitchThemeInjector as possible.

known issues: elements like "X": 1E-05, are encoded as "X": 1e-05, this is
reasonable per the json spec https://www.json.org/json-en.html. And has been
confirmed as working with version 15

#### Signature

```python
def dump_dict(json_data: dict) -> bytes: ...
```



## execute

[Show source in sarc_tool.py:40](../../../../nxtheme_creator/backends/sarc_tool.py#L40)

Python implementation of SwitchTheme.exe using the sarc lib to do a lot of the heavy lifting.

#### Arguments

- `component_name` *str* - component to build. eg. home, apps etc
- `image_path` *str* - path to the source image
- `layout_path` *dict* - path to the layout file
- `name` *str* - theme name
- `author_name` *str* - author name
- `out` *str* - destination file name

#### Signature

```python
def execute(
    component_name: str,
    image_path: str,
    layout_path: str | None,
    theme_name: str,
    author_name: str,
    out: str,
) -> None: ...
```



## sarc_create

[Show source in sarc_tool.py:27](../../../../nxtheme_creator/backends/sarc_tool.py#L27)

#### Signature

```python
def sarc_create(files: dict[str, bytes], dest_file: str) -> None: ...
```