# pico_launcher_cover_editor
This repository contains a simple script designed to help create compatible cover images for [Pico Launcher](https://github.com/LNH-team/pico-launcher).

## Usage
1. Place .nds files in the `/roms` directory.
2. Place unprocessed .bmp cover images, named by game ID code, in the `/source_covers` directory. These can be found on [GameTDB](https://www.gametdb.com/DS/Downloads).
3. Navigate within your terminal to the project directory.
4. Execute `pip install -r requirements.txt` to install the required modules.
5. Execute `python pico_launcher_cover_editor.py` to run the script.
6. Processed .bmp files will be saved to the `/processed_covers` directory.
7. Place .nds files in the desired location on your flashcart storage.
8. Place processed cover images in the `/_pico/covers/nds` directory.
