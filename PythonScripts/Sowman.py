import maya.cmds as cmds
size = 3
# snowman body
cmds.polySphere(radius=size, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], createUVs=2, constructionHistory=1)
cmds.move(0, size, 0, relative=1)

cmds.polySphere(radius=(size - 1), subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], createUVs=2, constructionHistory=1)
cmds.move(0, ((size * 2) + (size -1)), 0, relative=1)

cmds.polySphere(radius=(size - 2), subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], createUVs=2, constructionHistory=1)
cmds.move(0, ((size * 2) + ((size -1)* 2) + (size - 2)), 0, relative=1)

# snowman hat
hatheight = ((size / 2) / 3)

cmds.polyCylinder(radius=(size / 2), height=hatheight, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], roundCap=0, createUVs=3, constructionHistory=1)
cmds.move(0, (size * 4), 0)

cmds.polyCylinder(radius=(size / 2), height=size, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], roundCap=0, createUVs=3, constructionHistory=1)
cmds.move(0, (size * 4.2), 0)
cmds.scale(0.583452, 0.583452, 0.583452)

# snowman eyes
eyes = 0.1

cmds.polyCylinder(radius=eyes, height=eyes, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], roundCap=0, createUVs=3, constructionHistory=1)
cmds.move(-0.4, 11, 0.9, relative=1)
cmds.rotate(90, 0, 0, relative=1, objectSpace=1, forceOrderXYZ=1)

cmds.polyCylinder(radius=eyes, height=eyes, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], roundCap=0, createUVs=3, constructionHistory=1)
cmds.move(0.4, 11, 0.9, relative=1)
cmds.rotate(90, 0, 0, relative=1, objectSpace=1, forceOrderXYZ=1)

# snowman nose
cmds.polyCone(radius= 0.2, height=1, sx=20, sy= 1 ,sz=0, ax=[0, 1, 0], rcp=0, cuv=3, ch=1)
cmds.move(0, 11, 1.4, relative=1)
cmds.rotate(90, 0, 0, relative=1, objectSpace=1, forceOrderXYZ=1)

# snowman arms
cmds.polyCylinder(radius=0.3, height=3, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], roundCap=0, createUVs=3, constructionHistory=1)
cmds.move(-3, 8, 0)
cmds.rotate(0, 0, -76, relative=1, objectSpace=1, forceOrderXYZ=1)

cmds.polyCylinder(radius=0.3, height=3, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], roundCap=0, createUVs=3, constructionHistory=1)
cmds.move(3, 8, 0)
cmds.rotate(0, 0, 76, relative=1, objectSpace=1, forceOrderXYZ=1)
