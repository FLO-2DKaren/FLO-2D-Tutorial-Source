Area and Width Reduction Factor – Buildings
===========================================

Overview
~~~~~~~~

Buildings are only calculated from the *Blocked Areas* layer in the *User Layers* group.
The blocked areas are polygons that represent buildings or other features that displace and redirect the flow as it moves over an area.
The blocked areas are converted to FLO-2D Area Reductions Factors (ARF) and Width Reduction Factors (WRF) in the Schematic Layer.

Digitize or Copy Data
---------------------

Use the editor and *Create Polygon* tool to digitize or outline buildings with polygons.
If the buildings are in another layer, copy the polygons from the external layer and paste it into the *Blocked Areas* layer.
Select *Buildings* from the external layer.
If there are multiple types of polygons in the layer, it is possible to select the building by attribute type.
Copy the selected polygons using Left Click Feature or Map Canvas and Ctrl C.

.. image:: ../../img/Area-and-Width-Reduction-Factor-Buildings/areaandwidthreductionfactorbuildings002.png

Highlight the *Blocked Areas* layer and click the *Toggle Editing* icon.
Paste the selected polygons into the *Blocked Areas* layer.
Left Click Canvas and Ctrl V.

.. image:: ../../img/Area-and-Width-Reduction-Factor-Buildings/areaandwidthreductionfactorbuildings003.png


Click the *Toggle Editing* icon again to save and close the editor.
The blocked layers attribute table can be edited to add:

-  Building collapse;

-  ARF switch (0 will skip the ARF and 1 will calculate the ARF);

-  WRF switch (0 will skip the WRF and 1 will calculate the WRF).

Use a table join or spatial join to fill the attribute data if it is available in an alternate layer.
Commands and tutorials for these tools are available on the QGIS Tutorials website: `www.qgistutorials.com <http://www.qgistutorials.com>`__.

Calculate ARF and WRF layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../img/Area-and-Width-Reduction-Factor-Buildings/areaandwidthreductionfactorbuildings004.png


Click the *Evaluate Reduction Factors (ARF and WRF)* icon.
There are two options.
Use the Blocked Areas Layer if constructing polygons from the digitizing tools.
Use the external polygon layer if building polygons are in another layer.

.. image:: ../../img/Area-and-Width-Reduction-Factor-Buildings/areaandwidthreductionfactorbuildings005.png


Click OK and wait for the procedure to finish.
The following message will appear and click *OK* to close it.

.. image:: ../../img/Area-and-Width-Reduction-Factor-Buildings/areaandwidthreductionfactorbuildings006.png
 

The ARF and WRF features are visible in the *Schematic Layers* group.

.. image:: ../../img/Area-and-Width-Reduction-Factor-Buildings/areaandwidthreductionfactorbuildings007.png

Click on the Set Control Parameters icon, and then on the Control Variables (CONT.DAT) tab Check on Area Reduction Factors (ARF) and then click Save.

.. image:: ../../img/Area-and-Width-Reduction-Factor-Buildings/areaandwidthreductionfactorbuildings008.png

Troubleshooting
~~~~~~~~~~~~~~~

1. Missing building polygons from the *Blocked Areas* layer can be created.

2. If the *Grid* layer is empty, create a grid and try again.

3. If a Python error appears during the sampling procedure, the attribute table may be missing.
   Save and reload the project and try again.

4. If a polygon is outside the computational domain, it might result in an error.
   Delete buildings outside the computational domain.
