import editor
import os
import re
import importlib;

ed_path = editor.get_path()
(filepath, filename) = os.path.split(ed_path)
module = re.sub(r"\..+$",'',filename)

print("re-import module: {}".format(module))
importlib.import_module(module)

