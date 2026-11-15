from PIL import Image
for p in ['characters/intel/expressions.png','characters/amd/expressions.png','characters/nvidia/expressions.png','characters/intel/character_sheet.png']:
    print(p, Image.open(p).size)
