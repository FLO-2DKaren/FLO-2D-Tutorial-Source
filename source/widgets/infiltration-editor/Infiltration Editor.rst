Infiltration Editor
===================

Green-Ampt
----------

The Green-Ampt infiltration editor can add global or spatially variable infiltration data to the INFIL.DAT file.

Global
------

Global data is set up using the Global Infiltration button.
Click the button to open the editor dialog box.

.. image:: ../../img/Infiltration-Condition-Editor/infilt002.png

.. image:: ../../img/Infiltration-Condition-Editor/infilt003.png

Channel Infiltration
--------------------

To assign channel infiltration, use the channel infiltration editor.
Set a global hydraulic conductivity for all channel elements and click the Channel Infiltration button.

.. image:: ../../img/Infiltration-Condition-Editor/infilt004.png

Local channel infiltration is set by segment in the dialog box.

.. image:: ../../img/Infiltration-Condition-Editor/infilt005.png

Green-Ampt from Infiltration Polygons
-------------------------------------

Spatially variable floodplain infiltration is set by digitizing infiltration polygons or importing infiltration polygons.
Use the polygon editor to digitize spatially variable infiltration.
Create a polygon to represent an area of infiltration.

1. |infilt019|\ Click the create a polygon tool and digitize a polygon.

2. |infilt020|\ Name the infiltration polygon.

3. Fill the table for the infiltration data.

4. Click *Save*.

5. |infilt021|\ Click Schematize.

.. image:: ../../img/Infiltration-Condition-Editor/infilt006.png

The infiltration polygons outline areas of cells that have similar infiltration characteristics.
In the following image, the infiltration areas are different for urban, desert and desert drainage.

.. image:: ../../img/Infiltration-Condition-Editor/infilt007.png

Green-Ampt from Infiltration Calculator
---------------------------------------

To use the Green-Ampt calculator, the user must prepare soil and landuse shapefiles.
The soils data is acquired from the United States Department of Agriculture Web Soil Survey (USDA, 2017).
The data is organized by soil group.

The land use data can be acquired from various sources but is generally available from the United States Geological Survey Land Cover website (USGS,
2017).
The land use data can account for vegetative cover and impervious cover.

Prepare the data into shapefiles using QGIS or import them into QGIS.

.. image:: ../../img/Infiltration-Condition-Editor/infilt008.png

To run the calculator, click the Calculate Green-Ampt button.

.. image:: ../../img/Infiltration-Condition-Editor/infilt009.png

Use the following dialog box to assign the required shapefiles and fields to the calculator.
Click OK to run the calculation.
The plugin will assign spatially variable infiltration data to each cell.
The data is exported to the INFIL.DAT file.

.. image:: ../../img/Infiltration-Condition-Editor/infilt010.png

SCS
---

.. _global-1:

Global
~~~~~~

The SCS infiltration editor can add global or spatially variable infiltration data to the INFIL.DAT file for infiltration curve numbers.

1. Set up the Global Infiltration first.
   Click Global Infiltration.

.. image:: ../../img/Infiltration-Condition-Editor/infilt011.png

2. Fill the Global Infiltration dialog box.

.. image:: ../../img/Infiltration-Condition-Editor/infilt012.png

SCS Calculator Single Shapefile

1. Click the Calculate SCS CN button.

.. image:: ../../img/Infiltration-Condition-Editor/infilt013.png

2. Select the layer and field with the infiltration data and click OK to run the calculator.

.. image:: ../../img/Infiltration-Condition-Editor/infilt014.png

3. When the calculation is complete, the following box will appear.
   Click OK to close the box.

.. image:: ../../img/Infiltration-Condition-Editor/infilt015.png

SCS Calculator Single Shapefile Multiple Fields

Use this option to calculate SCS curve number data from a single layer with multiple fields.
This is a vector layer with polygon features and field to define the soil group, vegetation coverage and impervious space.
This option was developed specifically for Pima County.

1. Click the Calculate SCS CN button.

.. image:: ../../img/Infiltration-Condition-Editor/infilt013.png

2. Select the layer and fields with the infiltration data and click OK to run the calculator.

.. image:: ../../img/Infiltration-Condition-Editor/infilt016.png

3. When the calculation is complete, the following box will appear.
   Click OK to close the box.

.. image:: ../../img/Infiltration-Condition-Editor/infilt015.png

Horton
------

.. _global-2:

Global
~~~~~~

The SCS infiltration editor can add global or spatially variable infiltration data to the INFIL.DAT file for infiltration curve numbers.

1. Set up the Global Infiltration first.
   Click Global Infiltration.

.. image:: ../../img/Infiltration-Condition-Editor/infilt011.png

2. Fill the Global Infiltration dialog box.

.. image:: ../../img/Infiltration-Condition-Editor/infilt017.png

Horton Spatially Variable Method
--------------------------------

Spatially variable Horton infiltration is created by digitizing infiltration polygons.
Use the polygon editor to digitize spatially variable infiltration.
Create a polygon to represent an area of infiltration.

3. |infilt019|\ Click the create a polygon tool and digitize a polygon.

4. Click *Save*.

5. |infilt020|\ Right Click the Infiltration Areas layer (User Layers) and
   open the Attributes Table. Click the Editor Pencil button.

6. Name the infiltration polygons and fill out the data for fhorti, fhori, and deca.

7. Click the Save button and Editor Pencil button.

.. image:: ../../img/Infiltration-Condition-Editor/infilt018.png

8. Click Schematize.

Troubleshooting
~~~~~~~~~~~~~~~

1. |infilt021|\ Infiltration calculators all use intersection tools. This
   can cause problems if the shapefiles are not set up correctly.
   Specifically, land use and soils shapefiles that may have been
   converted from raster data. If errors persist, use “fix geometry”,
   “simplify”, and “dissolve” on the source shapefiles. These tools are
   part of the QGIS Processing Toolbox. They can also be corrected in
   ArcGIS if the datasets are very large.

2. Make sure the shapefiles completely cover the grid.
   If a grid element is outside the coverage of the infiltration, QGIS will show an error.

3. Make sure the shapefile fields have a correctly defined number type.
   The shapefiles that are supplied with the QGIS Lessons will help define the Field Variable Format such as string, whole number or decimal number.

.. |infilt019| image:: ../../img/Infiltration-Condition-Editor/infilt019.png
.. |infilt020| image:: ../../img/Infiltration-Condition-Editor/infilt020.png
.. |infilt021| image:: ../../img/Infiltration-Condition-Editor/infilt021.png
.. |infilt019| image:: ../../img/Infiltration-Condition-Editor/infilt019.png
.. |infilt020| image:: ../../img/Infiltration-Condition-Editor/infilt020.png
.. |infilt021| image:: ../../img/Infiltration-Condition-Editor/infilt021.png
