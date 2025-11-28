import ndspy.rom
import os
from PIL import Image

cwd = os.getcwd()
roms_directory = os.path.join(cwd, "roms")
source_covers_directory = os.path.join(cwd, "source_covers")
processed_covers_directory = os.path.join(cwd, "processed_covers")

roms_list = os.listdir(roms_directory)

for rom_file in roms_list:
    rom = ndspy.rom.NintendoDSRom.fromFile(os.path.join(roms_directory, rom_file))
    rom_id = rom.idCode.decode('ascii')
    rom_name = rom.name.decode('ascii')

    try:
        source_cover = os.path.join(source_covers_directory, f"{rom_id}.bmp")
        im = Image.open(source_cover)
        im_size = im.size
        final_x_dim = min(round(im_size[0] * 96 / im_size[1]), 128)
        im1 = im.resize((final_x_dim, 96)) # Resize to height 96, maintain aspect ratio
        result = Image.new(im.mode, (128, 96), (255, 255, 255))
        result.paste(im1, (0, 0)) # Paste resized image onto white background
        result = result.quantize(colors=256, method=2) # Reduce to 256 colors
        result.save(os.path.join(processed_covers_directory, f"{rom_id}.bmp"))
    except FileNotFoundError:
        print(f"Source cover for {rom_name} ({rom_id}) not found.")
        continue
