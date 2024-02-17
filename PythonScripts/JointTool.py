import maya.cmds as cmds

def create_joint_chain(*args):
 
    num_joints = cmds.intField("numJointsField", query=True, value=True)

    if num_joints <= 0:
        cmds.warning("Please enter a valid number of joints.")
        return

    # Create joint chain
    joints = []
    for i in range(num_joints):
        joint = cmds.joint(name=f"joint_{i + 1}")
        joints.append(joint)

    cmds.select(clear=True)

def create_custom_ui():

    window_name = "customJointChainUI"
    
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name, window=True)

    cmds.window(window_name, title="Custom Joint Chain UI", widthHeight=(300, 100))

    cmds.columnLayout(adjustableColumn=True)

    cmds.text(label="Number of Joints:")
    num_joints_field = cmds.intField("numJointsField", minValue=1, value=3)

    cmds.button(label="Create Joint Chain", command=create_joint_chain)

    cmds.showWindow(window_name)

create_custom_ui()
