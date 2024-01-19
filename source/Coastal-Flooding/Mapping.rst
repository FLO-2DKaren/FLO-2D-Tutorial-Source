Mapping Results
===============

**Overview**

This tutorial outlines the process of mapping the FLO-2D results.

Required Data

================== ==========================
**File**           **Content**
================== ==========================
\*.out             FLO-2D output files
\*.out             TIMDEP time series output
================== ==========================

Data Location:  \\Coastal Training\\Project Data\\Project Export Folder

Step 1. Simplify map
_____________________

1. Uncheck unnecessary layers like Grid, Elevation, and the user added layers (e.g. Culvert Data, Storm Drain...). Uncheck the following groups:

- Schematic Layers

- Hydraulic Structures

- Storm Drain

.. image:: ../img/Coastal/map017.png

.. tip:: Remove unnecessary layers to emphasize the specific result or feature intended for mapping.

Step 2. Rasterizor
_____________________________________

Rasterizor is a quick mapping tool for FLO-2D output files.
The files should have a standard format with 4 columns ge, x, y, n.
These are grid element number, x coordinate, y coordinate, and n is the mapped value.
It could be water surface elevation, depth, velocity or time to depth.

.. seealso:: The Rasterizor documentation can be found at: `Rasterizor Wiki <https://github.com/FLO-2DKaren/FLO-2D-Rasterizor/wiki>`_

1. Create a group named 'Rasterizor Results' to simplify the management of results.

.. image:: ../img/Coastal/map019.png

2. Open Rasterizor

.. image:: ../img/Coastal/map018.png

3. A file often mapped by Rasterizor is the DEPTH.OUT. Click on the button to load the file.

.. image:: ../img/Coastal/map020.png

.. seealso:: DEPTH.OUT shows the maximum combined channel/floodplain flow depths. More information regarding the output (\*.OUT) files can be found on FLO-2D Data Input Manual.

4. Select this file in the Run/Export Folder.

.. image:: ../img/Coastal/map021.png

3. Create a folder called Rasterizor to save the results and fill the data as the following image. Click Run.

.. image:: ../img/Coastal/map022.png

.. note:: The projection has already been retrieved from the QGIS project.
          However, when mapping results from a blank project in Rasterizor,
          the projection defaults to WGS84. In such cases, the user must manually change it to the correct projection.

4. The DEPTH results will be displayed with a default FLO-2D symbology.

.. image:: ../img/Coastal/map023.png

5. It is possible to change the symbology by right clicking on the layer and selecting Properties.

.. image:: ../img/Coastal/map024.png

6. Navigate to the symbology tab and modify the color ramp for demonstration purposes. Choose either a predefined color ramp or create a custom one.

.. image:: ../img/Coastal/map025.png

7. Here is the exact same data from the DEPTH.OUT but using another symbology.

.. image:: ../img/Coastal/map026.png

.. note:: The default FLO-2D symbology serves as a color reference and can be customized according to the user's preferences.

8. Rasterizor also can map velocities. Select the VELFP.OUT file and click Run.

.. image:: ../img/Coastal/map027.png

.. seealso:: VELFP.OUT shows the maximum floodplain flow velocity. More information can be found on the FLO-2D Data Input Manual.

9. Uncheck the Depth layer and check the velocity results.

.. image:: ../img/Coastal/map028.png

.. tip:: It is possible to use the QGIS Info Tool to check the velocity/depth value.

        .. image:: ../img/Coastal/map029.png

Step 3. MapCrafter
____________________

FLO-2D MapCrafter is designed to transform FLO-2D output files into comprehensive visualizations.
It generates flood maps for single-phase simulations, sediment maps, mudflow maps, and two-phase simulation flood maps.
Additionally, MapCrafter goes beyond by creating hazard maps, highlighting areas with elevated risks based on
FLO-2D simulations, aiding in risk management. The plugin also streamlines the QGIS layout manager process by
automatically generating templates for easy customization.

.. seealso:: The MapCrafter documentation can be found at: `MapCrafter Wiki <https://github.com/FLO-2DSoftware/FLO-2DMapCrafter/wiki>`_

1. Uncheck the 'Rasterizor Results' group. Creating a specific group for MapCrafter is unnecessary as it automatically generates its own group.

2. Open MapCrafter

.. image:: ../img/Coastal/map030.png

3. Select the Run/Export Folder.

.. image:: ../img/Coastal/map031.png

4. Expand the Site Characteristics, Basic, and Channel groups. Select the following variables to be mapped by MapCrafter and click on Create maps.

.. image:: ../img/Coastal/map032.png

.. important:: MapCrafter filters variables for mapping based on the type of simulation,
    including Flood, Sediment, Mudflow, and Two-Phase. The availability of hazard maps depends on the specific type of simulation and the data that is accessible.

5. Please wait for MapCrafter to generate the maps.
   The duration of this process may vary depending on the number of cells and results being mapped. A notification when the operation is complete will be shown.

.. image:: ../img/Coastal/map033.png

6. All MapCrafter results will be displayed within their dedicated group, labeled 'FLO-2D MapCrafter', and subgroups, 'Site Characteristics', 'Basic', 'Channel' ...

.. image:: ../img/Coastal/map034.png

**GROUND ELEVATION**

Maps the ground elevation based on the TOPO.DAT file

.. image:: ../img/Coastal/map035.png

**MAXIMUM DEPTH**

Maps the maximum floodplain depth based on the DEPFP.OUT file

.. image:: ../img/Coastal/map036.png

**FINAL DEPTH**

Maps the final floodplain depth based on the FINALDEP.OUT file

.. image:: ../img/Coastal/map037.png

**MAXIMUM VELOCITY VECTORS**

Maps the maximum velocity vectors based on a combination of the VELFP.OUT and VELDIREC.OUT files

.. image:: ../img/Coastal/map038.png

**FINAL VELOCITY VECTORS**

Maps the final velocity vectors based on a combination of the FINALVEL.OUT and FINALDIR.OUT files

.. image:: ../img/Coastal/map039.png

**MAXIMUM CHANNEL DEPTH**

Maps the maximum channel depth based on the DEPCH.OUT file

.. image:: ../img/Coastal/map040.png

**FINAL CHANNEL DEPTH**

Maps the final channel depth based on the DEPCHFINAL.OUT file

.. image:: ../img/Coastal/map041.png

**MAXIMUM CHANNEL VELOCITY**

Maps the maximum channel velocity based on the VELOC.OUT file

.. image:: ../img/Coastal/map042.png

.. important:: There are numerous other options available for mapping results with MapCrafter.
               The examples provided here are just a demonstration of some results that can be mapped.
               It is recommended to explore additional mapping options based on the user's specific needs.

Step 4. MapCrafter Layouts
_______________________________

The latest MapCrafter version comes with FLO-2D Layouts, a tool that automatizes the creation of QGIS maps by using pre-defined map layouts.

1. Select the FLO-2D Layouts tab. Fill out the information bellow and click on 'Open selected layout'

.. image:: ../img/Coastal/map043.png

.. note:: The available options include A4 and A3 paper sizes, and you can choose between landscape and portrait orientations.

2. A QGIS New Print Layout window will appear with the data filled in the previous step.

.. important:: This layout serves as a starting point and it should be customized according to the user's specific requirements.

.. image:: ../img/Coastal/map044.png

3. To add a legend, click on Add Item and Add Legend. Select a good centered position on the right of the map.

.. image:: ../img/Coastal/map045.png

4. Use the item properties to filter out the unnecessary layers and adjust the legend.

.. image:: ../img/Coastal/map046.png

.. note:: QGIS offers numerous tools and features to enhance map layout, but these are beyond the scope of this training and will not be covered for the sake of time.

5. Once the layout is ready, click on Export as PDF to save the map.

.. image:: ../img/Coastal/map047.png

6. Select the desired file name and folder.

.. image:: ../img/Coastal/map048.png

7. It is possible to select as many layers as desired to export to the pdf, but since a Maximum Depth legend was added, only the Maximum Depth will be selected to be saved.

.. image:: ../img/Coastal/map049.png

.. important:: This is a user's choice; all layers can be exported in one PDF, or multiple PDFs containing separated layers can be exported.

8. Load the pdf to review it.

9. If multiple layers were selected, they will be displayed as layers in the PDF reader.

.. image:: ../img/Coastal/map015.png
