# Nxtheme

[Nxtheme-creator Index](../../README.md#nxtheme-creator-index) / [Nxtheme Creator](../index.md#nxtheme-creator) / [Backends](./index.md#backends) / Nxtheme

> Auto-generated documentation for [nxtheme_creator.backends.nxtheme](../../../../nxtheme_creator/backends/nxtheme.py) module.

- [Nxtheme](#nxtheme)
  - [execute](#execute)

## execute

[Show source in nxtheme.py:7](../../../../nxtheme_creator/backends/nxtheme.py#L7)

Use python subprocess to drive the user defined SwitchTheme.exe.

#### Arguments

- `nxthemebin` *str* - path to SwitchTheme.exe
- `component_name` *str* - component to build. eg. home, apps etc
- `image_path` *str* - path to the source image
- `layout_path` *dict* - path to the layout file
- `name` *str* - theme name
- `author_name` *str* - author name
- `out` *str* - destination file name

#### Signature

```python
def execute(
    nxthemebin: str,
    component_name: str,
    image_path: str,
    layout_path: str,
    theme_name: str,
    author_name: str,
    out: str,
) -> None: ...
```