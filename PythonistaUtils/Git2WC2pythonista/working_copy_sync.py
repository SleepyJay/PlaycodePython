from collections import OrderedDict, namedtuple
import editor
import re
from urllib.parse import urlencode, quote
import webbrowser
import os
import json

class WorkingCopySync(object):
    #
    def __init__(self, repo, key, controller):
        self.key = key
        self.contoller_script = controller
        self.ParsedPath = namedtuple("ParsedPath", ["full", "doc_root", "base_dir", "local_dir", "file"] )
        self.repo = repo or self.guess_repo()

    #
    def sync_to_repo(self, file_path=None, askcommit=0, overwrite=1):
        file_path = self.get_repo_file(file_path)

        params              = self.get_base_URL(file_path)
        params["x-success"] = "pythonista://"
        params["text"]      = editor.get_text()
        params["askcommit"] = askcommit
        params["overwrite"] = overwrite

        url = "working-copy://x-callback-url/write/?" + urlencode(params, quote_via=quote)
        webbrowser.open(url)

    #
    def sync_from_repo(self, repo_path=None, editor_path=None):
        repo_path = self.get_repo_file(repo_path)
        editor_path = self.get_editor_file()

        params              = self.get_base_URL(repo_path)
        params["command"]   = "pull"
        params["command"]   = "read"
        params["x-success"] = "pythonista://{}?action=run&argv={}&argv={}&argv=".format(
            self.contoller_script, "update", editor_path)

        url = "working-copy://x-callback-url/chain/?" + urlencode(params, quote_via=quote)
        webbrowser.open(url)

    #
    def fetch_repo_file_list(self, unchanged=1):
        params              = self.get_base_URL()
        params["x-success"] = "pythonista://{}?action=run&argv={}&argv=".format(
            self.contoller_script, "list_callback")
        params["unchanged"] = unchanged

        url = "working-copy://x-callback-url/status/?" + urlencode(params, quote_via=quote)
        webbrowser.open(url)

    #
    def get_base_URL(self, file_path=None):
        params = OrderedDict()
        params["key"]   = self.key
        params["repo"]  = self.repo

        if file_path:
            params["path"] = file_path

        return params

    #
    def replace_text(self, file_path, file_text):
        editor.open_file(self.get_full_file())
        text_length = len(editor.get_text())
        editor.replace_text(0, text_length, file_text)

    #
    def find_files(self, repo_files=None):
        found = {}
        editor_files = self.find_editor_files()

        for name in editor_files:
            found[name] = '==>'

        if repo_files:
            for item in repo_files:
                if item['kind'] == 'repository': continue
                if item['kind'] == 'directory': continue
                
                #print("{}".format(item))
                name = os.path.join(self.repo, item['path'])
                if name in found:
                    found[name] = '<=>'
                else:
                    found[name] = '<=='
        return found

    #
    def find_repo_files(self):
        found = set()
        path = self.get_walking_path()
        for root, dir, files in os.walk(path):
            if re.search('/__pycache__', root): continue
            if re.search('/.git', root): continue

            for name in files:
                if re.search('.DS_Store', name): continue
                found.add(name)

        return found

    #
    def find_editor_files(self):
        found = set()
        path = self.get_walking_path()
        for root, dir, files in os.walk(path):
            if re.search('/__pycache__', root): continue
            if re.search('/.git', root): continue

            for name in files:
                if re.search('.DS_Store', name): continue
                
                found.add(self.get_editor_file(os.path.join(root,name)))

        return found

    #
    def parsePath(self, path=None, base_dir="Documents"):
        # /<blah, blah>/Pythonista3/Documents/pv_Python/Git2WC2pythonista/working_copy_sync.py
        # ==> (namedTuple ["doc_root", "base_dir", "local_dir", "file"] )
        # [ "/<blah, blah>/Pythonista3/Documents", "pv_Python", "Git2WC2pythonista", "working_copy_sync.py" ]

        path = path or self.get_full_file()
        (filepath, filename) = os.path.split(path)
        path_re = re.compile(r"^(\/.+\/{})\/(.+)$".format(base_dir))

        # TODO: check for edge cases?
        m = path_re.match(filepath)

        doc_root = m.group(1)
        parts    = m.group(2).split('/')

        base_dir  = parts[0]
        local_dir = ""

        if len(parts) > 1:
            local_dir = '/'.join(parts[1:])

        return self.ParsedPath(path, doc_root, base_dir, local_dir, filename)

    #
    def get_walking_path(self, path=None):
        p_path = self.parsePath(path)
        return os.path.join(p_path.doc_root, p_path.base_dir)

    #
    def get_editor_path(self, path=None):
        p_path = self.parsePath(path)
        return os.path.join(p_path.base_dir, p_path.local_dir)    

    #
    def get_repo_file(self, path=None):
        p_path = self.parsePath(path)
        return os.path.join(p_path.local_dir, p_path.file)

    #
    def get_editor_file(self, path=None):
        p_path = self.parsePath(path)
        return os.path.join(p_path.base_dir, p_path.local_dir, p_path.file)

    #
    def get_base_path(self, path=None):
        p_path = self.parsePath(path)
        return os.path.join(p_path.doc_root, p_path.base_dir)

    #
    def get_full_file(self):
        return editor.get_path()
        
    #
    def guess_repo(self):
        p_path = self.parsePath()
        return p_path.base_dir






