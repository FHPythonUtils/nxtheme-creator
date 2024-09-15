# Process Themes

[Nxtheme-creator Index](../README.md#nxtheme-creator-index) / [Nxtheme Creator](./index.md#nxtheme-creator) / Process Themes

> Auto-generated documentation for [nxtheme_creator.process_themes](../../../nxtheme_creator/process_themes.py) module.

- [Process Themes](#process-themes)
  - [processImages](#processimages)
  - [resolveConf](#resolveconf)
  - [walkfiletree](#walkfiletree)

## processImages

[Show source in process_themes.py:133](../../../nxtheme_creator/process_themes.py#L133)

Process images from the specified input directory to generate Nintendo Switch themes. This
 function handles the following tasks:
1. Walks through the input directory to collect images and associate them with themes.
2. Resolves and validates configuration paths for layout files.
3. Iterates over each theme and its components, and builds the theme files using the `nxtheme`
 executable.

#### Arguments

- `nxthemebin` *str* - The path to the `nxtheme` executable used for building themes.
- `inputdir` *str* - The directory containing the input images for the themes.
- `outputdir` *str* - The directory where the generated theme files will be saved.
- `config` *dict* - A dictionary containing configuration options such as the author name,
and paths to layout files.

#### Returns

None

#### Signature

```python
def processImages(
    nxthemebin: str | None, inputdir: str, outputdir: str, config: dict
) -> None: ...
```



## resolveConf

[Show source in process_themes.py:95](../../../nxtheme_creator/process_themes.py#L95)

Resolve the file paths for layout configurations specified in the `conf` dictionary.
This function checks if the specified layout files exist. If they do not, it attempts
to find the files in a default `Layouts` directory relative to the `nxthemebin` executable.
If the files are still not found, it tries to append `.json` to the filenames and checks again.

#### Arguments

- `nxthemebin` *str* - The path to the `nxtheme` executable, used to locate the default
 `Layouts` directory.
- `conf` *dict* - A dictionary containing layout configuration. The keys should be screen types
 (e.g., 'home', 'lock') and the values should be file paths or filenames.

#### Returns

Type: *dict*
The updated `conf` dictionary with resolved file paths.

#### Signature

```python
def resolveConf(nxthemebin: str | None, conf: dict) -> dict: ...
```



## walkfiletree

[Show source in process_themes.py:18](../../../nxtheme_creator/process_themes.py#L18)

Create a theme_image_map from an input directory by walking the dir and getting
theme names and corresponding images for each component.

#### Arguments

- `inputdir` *str* - the directory to walk

#### Returns

Type: *dict*
the final theme_image_map

 **Example**:
Given the following directory structure:

```
input_directory/
├── ThemeA/
│   ├── home.jpg
│   ├── lock.jpg
│   └── apps,news.jpg
└── ThemeB/
 ├── home.dds
 └── lock.dds
```

Calling `walkfiletree("input_directory")` would produce:

```json
{
 "ThemeA": {
  "home": "/path/to/input_directory/ThemeA/home.jpg",
  "lock": "/path/to/input_directory/ThemeA/lock.jpg",
  "apps": "/path/to/input_directory/ThemeA/apps,news.jpg",
  "news": "/path/to/input_directory/ThemeA/apps,news.jpg"
 },
 "ThemeB": {
  "home": "/path/to/input_directory/ThemeB/home.dds",
  "lock": "/path/to/input_directory/ThemeB/lock.dds"
 }
}
```

#### Signature

```python
def walkfiletree(inputdir: str) -> dict: ...
```