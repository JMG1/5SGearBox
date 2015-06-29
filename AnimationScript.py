#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Javier Martinez Garcia June 2015
from PySide import QtCore

# retrieve the components of the gearbox
MShaft = FreeCAD.ActiveDocument.getObject("Fusion004001")
Gear1 = FreeCAD.ActiveDocument.getObject("Fusion")
Gear2 = FreeCAD.ActiveDocument.getObject("Fusion001")
Gear3 = FreeCAD.ActiveDocument.getObject("Fusion002")
Gear4 = FreeCAD.ActiveDocument.getObject("Fusion003")
Gear5 = FreeCAD.ActiveDocument.getObject("Part__Feature013")
MShaftPlc = MShaft.Placement 

i = 0.0
def Rotate():
  global i 
  MShaft.Placement=FreeCAD.Placement(FreeCAD.Vector(0,0,0), FreeCAD.Rotation(FreeCAD.Vector(0,0,1),-i),FreeCAD.Vector(0,88.5,0))
  # 1º
  Gear1.Placement=FreeCAD.Placement(FreeCAD.Vector(0,0,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),18*i/53.0))
  #2º
  Gear2.Placement=FreeCAD.Placement(FreeCAD.Vector(0,0,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),18*i/37.0))
  #3º
  Gear3.Placement=FreeCAD.Placement(FreeCAD.Vector(0,0,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),21*i/30.0))
  #4º
  Gear4.Placement=FreeCAD.Placement(FreeCAD.Vector(0,0,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),25*i/25.0))
  #5º
  Gear5.Placement=FreeCAD.Placement(FreeCAD.Vector(0,0,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),28*i/23.0))
  
  i += 3.0 # angle increment at each "photogram"
  if i > 360.0:
    # this prevents i from going too big
    i = 0.0


timer = QtCore.QTimer() # create a timer object
timer.timeout.connect(Rotate) # make it call "Rotate()" when triggered
timer.start(50) # trigger every 50 milliseconds



