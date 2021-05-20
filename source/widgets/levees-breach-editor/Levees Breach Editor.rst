Levees Breach Editor
====================

Breach Prescribed
-----------------

|levees014|\ Use the Grid ID tool to pick the levee element to assign a
prescribed breach to.

.. image:: ../../img/Levees-Breach-Editor/levees002.png

From the Levees and Breach Editor, click Prescribed Failure radio button and then click the Levee Grid Elements button.

.. image:: ../../img/Levees-Breach-Editor/levees003.png

The process to apply levee prescribed breach:

1. Add the grid element number of the levee that will initiate the failure.
   Press the eye button.
   (Green)

2. Place the cursor into the levee elevation combo.
   (Orange)

3. Check the Failure check box.
   (Purple)

4. Fill the failure criteria.
   See Data Input Manual for variables use.
   (Blue)

5. Click Apply Change.
   (Red)

.. image:: ../../img/Levees-Breach-Editor/levees004.png

Breach Erosion
--------------

To create Breach Erosion data for the embedded Fread Dam Breach module, set the Failure Mode to Breach Failure.
This action will activate the Breach widget.

.. image:: ../../img/Levees-Breach-Editor/levees005.png

The General breach data is set in the Breach Widget.
Fill the boxes below.

.. image:: ../../img/Levees-Breach-Editor/levees006.png

|levees015|\ Use the Point button to create a Dam Breach Node. Click the
button and then click the breach location on the map.

It is important to apply the breach to the reservoir side of the levee.
Do not apply a breach point on the downstream side of the levee.
In this case, the breach starts in the North direction because the Point is closest to that levee.

.. image:: ../../img/Levees-Breach-Editor/levees007.png

.. image:: ../../img/Levees-Breach-Editor/levees008.png

Click OK to close the Dialog box.
It is not necessary to fill the data here.

.. image:: ../../img/Levees-Breach-Editor/levees009.png

Click the Save icon on the Breach Widget activate the breach editor.
Click the Individual Breach Data Button to fill the dam and breach data into the dialog box.

.. image:: ../../img/Levees-Breach-Editor/levees010.png

.. image:: ../../img/Levees-Breach-Editor/levees011.png

Export the data and check the BREACH.DAT and LEVEE.DAT data files.

LEVEE.DAT should include the Breach Erosion Switch.

.. image:: ../../img/Levees-Breach-Editor/levees012.png

BREACH.DAT should have only the B lines and D lines for general and individual breach data.

.. image:: ../../img/Levees-Breach-Editor/levees013.png

Important notes for Dam Breach Modeling.

1. The cell elevation should be reset to the base floodplain elevation for any cell that represents the breach flow path.
   See the Elevation Correction section for more details.

2. The breach node should be assigned to a node with a levee and the breach direction should be set so that the breach occurs in the downstream
   direction.

3. It is also important to choose a flow direction that contains a levee cutoff.

4. The levee crest elevation is used as the dam crest elevation.
   The base elevation is set by the levee cells where the breach occurs.

.. |levees014| image:: ../../img/Levees-Breach-Editor/levees014.png
.. |levees015| image:: ../../img/Levees-Breach-Editor/levees015.png
