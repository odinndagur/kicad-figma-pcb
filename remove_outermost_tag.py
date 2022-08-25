import os
import sys

args = sys.argv[1:]
if os.path.isfile(args[0]):
    filename = args[0]

# filename = '/Users/odinndagur/Documents/figma-island-lol 2.svg'
name,ext = os.path.splitext(os.path.basename(filename))
dirname = os.path.dirname(filename)

with open(filename) as f:
    data = f.read()

print(f'filename: {filename}\nbasename: {name}')

end_tag = '</g>'

if f'<g id="{name}">\n' in data:
    modified_name = name + '_modified' + ext
    print(f'found <g id="{name}">\n tag, removing, saving as {modified_name}\nfull path: {os.path.join(dirname,modified_name)}')
    out = data.replace(f'<g id="{name}">\n','')
    lastPos = out.rfind(end_tag)
    out = out[:lastPos] + out[lastPos+len(end_tag):]
    out_path = os.path.join(dirname,modified_name)
    with open(out_path,'w') as f:
        f.write(out)
    print('done!')
