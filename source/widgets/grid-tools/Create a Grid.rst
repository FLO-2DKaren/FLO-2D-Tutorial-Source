Create a Grid
=============

1. The first step in creating a FLO-2D grid system is to create the
   *Computational Domain*. The first method is to copy the polygon from
   any polygon layer.

2. Select external polygon layer.

.. image:: ../../img/Create-a-Grid/createagrid1.png
 

3. This method will copy the polygon to the Comp Domain Layer and create
   the grid.

4. The second method is to create a polygon in the *Computational
   Domain* layer in the *Layers Panel*>\ *User Layers*.

.. image:: ../../img/Create-a-Grid/createagrid2.png
   

5. Select the *Toggle Editing* icon from the QGIS Toolbar to activate
   the editor and then click the *Add Feature* button to create a
   polygon.

.. image:: ../../img/Create-a-Grid/createagrid3.png


6. Digitize the polygon in the map canvas and right click to close the
   polygon. Set the grid element size and click *OK* to complete the
   polygon.

|image1|\ |image2|

7. Save the layer and turn off the editor by clicking the Editor tool to
   toggle it off.

.. image:: ../../img/Create-a-Grid/createagrid6.png


8. From the Grid Tools widget, select Create Grid.

.. image:: ../../img/Create-a-Grid/createagrid7.png


9. If this is a new project, the grid system will be created
   automatically. If this is a current project, the user will be asked
   to overwrite the current grid system. Click *Yes* to continue and
   *No* to cancel. Once the grid system is generated, the “Grid
   created!” message will appear. Click *OK* to close.

.. image:: ../../img/Create-a-Grid/createagrid8.png
  

10. If the grid system is not as expected, edit the *Computational
    Domain* layer and repeat the *Create Grid* process. Each time the
    grid system is replaced, the elevation and roughness data are also
    reset and must be recalculated. Each time the grid system is
    replaced, it may be necessary to re-assign the *User Layers* to the
    *Schematic Layers*. The grid system data is saved to the *Grid*
    *Schematic Layer* as shown below.

.. image:: ../../img/Create-a-Grid/createagrid9.png
   :alt: C:\Users\ALEJAN~1\AppData\Local\Temp\SNAGHTML67cc0996.PNG
 

.. |image1| image:: ../../img/Create-a-Grid/createagrid4.png
  
.. |image2| image:: ../../img/Create-a-Grid/createagrid5.png
 
