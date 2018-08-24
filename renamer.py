"""
This utility adds suffixes to objects based on the object type, helping keep our scenes organized.
"""
from maya import cmds
selection = cmds.ls(selection=True, long=True)

print selection
if len(selection) == 0:
    selection = cmds.ls(long=True, dag=True)
    selection.sort(key=len, reverse=True)

for obj in selection:
    shortName = obj.split('|')[-1]

    print "Before rename: ", shortName
    children = cmds.listRelatives(obj, children=True) or []
    if len(children) == 1:
        child = children[0]
        objType = cmds.objectType(child)
    else:
        objType = cmds.objectType(obj)

    if objType == "mesh":
        suffix = 'geo'
    elif objType == "joint":
        suffix = 'jnt'
    elif objType == 'camera':
        print "Skipping camera"
        continue
    else:
        suffix = 'grp'

    newName = shortName+"_"+suffix

    cmds.rename(obj, newName)

    print "After rename: ", newName