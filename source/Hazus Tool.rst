
\***Jasmine, This one has a note, and bullets. Might want to verify the headings are level 1 or 2.
==================================================================================================

Hazus Tool
==========

The Hazus tool is used to generate water surface elevation or flow depth
rasters for the FEMA Hazus program.

Building Layer
--------------

1. Add building layer from a shapefile.

2. Click the *Add a Vector Layer* button. Navigate to the building
   shapefile and add it to the map. If the layer does not have a CRS
   assigned, a prompt will allow it to be assigned.

.. image:: img/hazustool1.png


Import Depth and Water Surface Layers.
--------------------------------------

3. Add a depth layer and a water surface layer. Click *Layer*>\ *Add
   Layer*>\ *Add Delimited Text Layer* to import the files DEPTH.OUT and
   MAXWSELEV.OUT.

|image1|\ |image2|

4. Right click the layer and assign the Coordinate Reference System.

|image3|\ |C:\Users\ALEJAN~1\AppData\Local\Temp\SNAGHTML2dc68f89.PNG|

5. Repeat this process for the DEPFP.OUT file.

*Assign Water Elevation and Depth to the Grid Layer*
----------------------------------------------------

6. On the Grid Tools widget select the Assign water elevations/flow
   depths to grid from points layer icon.

.. image:: img/hazustool6.png


7. Edit the dialog box as shown below and click the Assign to selected
   grid field button.

.. image:: img/hazustool7.png
   :alt: C:\Users\ALEJAN~1\AppData\Local\Temp\SNAGHTML2ddb3cfe.PNG


8. Click OK to close the dialog box.

.. image:: img/hazustool8.png
   :alt: C:\Users\ALEJAN~1\AppData\Local\Temp\SNAGHTML2dde7815.PNG
   

9.  Repeat the process for the Depth layer.

10. On the *Grid Tools* widget select the *Assign water elevations/flow
    depths to grid from points layer* button.

.. image:: img/hazustool6.png
   

11. Edit the dialog box as shown below and click the *Assign to selected
    grid field* button.

.. image:: img/hazustool9.png


12. Click *OK* to close the dialog box.

.. image:: img/hazustool8.png
   :alt: C:\Users\ALEJAN~1\AppData\Local\Temp\SNAGHTML2dde7815.PNG
 

Intersect Building Layer to Grid
--------------------------------

13. Use the *QGIS Vector* Menu to set up the intersection. Click
    *Vectors*>\ *GeoProcessing Tools*>\ *Intersection*.

.. image:: img/hazustool10.png
   

14. Set up the intersection dialog box as shown below. Click *Run* to
    make the intersection. This process adds the Intersection layer to
    the map automatically.

.. image:: img/hazustool11.png

Review Intersection Layer
-------------------------

15. The new *Intersection* layer has fields from both the *Buildings*
    and *Grid* layers:

.. image:: img/hazustool12.png


16. Each building polygon that intersects the grid has several
    partitions (polygons) with different elevations. The following
    building has 7 partitions with different data from each grid:

.. image:: img/hazustool13.jpeg
   :alt: HAZUS3
   

17. Each partition of the building has, different field values. For
    example, HOUSE_ID “1” in the Features Table, has different
    ‘elevation’, ‘water_elev’, and ‘flow_depth’:

.. image:: img/hazustool14.png
  

Homogenize the Intersection layer.
----------------------------------

18. Select the HAZUS icon in the *FLO-2D Toolbar*.

.. image:: img/hazustool15.png


19. Fill the dialog box as shown below and click the *Compute and Show
    Building Statistics* button.

.. image:: img/hazustool16.png

*Note: The ‘Finished floor global adjustment factor’ value will be added
to the ground elevations, if selected.*

20. Click OK to close the message dialog box.

.. image:: img/hazustool17.png


21. The Hazus tool calculates the statistics of the buildings polygons.
    It computes the following data for each building.

-  Ground elevation (min, max, mean);

-  First floor elevation (min, max, mean);

-  Water surface elevation (min, max, mean);

-  Depth (min, max, mean).

.. image:: img/hazustool18.png


.. image:: img/hazustool19.png
   :alt: C:\Users\ALEJAN~1\AppData\Local\Temp\SNAGHTML3180a766.PNG

Join Building Statistics Table to Building Polygons
---------------------------------------------------

22. Right click the *Buildings* layer and click *Properties*. *Add a
    Join* to the layer. Click *OK* and Close the *Properties* window.

.. image:: img/hazustool20.png
 

.. image:: img/hazustool21.png
   :alt: C:\Users\ALEJAN~1\AppData\Local\Temp\SNAGHTML318e5ee0.PNG


23. Save the *Buildings* Layer to a shapefile. Select the *Save As…* to
    a location and name the file.

Note: The style of this new layer can be edited to help the user review
the data. The attributes can be sorted and arranged to help track
outliers or bad data. Use the field calculator to perform additional
statistical analysis on the data in this layer.

.. image:: img/hazustool22.png


.. image:: img/hazustool23.png
   :alt: C:\Users\ALEJAN~1\AppData\Local\Temp\SNAGHTML31a1bf72.PNG


24. Now, the Buildings Shapefile has “join” fields from the Buildings
    Statistics table:

.. image:: img/hazustool24.png


Rasterize the Buildings
-----------------------

25. On the Main QGIS Menu, click *Processing*>\ *Toolbox*.

.. image:: img/hazustool25.png


26. Enter the search term *Rasterize* in the Processing Toolbox search
    field. Double click the *Saga Rasterize* tool. Saga>Raster Creation
    Tools>Rasterize.

.. image:: img/hazustool26.png


27. Change the dialog box as shown below and click *Run*.

.. image:: img/hazustool27.png


.. |image1| image:: img/hazustool2.png

.. |image2| image:: img/hazustool3.png
 
.. |image3| image:: img/hazustool4.png
 
.. |C:\Users\ALEJAN~1\AppData\Local\Temp\SNAGHTML2dc68f89.PNG| image:: img/hazustool5.png

