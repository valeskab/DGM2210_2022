import maya.cmds as cmds

# Build right wall
cmds.polyCube(width=1, height=1, depth=1, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
cmds.scale(1, 20, 24, relative=1)
cmds.move(12, 10, 0, relative=1)

# Build left wall
cmds.polyCube(width=1, height=1, depth=1, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
cmds.scale(1, 20, 24, relative=1)
cmds.move(-12, 10, 0, relative=1)

# Build back wall
cmds.polyCube(name="backWall", width=1, height=1, depth=1, subdivisionsX=2, subdivisionsY=2, subdivisionsZ=2, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
cmds.rotate(0, 90, 0, relative=1, objectSpace=1, forceOrderXYZ=1)
cmds.scale(1, 20, 24, relative=1)
cmds.move(0, 10, -12, relative=1)
cmds.select("backWall.vtx[9:11]", replace=1)
cmds.move(0, 13.143519, 0, relative=1)

# Build front wall
cmds.polyCube(name="frontWall", width=1, height=1, depth=1, subdivisionsX=2, subdivisionsY=2, subdivisionsZ=2, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
cmds.rotate(0, 90, 0, relative=1, objectSpace=1, forceOrderXYZ=1)
cmds.scale(1, 20, 24, relative=1)
cmds.move(0, 10, 12, relative=1)
cmds.select("frontWall.vtx[9:11]", replace=1)
cmds.move(0, 13.143519, 0, relative=1)

# Build floor
cmds.polyCube(width=26, height=1, depth=26, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)

# Build Front left corner edge
cmds.polyCube(width=1.5, height=20, depth=1.5, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
cmds.move(-12.17, 10, 12.17, relative=1)

# Build Front right corner edge
cmds.polyCube(width=1.5, height=20, depth=1.5, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
cmds.move(12.17, 10, 12.17, relative=1)

# Build back left corner edge
cmds.polyCube(width=1.5, height=20, depth=1.5, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
cmds.move(-12.17, 10, -12.17, relative=1)

# Build back right corner edge
cmds.polyCube(width=1.5, height=20, depth=1.5, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
cmds.move(12.17, 10, -12.17, relative=1)

# Build front door
cmds.polyCube(width=8, height=15, depth=1.9, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
cmds.move(0, 7.5, 12, relative=1)
# doorknob
cmds.polySphere(radius=0.5, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], createUVs=2, constructionHistory=1)
cmds.scale(1, 1, -0.5, relative=1)
cmds.move(2.33, 6.75, 13.416, relative=1)
# connecting cylinder
cmds.polyCylinder(r=0.175, h=0.75, sx=20, sy=1, sz=1, ax=[0, 1, 0], rcp=0, cuv=3, ch=1)
cmds.rotate(90, 0, 0, relative=1, objectSpace=1, forceOrderXYZ=1)
cmds.move(2.33, 6.75, 13.075, relative=1)

# Build porch
cmds.polyCube(width=11.2, height=0.6, depth=11.16, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
cmds.move(0, -0.2, 13.275, relative=1)
# Top layer of porch
cmds.polyCube(width=8.75, height=0.75, depth=4.5, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
cmds.move(0, 0.175, 14.4, relative=1)

# Build roof
cmds.polyCube(width=25, height=1, depth=29, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
cmds.move(-6.5, 26.2, 0, relative=1)
cmds.rotate(0, 0, 46.75, relative=1, objectSpace=1, forceOrderXYZ=1)

cmds.polyCube(width=25, height=1, depth=29, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
cmds.move(6.5, 26.2, 0, relative=1)
cmds.rotate(0, 0, -46.75, relative=1, objectSpace=1, forceOrderXYZ=1)
# Roof beam
cmds.polyCube(width=2.115, height=2.115, depth=29.7, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
cmds.move(0, 33, 0, relative=1)
cmds.rotate(0, 0, 45, relative=1, objectSpace=1, forceOrderXYZ=1)