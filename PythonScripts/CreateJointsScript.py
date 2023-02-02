import maya.cmds as cmds

def create_joints():
    """

    creates a joint at each selection(s) transform.
    Returns: [joints]
    """
    selections = cmds.ls(sl=True)
    new_joints = []

    for sel in selections:
        position = cmds.xform(sel, q=True, translation=True, worldSpace=True)
        cmds.select(cl=True)

        jnt = cmds.joint()
        new_joints.append(int)

        cmds.xform(jnt,worldSpace=True, translation=position)

    cmds.select(new_joints, r=True)

    return new_joints

create_joints()
