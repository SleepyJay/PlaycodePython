from working_copy_sync import WorkingCopySync
import sys
import json

# one controller for all

#REPO_NAME        = "ScheduleRA"
#REPO_NAME        = "pv_Python"
REPO_NAME        = "" # GUESS ! :)
REPO_KEY         = "95RRS3A4CU"
CONTOLLER_SCRIPT = "pv_Python/Git2WC2pythonista/controller"
result = 'OK' # TODO: catch failures and change here...

wcs = WorkingCopySync(REPO_NAME, REPO_KEY, CONTOLLER_SCRIPT)

if len(sys.argv) == 1:
    print("REQUIRES ARGV in script defn")
    quit()

elif(sys.argv[1] == 'sync_to'):
    wcs.sync_to_repo()

elif(sys.argv[1] == 'sync_from'):
    wcs.sync_from_repo()

elif(sys.argv[1] == 'update'):
    wcs.replace_text(sys.argv[2], sys.argv[3])

elif(sys.argv[1] == 'list'):
    found = wcs.fetch_repo_file_list()
    # see 'repo_list_callback'

elif(sys.argv[1] == 'list_callback'):
    # We need this callback because of how the `x-url-callback` protocol works.
    repo_list = json.loads(sys.argv[2])
    found     = wcs.find_files(repo_list)
    print("to_repo: '==>', from_repo: '<==', both: '<=>':\n")
    for key in sorted(found):
        print("{} {}".format(found[key], key))
    
    print()

elif(sys.argv[1] == 'list_editor_files'):
    """ONLY show the editor list of files (for this repo)"""
    found = wcs.find_editor_files()
    for key in sorted(found):
        print("\n{}".format(wcs.get_repo_file(key)))

elif(sys.argv[1] == 'custom'):
    # Do some interesting stuff here...possibly even in a different repo...
    #wcs = WorkingCopySync()
    #wcs.fetch_repo_file_list()
    #print("{}".format(wcs.guess_repo()))
    print("{}".format(wcs.repo))
    
elif(sys.argv[1] == 'print_response'):
    """Just print any old response"""
    print("{}".format(sys.argv[2]))

else:
    print("Unknown argv: '" + sys.argv[1] + "'")
    quit()

print("{}: action '{}' for repo '{}'".format(result, sys.argv[1], wcs.repo))




