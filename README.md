# Calculator App

A simple calculator app with GUI that supports multiple numbers and various operations.

## Features
- Enter multiple numbers (space or comma separated)
- Choose from operations: +, -, *, /, %, **, //
- Handles errors like invalid input and division by zero

## How to Run
1. Download the executable from the [Releases](https://github.com/YOUR_USERNAME/YOUR_REPO/releases) page.
2. Run the file (no installation needed).
3. Enter numbers, select operation, click Calculate.

## For Developers
- Requires Python 3.x and Tkinter.
- Run `python3 calculator.py` to start the GUI.

## Building from Source
To create a downloadable executable:
1. Install PyInstaller: `pip install pyinstaller` (or use venv/pipx).
2. Run: `pyinstaller --onefile --windowed calculator.py`
3. Find the executable in `dist/` folder.

## Publishing
This app is published via GitHub Releases. To create a new release:
1. Update version in code if needed.
2. Create a git tag: `git tag v1.0.1`
3. Push tag: `git push origin v1.0.1`
4. GitHub Actions will build executables for Windows, macOS, and Linux.
5. Go to Releases and publish the draft release with the attached assets.