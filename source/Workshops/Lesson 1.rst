Lesson 1, Part 1 – QGIS FLO-2D Plugin Getting Started
=====================================================

Overview
________

This lesson will outline the process of setting up a FLO-2D project using the Plugin for QGIS.
Setting up the computational domain, creating a grid, interpolating elevation data and spatially variable roughness.

This video will guide you through the lesson.

.. youtube:: vU9qQDuZpfY

Required Data
_____________

The lesson makes use of terrain elevation data, project domain, roughness data, and an inflow hydrograph in the Lesson 1 folders.

.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - **File**
     - **Content**
     - **Location**

   * - Elevation.tif
     - Digital terrain raster
     - \\Example Projects\QGIS Tutorials\QGIS Lesson 1 PRO

   * - Project Domain.shp
     - Polygon for project domain
     -

   * - Mannings n.shp
     - Shapefile for spatially variable roughness
     -

   * - GroverBasinInflow24hr 100yr.txt
     - Inflow data file
     -


\*\ *Project Location C:\Users\Public\Documents\FLO-2D PRO Documentation*

Check these folders to ensure the data is available before starting the lesson.

Step-by-Step Procedure
______________________

To setup a FLO-2D flood simulation use these steps.

1.  Open the QGIS program;

2.  Import the project domain;

3.  Set up the project;

4.  Create the grid;

5.  Save the project

6.  Assign the elevation to the grid;

7.  Assign Manning’s data to the grid;

8.  Assign Control variables;

9.  Save the project;

10.
Export the FLO-2D data files;

11.
Run the FLO-2D model.

Step 1: Open QGIS
_________________

.. image:: ../img/Workshop/Worksh002.png

Search the start menu and run the “QGIS Desktop” program.

Click the New Project icon to load a new map.

.. image:: ../img/Workshop/Worksh003.png


Step 2: Import the project domain
_________________________________

1. Open the project folder

2. Drag the file **Project Domain.shp** onto the map space.
   This will set the CRS to the correct EPSG code.

C:\Users\Public\Documents\FLO-2D PRO Documentation \\Example Projects\QGIS Tutorials\QGIS Lesson 1\Project domain.shp

.. image:: ../img/Workshop/Worksh004.png


Step 3: Set up the FLO-2D project
_________________________________

.. image:: ../img/Workshop/Worksh005.png

1. Click the Set-up icon fill out the dialog box as shown below.
   Set the Grid cell size to 30 ft.

2. Click *Create*.

.. image:: ../img/Workshop/Worksh006.png

3. Save the geopackage file to the project folder.

4. Name the file Lesson 1.gpkg.

..

   **C:\Users\Public\Documents\FLO-2D PRO Documentation\Example Projects\QGIS Tutorials\QGIS Lesson 1**

5. Set the project CRS to Arizona Central (ft).
   Filter the list with an EPSG code: 2223.
   Select EPSG: 2223 and click *OK.*

.. image:: ../img/Workshop/Worksh007.png


6. Wait for the geopackage to write and check the accuracy of the project settings and click *OK*.

Step 4: Create the grid
_______________________

1. From the Grid Tools widget, select *Create Grid*.

.. image:: ../img/Workshop/Worksh008.png


2. Select the Project Domain layer, and the Cell Size field and click OK

.. image:: ../img/Workshop/Worksh009.png

3. Click OK to close.
   The grid is complete.

.. image:: ../img/Workshop/Worksh010.png


Step 5: Save the project
________________________

1. Click the main Save icon on the QGIS toolbar.

.. image:: ../img/Workshop/Worksh011.png


2. Navigate to the Lesson folder, name the project Lesson 1.qgz and click Save.

**C:\Users\Public\Documents\FLO-2D PRO Documentation\Example Projects\QGIS Tutorials\QGIS Lesson 1\Lesson 1.qgz**

Step 6: Assign grid elevation
_____________________________

1. Import the elevation file.
   Open the project folder and drag the **Elevation.tif** file onto the map space.

.. image:: ../img/Workshop/Worksh012.png


2. To interpolate the elevation to a grid layer from a raster layer, use the *Sample Grid Elevation* icon.

.. image:: ../img/Workshop/Worksh013.png


3. Click on the *Sample Grid Elevation* icon and enter the required data in the dialog fields and click *OK*.

4. As shown below, when the elevation sample is complete, the Select the *Fill NoDATA* option to set the elevation of empty grid elements from neighbors.

5. *Sampling Done* dialog box will appear.
   Close it.

.. image:: ../img/Workshop/Worksh153.png
.. image:: ../img/Workshop/Worksh154.png

Step 7: Assign Manning’s data
_____________________________

1. Import the sample roughness file.
   Open the project folder and drag the Mannings n.shp file onto the map space.

.. image:: ../img/Workshop/Worksh014.png


2. Click the Sample Manning’s icon.

.. image:: ../img/Workshop/Worksh015.png


3. Fill the dialog box and click *OK*.
   Once the sample is complete, the following window will appear.
   Close the window.

.. image:: ../img/Workshop/Worksh155.png
.. image:: ../img/Workshop/Worksh156.png

The roughness values and elevations are assigned to the grid layer in the Schematized Layers group.

.. image:: ../img/Workshop/Worksh016.png


Step 8: Assign Control variables
________________________________

1. Click the *Set Control Parameters* Icon.

.. image:: ../img/Workshop/Worksh017.png


2. Fill the dialog box using the two figures below.
   Save the data to the GeoPackage with the *Save* icon.
   The variable descriptions and instructions are presented in the Data Input Manual.

.. image:: ../img/Workshop/Worksh018.png


.. image:: ../img/Workshop/Worksh019.png


Step 9: Save the project
________________________

1. Click the main *Save* icon on the QGIS toolbar.

.. image:: ../img/Workshop/Worksh020.png


Step 10: Export the project
___________________________

1. Save project, then continue to export the project data into the FLO-2D format.

2. Click the *GDS Export* icon.

.. image:: ../img/Workshop/Worksh021.png


3. Navigate to the project folder and click *Select* Folder.

C:\Users\Public\Documents\FLO-2D PRO Documentation\Example Projects\QGIS Tutorials\QGIS Lesson 1\Project Export

Step 11: Run the simulation
___________________________

1. Click on the *Run FLO-2D* icon.

.. image:: ../img/Workshop/Worksh022.png


2. Set the FLO-2D Pro folder.
   **C:\program files (x86)\flo-2d pro**

3. Set the Project folder.
   **C:\users\public\documents\flo-2d pro documentation\Example Projects\QGIS Tutorials\QGIS Lesson 1**

4. Click *OK* to Run the simulation.

.. image:: ../img/Workshop/Worksh023.png


Lesson 1, Part 2 – Project Recovery Methods
-------------------------------------------

.. _overview-1:

Overview
________

Lesson 1, Part 2 is a practical study of managing a FLO-2D project that was constructed using QGIS and the FLO-2D Plugin.

.. _required-data-1:

Required Data
_____________

The lesson has a QGIS project file, Geopackage file, FLO-2D Data Export files and FLO-2D Project Run files.

.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - **File**
     - **Content**
     - **Location**

   * - Lesson 1.qgz
     - Digital terrain raster
     - \\Example Projects\QGIS Tutorials\QGIS Tutorials\QGIS Lesson 1 PRO

   * - Lesson 1.gpkg
     - Polygon for project domain
     -

   * - \*.DAT files
     - Shapefile for spatially variable roughness
     -


\*\ *Project Location C:\Users\Public\Documents\FLO-2D Documentation*

Check these folders to ensure the data is available before starting the lesson.
Lesson 1, Part 1 should be completed first.

.. _step-by-step-procedure-1:

Step-by-Step Procedure
______________________

To create recovery backup system, follow these steps:

1. Create a recovery file;

2. Recover a project;

3. Open project;

4. Load a GeoPackage from previous FLO-2D Plugins build;

5. Recover data from a corrupt GeoPackage file;

Step 1: Create a recovery file
______________________________

1. Open QGIS Lesson 1 in a File Browser.
   Select the **Lesson 1.gpkg** and **Lesson 1.qgz** files and zip them.
   This will create a recovery file.

2. Name the zipped file.
   It is good to choose a name that identifies project progress.
   For Example: **Lesson 1 n-value OK.zip**.

.. image:: ../img/Workshop/Worksh024.png


Step 2: Recover a project
_________________________

This step is used when project data is corrupt.
If a project is not exporting data correctly or a mistake is made, use this method.

1. In the Lesson 1 Folder, select **Lesson 1.gpkg** and **Lesson 1.qgz** and delete them both.

.. image:: ../img/Workshop/Worksh025.png


2. Extract the recovery files.
   The example below uses **Lesson 1 Recovery Files.zip.** Either use this file or the file created in **Step 1**.

.. image:: ../img/Workshop/Worksh026.png


3. Change the name of the path so the file can be extracted directly to the Lesson 1 folder.

.. image:: ../img/Workshop/Worksh027.png


Step 3: Open the project
________________________

1. Open QGIS and drag Lesson 1.qgz onto the canvas the file in QGIS and Load the Project into the FLO-2D Plugin.

.. image:: ../img/Workshop/Worksh028.png


2. Click Yes to load the plugin.

.. image:: ../img/Workshop/Worksh029.png


3. If the project folder changes, open the project but click No on the Load Model box and Yes to load the model from the current directory.

.. image:: ../img/Workshop/Worksh030.png


Lesson 1, Part 3 – Hydrology, Rainfall, and Infiltration
--------------------------------------------------------



Overview
________

This lesson will outline the process for setting up a rainfall runoff model using a 24-hour 100yr storm and rainfall data and spatially variable
infiltration data.
This lesson is a continuation Lesson 1.
If Lesson 1 cannot be loaded, it can be recovered from the Lesson 1 Recovery Files.zip.



Required Data
_____________

The lesson makes use of rainfall distribution, rain arf, landuse and soil data.

.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - **File**
     - **Content**
     - **Location**

   * - SCS 24-Hr Type II
     - Rainfall Distribution Curve
     - \\Example Projects\QGIS Tutorials\QGIS Tutorials\QGIS Lesson 1 PRO\Hydrology

   * - NOAA Atlas 14
     - Rainfall depth reduction
     -

   * - Land use.shp
     - Shapefile for land use
     -

   * - Soil.shp
     - Shapefile for soil type
     -


\*\ *Project Location C:\Users\Public\Documents\FLO-2D PRO Documentation*

Check these folders to ensure the data is available before starting the lesson.

.. _step-by-step-procedure-2:

Step-by-Step Procedure
----------------------

To setup a FLO-2D flood simulation use these steps.

4.  Open the QGIS program;

5.  Load Lesson 1;

6.  Import aerial images;

7.  Assign inflow;

8.  Assign rainfall;

9.  Assign infiltration

10.
Check control variables;

11.
Save the project;

12.
Export the FLO-2D data files;

13.
Run the FLO-2D model.

.. _step-1-open-qgis-1:

.. image:: ../img/Workshop/Worksh002.png

Step 1: Open QGIS
___________________________

Search the start menu and run the “QGIS Desktop” program.

Step 2: Load Lesson 1
_____________________

1. Open the project folder.

2. Drag the file **Lesson 1.qgz** onto the map space.
   If the file is missing.
   Extract it from the zipped recovery file.

**C:\Users\Public\Documents\FLO-2D PRO Documentation\Example Projects\QGIS Tutorials\QGIS Lesson 1\Lesson 1.qgz**

.. image:: ../img/Workshop/Worksh157.png

.. image:: ../img/Workshop/Worksh158.png

3. Click *Yes* to load the model.

.. image:: ../img/Workshop/Worksh031.png


Step 3: Import aerial images
____________________________

Inflow nodes are set up using the Boundary Condition Editor widget.

1. Load an aerial image to help with placement.

2. Use *Quick Map Services Plugin* with the *Contributed Pack* to load aerial images into the layer.

.. image:: ../img/Workshop/Worksh032.png


*Note: If this plugin is not available, aerial images are saved to QGIS Lesson 1/Aerials folder.*

*Note: If you do not see the Google maps, go toQuick Map Services/Settings/More Services/Get Contributed Pack.*

Step 4: Add inflow node
_______________________

1. Zoom in on the top right corner of the project grid.
   Find the Basin Inlet feature.

.. image:: ../img/Workshop/Worksh033.png


2. Click the *Add point BC* icon.

.. image:: ../img/Workshop/Worksh034.png


3. Click the cell indicated on the map in the following image and click *OK* to close the window.

.. image:: ../img/Workshop/Worksh035.png


4. Click *Save* to load the data into the editor.

5. Updated the BC name and the Time series name.

.. image:: ../img/Workshop/Worksh036.png


6. The inflow hydrograph is stored in a text file in the project folder.
   Open this file in Notepad.

**C:\Users\Public\Documents\FLO-2D PRO Documentation\Example Projects\QGIS Tutorials\QGIS Lesson 1\GroverBasinIfnlow 24hr 100yr.txt**

.. image:: ../img/Workshop/Worksh037.png


**CTRL – A** will select all data.

**CTRL – C** will copy the data.

**CTRL – W** will close the file.

.. image:: ../img/Workshop/Worksh038.png


7. *Select* the first cell of the FLO-2D Table Editor Table and click *Paste*.

.. image:: ../img/Workshop/Worksh039.png


8. Schematize the inflow data into the schema layers.

.. image:: ../img/Workshop/Worksh040.png


9. Click OK.

.. image:: ../img/Workshop/Worksh041.png


Step 5: Assign rainfall
_______________________

1. Import the NOAA Atlas rainfall map.
   Open the project folder and drag the **NOAA Atlas 14 24hr 100yr.tif** file onto the map space.

.. image:: ../img/Workshop/Worksh042.png

2. Uniform rainfall requires the total rain in inches or millimeters and a rainfall distribution.
   **Set that to 3.74 Inches**.

3. The rainfall distribution is in a rainfall distribution data file.
   Click the *Import* icon and load the data file from QGIS Lesson 1.

**C:\Users\Public\Documents\FLO-2D PRO Documentation\Example Projects\QGIS Tutorials\QGIS Lesson 1\Hydrology\SCS 24-Hr Type II.DAT**

.. image:: ../img/Workshop/Worksh043.png


.. image:: ../img/Workshop/Worksh159.png
.. image:: ../img/Workshop/Worksh160.png

.. image:: ../img/Workshop/Worksh161.png

4.The rainfall data is imported into the FLO-2D Table Editor.

5. To perform the depth area reduction calculation, use the Area Reduction calculator.

.. image:: ../img/Workshop/Worksh044.png

.. image:: ../img/Workshop/Worksh162.png

1. Click the *Area Reduction* icon.

2. Fill the form and click OK.

3. The raster pixels are typically 1000 by 1000 ft or larger.
   It is not necessary to average the data.
   Fill the dialog box as shown below and click OK to calucate and OK to confirm the data was written to file.

.. image:: ../img/Workshop/Worksh045.png


Step 6: Assign infiltration
___________________________

1. Drag the file **Land Use.shp** onto the map space.

**C:\Users\Public\Documents\FLO-2D PRO Documentation\FLO-2D Pro Documentation\Example Projects\QGIS Tutorials\QGIS Lesson 1\Hydrology\Land Use.shp**

.. image:: ../img/Workshop/Worksh046.png

2. Drag the file **Soil.shp** onto the map space.

**C:\Users\Public\Documents\FLO-2D PRO Documentation\FLO-2D Pro Documentation\Example Projects\QGIS Tutorials\QGIS Lesson 1\Hydrology\Soil.shp**

.. image:: ../img/Workshop/Worksh047.png

3. From the Infiltration Editor click the Global Infiltration icon.

.. image:: ../img/Workshop/Worksh048.png


4. Check the **Global** **Green** **Ampt** switch and fill the global variables.
   The Global variables will be used for any cell that is not defined by the F lines in the spatially variable data assigned to INFIL.DAT.

5. Click **OK** to close.

.. image:: ../img/Workshop/Worksh049.png


6. On the Infiltration Editor click Calculate Green-Ampt.

.. image:: ../img/Workshop/Worksh050.png


7. Specify the attributes as shown in the following image and click OK.
   The calculation process will take 1 to 5 min for this project.

.. image:: ../img/Workshop/Worksh051.png


.. image:: ../img/Workshop/Worksh052.png


Step 7: Check control variables
_______________________________

1. Click the **Control** **Parameters** **Icon**.
   Make sure the **Rain** and **Infiltration** switches are turned on.
   Click **Save** to **Close**.

.. image:: ../img/Workshop/Worksh017.png


.. image:: ../img/Workshop/Worksh053.png


Step 8: Save the project
________________________

1. Click the main Save icon on the QGIS toolbar.

.. image:: ../img/Workshop/Worksh020.png


Step 9: Export the project
__________________________

1. Save project, then continue to export the project data into the FLO-2D format.
   Click the GDS Export icon.
   Navigate to the project folder and click Select Folder.

.. image:: ../img/Workshop/Worksh021.png


**C:\Users\Public\Documents\FLO-2D PRO Documentation\Example Projects\QGIS Tutorials\QGIS Lesson 1\Project Export**

Step 10: Run the simulation
___________________________

1. Click on the *Run FLO-2D* icon.

.. image:: ../img/Workshop/Worksh005.png


2. Set the FLO-2D Pro folder.
   C:\program files (x86)\flo-2d pro

3. Set the Project folder.

**C:\users\public\documents\flo-2d pro documentation\Example Projects\QGIS Tutorials\QGIS Lesson 1\Lesson 1 Export**

.. image:: ../img/Workshop/Worksh054.png


4. This project can be opened in the GDS and tested for accuracy.
