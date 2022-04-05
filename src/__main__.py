import argparse
from valvebsp import Bsp
from valvebsp.lumps import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("path", help="The path of the BSP to deobfuscate.")
    parser.add_argument("-o", "--output", default="", help="Where to save the deobfuscated BSP, overrides by default.")
    parser.add_argument("-ent", "--rip_entities", action="store_true", help="Whether the entity lump should be overwritten with a blank one.")

    args = parser.parse_args()

    print(f"Loading {args.path}...")
    bsp = Bsp(args.path)

    print("Reversing brush obfuscation...")
    for brush in bsp[LUMP_BRUSHES]:
        if brush.numSides == 0:
            # It's trivial really
            brush.numSides = 6

    if args.rip_entities:
        print("Ripping out entities...")
        print("WARNING: If the worldspawn entity is not the first one, this may cause issues and you will have to do it manually.")
        bsp[LUMP_ENTITIES] = [bsp[LUMP_ENTITIES][0]]

    print(f"Saving deobfuscated BSP as {args.output or args.path}...")
    bsp.save(args.output)
    