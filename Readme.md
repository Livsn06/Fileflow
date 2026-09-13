# 📁 FileFlow

<p align="center">
  <strong>A simple and lightweight Python file organization tool.</strong>
  <br>
  Automatically organize your files into folders based on their file type.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/Platform-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.0.0-EDBD53?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-2EA44F?style=for-the-badge)

</p>

---

## ✨ Features

- 📂 Automatically organizes files by type
- 🖥️ Simple Windows CLI
- ⚡ Lightweight and fast
- 🧩 Modular Python architecture
- 🔎 Built-in help command
- 🏷️ Version information
- 🛡️ Explicit `path` command to prevent accidental organization
- ⚙️ Customizable file categories
- 🌍 Can be used globally through Windows `PATH`

---

## 📁 File Categories

FileFlow automatically creates the following folders when matching files are found:

| Category          | Supported Extensions                                              |
| ----------------- | ----------------------------------------------------------------- |
| 🖼️ `images`       | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`, `.webp` |
| 🎬 `videos`       | `.mp4`, `.mkv`, `.flv`, `.avi`, `.mov`, `.wmv`, `.webm`           |
| 📄 `documents`    | `.pdf`, `.doc`, `.docx`, `.txt`, `.ppt`, `.pptx`, `.xls`, `.xlsx` |
| 🎵 `audio`        | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.wma`                   |
| 📦 `archives`     | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`, `.xz`, `.iso`       |
| ⚙️ `applications` | `.exe`, `.msi`, `.apk`, `.dmg`, `.deb`, `.rpm`                    |
| 💻 `codes`        | `.py`, `.js`, `.html`, `.css`, `.java`                            |
| 📁 `Others`       | Unknown or unsupported file types                                 |

---

# 🚀 Installation

## Requirements

Before installing FileFlow, make sure you have:

- Windows
- Python 3.10 or newer
- Git _(optional, but recommended)_

Check your Python installation:

```cmd
python --version
```

Example:

```text
Python 3.13.0
```

---

## 1. Clone the Repository

```cmd
git clone https://github.com/Livsn06/Fileflow.git
```

Go into the project:

```cmd
cd FileFlow
```

Your project should look like:

```text
FileFlow/
│
├── fileflow.bat
├── README.md
│
└── src/
    ├── __init__.py
    ├── main.py
    ├── organizer.py
    └── config.py
```

---

# 🧪 Run FileFlow

You can test FileFlow without adding it to Windows `PATH`.

From the project directory:

### Show Help

```cmd
python -m src.main -h
```

### Show Version

```cmd
python -m src.main -v
```

Output:

```text
FileFlow 1.0.0
```

### Organize a Folder

```cmd
python -m src.main path "C:\Users\YourName\Downloads\Sample"
```

---

# 🖥️ Use FileFlow as a Command

The recommended setup allows you to use:

```cmd
fileflow -h
```

```cmd
fileflow -v
```

```cmd
fileflow path "C:\Users\YourName\Downloads\Sample"
```

from **any directory**.

To do this, add the FileFlow folder to your Windows `PATH`.

---

# ⚙️ Windows PATH Setup

## Step 1 — Locate FileFlow

Find the folder containing:

```text
fileflow.bat
```

For example:

```text
C:\FileFlow
```

Your structure should be:

```text
C:\FileFlow
│
├── fileflow.bat
│
└── src
    ├── __init__.py
    ├── main.py
    ├── organizer.py
    └── config.py
```

---

## Step 2 — Open Environment Variables

Press:

```text
Windows + R
```

Enter:

```text
sysdm.cpl
```

Press **Enter**.

Then:

1. Open the **Advanced** tab.
2. Click **Environment Variables**.
3. Under **User variables**, find `Path`.
4. Select `Path`.
5. Click **Edit**.
6. Click **New**.
7. Enter your FileFlow folder:

```text
C:\FileFlow
```

8. Click **OK**.
9. Click **OK** again to close the remaining windows.

---

## Step 3 — Restart Your Terminal

Close your current CMD or PowerShell window.

Open a **new** terminal.

Run:

```cmd
fileflow -v
```

You should get:

```text
FileFlow 1.0.0
```

🎉 FileFlow is now available as a global command.

---

# 💻 CLI Usage

## Help

```cmd
fileflow -h
```

or:

```cmd
fileflow --help
```

This displays all available commands and options.

---

## Version

```cmd
fileflow -v
```

or:

```cmd
fileflow --version
```

Output:

```text
FileFlow 1.0.0
```

---

## Organize a Folder

Use the `path` command:

```cmd
fileflow path "C:\Users\YourName\Downloads\Sample"
```

You can also use:

```cmd
fileflow path "Downloads\Sample"
```

If the path contains spaces, always use quotation marks:

```cmd
fileflow path "C:\Users\YourName\My Files"
```

---

# 🛡️ Why Use `path`?

FileFlow intentionally requires the `path` command:

```cmd
fileflow path "Downloads"
```

instead of:

```cmd
fileflow "Downloads"
```

This makes the command more explicit and helps prevent accidental organization.

It also makes it easier to add more commands in the future:

```text
fileflow path "Downloads"
fileflow scan "Downloads"
fileflow config
```

---

# 📊 Example

### Before

```text
Sample/
│
├── photo.jpg
├── vacation.png
├── video.mp4
├── report.pdf
├── music.mp3
├── project.zip
└── script.py
```

Run:

```cmd
fileflow path "Sample"
```

### After

```text
Sample/
│
├── images/
│   ├── photo.jpg
│   └── vacation.png
│
├── videos/
│   └── video.mp4
│
├── documents/
│   └── report.pdf
│
├── audio/
│   └── music.mp3
│
├── archives/
│   └── project.zip
│
└── codes/
    └── script.py
```

---

# 🏗️ Project Structure

```text
FileFlow/
│
├── fileflow.bat
├── README.md
│
└── src/
    │
    ├── __init__.py
    │
    ├── main.py
    │
    ├── organizer.py
    │
    └── config.py
```

### `fileflow.bat`

The Windows launcher.

```bat
@echo off
cd /d "%~dp0"
python -m src.main %*
```

It allows FileFlow to work regardless of where the project is installed.

---

### `src/main.py`

The main CLI entry point.

Responsible for:

- CLI argument parsing
- Commands
- Version information
- Folder validation
- Calling the organizer

---

### `src/organizer.py`

Contains the actual organization logic.

Responsible for:

- Reading files
- Checking file extensions
- Determining categories
- Creating folders
- Moving files

---

### `src/config.py`

Contains the supported file extensions and categories.

This allows file types to be changed without modifying the main organizing logic.

---

### `src/__init__.py`

Marks `src` as a Python package.

It can remain empty:

```python
# src/__init__.py
```

---

# 🔄 How FileFlow Works

```text
                 User
                   │
                   ▼
      fileflow path "Downloads"
                   │
                   ▼
             fileflow.bat
                   │
                   ▼
              src/main.py
                   │
                   ▼
            Parse command
                   │
                   ▼
            Validate path
                   │
                   ▼
          src/organizer.py
                   │
          ┌────────┴────────┐
          ▼                 ▼
     Check extension    Find category
          │                 │
          └────────┬────────┘
                   ▼
          Create category folder
                   │
                   ▼
              Move file
```

---

# ⚙️ Customizing File Types

Open:

```text
src/config.py
```

You can add additional extensions to an existing category.

Example:

```python
"images": [
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".heic"
]
```

You can also create a new category:

```python
"design": [
    ".fig",
    ".psd",
    ".ai"
]
```

FileFlow will then organize those files into:

```text
design/
```

---

# ⚠️ Important

FileFlow **moves** files rather than copying them.

Before using FileFlow on important folders, test it with a sample folder first.

For example:

```text
Downloads/
└── Sample/
```

Put some test files inside `Sample` and run:

```cmd
fileflow path "Downloads\Sample"
```

### Unknown file types

Files that don't match a configured extension are placed into:

```text
Others/
```

---

# 🛠️ Development

Clone the repository:

```cmd
git clone https://github.com/YOUR-USERNAME/FileFlow.git
```

Enter the project:

```cmd
cd FileFlow
```

Run the help command:

```cmd
python -m src.main -h
```

Run a test:

```cmd
python -m src.main path "C:\Path\To\TestFolder"
```

FileFlow currently uses only Python's standard library, so no additional packages are required.

---

# 🗺️ Roadmap

- [ ] Duplicate file handling
- [ ] `--dry-run` mode
- [ ] Better logging
- [ ] Recursive folder organization
- [ ] More file categories
- [ ] Custom configuration
- [ ] Interactive mode
- [ ] Unit tests
- [ ] Python package installation
- [ ] Cross-platform support
- [ ] Additional CLI commands

---

# 🎯 Project Purpose

FileFlow started as a practical project for learning **Python automation**.

The project is designed to provide hands-on experience with:

- 🐍 Python
- 📂 File and directory manipulation
- `pathlib`
- `argparse`
- Python modules
- Python packages
- Error handling
- Windows batch scripting
- Environment variables
- Windows `PATH`
- Git and GitHub
- CLI application design
- Clean project architecture
- Automation concepts

The goal is not only to create a file organizer, but to build a foundation for creating more practical automation tools in Python.

---

<p align="center">
  <strong>FileFlow</strong>
  <br>
  Move less. Organize more. ⚡
</p>
