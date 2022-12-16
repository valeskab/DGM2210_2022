import maya.cmds as cmds


def SequentialRenamer(txt):


    sels = cmds.ls(sl=True)

    if len(sels) > 0:
        count = txt.count("#")
        if count > 0:
            nums = ("#" * count)
            x = txt.partition(nums)
            prefix = x[0]
            suffix = x[2]
            i = 1
            
            for sel in sels:
                num = str(i).zfill(count)
                cmds.select(sel)
                cmds.rename(prefix + num + suffix)
                i += 1
        else:
            cmds.error("String doesn't contain '#'. try again.")
    else:
        cmds.error("No objects were selected, please select an object.")

SequentialRenamer("Leg_####_Jnt")