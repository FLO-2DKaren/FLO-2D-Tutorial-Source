Lesson 1 Part 2 – Project Recovery Methods
==========================================

.. _overview-1:

Overview
________

Lesson 1, Part 2 is a practical study of managing a FLO-2D project that was constructed using QGIS and the FLO-2D Plugin.
Use this tutorial to learn how to build a recovery or backup point and recover corrupted data.

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
     - QGIS file
     - QGIS Lesson 1

   * - Lesson 1.gpkg
     - FLO-2D GeoPackage
     -

   * - \*.DAT files
     - FLO-2D data files
     -


Project Location C:\\Users\\Public\\Documents\\FLO-2D PRO Documentation\\Example Projects\\QGIS Tutorials\\

Check these folders to ensure the data is available before starting the lesson.
Lesson 1, Part 1 should be completed first.

.. _step-by-step-procedure-1:

Step-by-Step Procedure
______________________

To create recovery backup system, follow these steps:

1. Create a recovery file;
2. Recover a project;
3. Open project.

Step 1: Create a recovery file
______________________________

1. If the QGIS is still open, save and close it.

2. Open QGIS Lesson 1 in a File Browser.
   Select the Lesson 1.gpkg and Lesson 1.qgz files and zip them.
   This will create a recovery file.

3. Name the zipped file.
   It is good to choose a name that identifies project progress.
   For Example: Lesson 1 n-value OK.zip.

4. Repeat this step after any time a Backup or Recovery Point is desired.

.. image:: ../img/Workshop/Worksh024.png


Step 2: Recover a project
_________________________

This step is used when project data is corrupt.
If a project is not exporting data correctly or a mistake is made, use this method.

1. In the Lesson 1 Folder, select Lesson 1.gpkg and Lesson 1.qgz and delete them both.

.. image:: ../img/Workshop/Worksh025.png


2. Extract the recovery files.
   The example below uses Lesson 1 Recovery Files.zip. Either use this file or the file created in Step 1.

.. image:: ../img/Workshop/Worksh026.png


3. Change the name of the path so the file can be extracted directly to the Lesson 1 folder.

.. image:: ../img/Workshop/Worksh027.png


Step 3: Open the project
________________________

.. image:: ../img/Workshop/Worksh002.png

1. Open QGIS and drag Lesson 1.qgz onto the canvas the file in QGIS and Load the Project into the FLO-2D Plugin.

.. image:: ../img/Workshop/Worksh028.png


2. Click Yes to load the plugin.

.. image:: ../img/Workshop/Worksh029.png


**Note:  If the project path changes, the plugin will recognize the path change and try to load the model from the new path.**


**Note:  If the project path changes but an old geopackage remains in the previous path, it will be loaded and can corrupt the project.**

.. image:: ../img/Workshop/Worksh030.png

