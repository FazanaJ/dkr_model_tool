import sys
import argparse

sys.path.insert(0,'src')
from import_obj import import_obj_model
from export_obj import export_obj_model
from import_dkr_binary import import_dkr_level_binary
from export_dkr_level_binary import export_dkr_level_binary
from preview import preview_level
sys.path.insert(0,'..')

OBJ_EXTENSIONS = '.obj'
LEVEL_BINARY_EXTENSIONS = ('.bin', '.cbin')

def load_model(args):
    lowerPath = args.input.lower()
    if lowerPath.endswith(OBJ_EXTENSIONS):
        return import_obj_model(args)
    elif lowerPath.endswith(LEVEL_BINARY_EXTENSIONS):
        return import_dkr_level_binary(args.input)
    raise SystemExit('Invalid file path "' + path + '"; must end with .obj, .bin, or .cbin')

def preview_model(args):
    preview_level(load_model(args.input))

def convert_model(args):
    model = load_model(args)
    lowerPath = args.output.lower()
    print('Level scale set to ' +str(args.scale))
    if lowerPath.endswith(OBJ_EXTENSIONS):
        print('Converting to OBJ, Please wait...')
        return export_obj_model(model, args)
    elif lowerPath.endswith(LEVEL_BINARY_EXTENSIONS):
        print('Converting to Level Binary, Please wait...')
        return export_dkr_level_binary(model, args)
def main():
    parser = argparse.ArgumentParser(description='Convert/Preview DKR Levels')
    parser.add_argument('input', help='Input file path')
    parser.add_argument('-o', '--output', help='Output file path', required=False)
    parser.add_argument('-s', '--scale', type=int, default=1, help='How many blender units makes 1 ingame unit. Default is 1', required=False)

    args = parser.parse_args()
    if args.output == None:
        preview_model(args)
    else:
        convert_model(args)
    

if __name__ == '__main__':
    main()