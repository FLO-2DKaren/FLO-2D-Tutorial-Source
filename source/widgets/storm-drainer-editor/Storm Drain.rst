Storm Drain Editor
==================

The Storm Drain Editor tool has several functions to prepare the data that integrates the FLO-2D surface water model with the storm drain model:

-  Reads/writes data from the SWMM.inp file, and associates inlets/junctions, outfalls, and conduits with FLO-2D cells.

-  Creates and edit the SWMM.INP file by importing inlets/junctions, outfalls, and conduits from shapefiles.

-  Saves and edits the FLO-2D SWMMFLO.DAT, SWMMRT.DAT and SWMMOUTF.DAT files containing the inlet and outlet data.

-  Displays the inlets and outlets and the piping network connections.

The storm drain editor widget has the following functionality:

.. image:: image\stormd002.png

Create storm drain components from shapefiles
---------------------------------------------

The select component from shapefile feature is used to build a storm drain network from a set of shapefiles.

.. image:: image\stormd003.png

The following information summarized the data that is needed in the Shapefiles for the creation of the \*.INP.
The collection of As-Built always help when assumptions are needed in the creation of the \*.INP file.

Inlets/Junctions Shapefiles
---------------------------

The following data is needed for inlets/junctions.
Data identified as optional is not required.

1.  Name

2.  Location (X- and Y- Coordinates)

3.  Invert Elevation

4.  Rim Elevation or Maximum Depth

5.  Initial Depth (Optional)

6.  Surcharge Depth (Optional for inlets, Non-optional for Manholes)

7.  External Inflows receive at inlet/junction (Optional).
   Typically, inflow coming from out of the domain can be imposed as an inflow condition to the Inlets/Junctions next to the boundary.

8.  Inlet Geometry for Inlets type 1,2,3, 4 and 5.
   For Inlet type 4, geometry is needed for the creation of the rating table.

9.  Length (1 or 2) / Perimeter (3 or 5)

10.
Width (2)/ Area (3 or 5)

11.
Height (1 or 2) / Sag (3) / Surcharge (5)

12.
Vertical Opening (1) / Horizontal Opening (0).

13.
Curb Height (Optional)

Click the button to open a dialog box that calls shapefiles attributes and assign them to the storm drain features.

.. image:: image\stormd004.png

Conduits Shapefiles

The following data is needed for conduits.
Data identified as optional is not required.

1.  Name

2.  Inlet and Outlet Node: upstream and downstream inlets/junctions connected to the pipe.

3.  Shape, example: Circular.

4.  Max Depth of Cross Section, example: diameter for circular shape.
   Other conduits shapes will require additional geometry data, see Storm Drain Manual for detailed information.

5.  Number of Barrels.

6.  Pipe Length.

7.  Manning’s Roughness Coefficient: typical values can be assigned based on the pipe material and conditions.

8.  Inlet/Outlet Offset (optional)

9.  Entry Loss Coefficient (optional)

10.
Exit Loss Coefficient (optional)

11.
Average Loss Coefficient (optional)

12.
Flap Gate (optional)

13.
Initial Flow (optional)

14.
Maximum Flow (optional)

Click the button to open a dialog box that calls shapefiles attributes and assign them to the storm drain features.

.. image:: image\stormd005.png

Outfall Shapefiles
------------------

The following data is needed for the outfalls.
Data identified as optional is not required.

1. Name

2. Location (X and Y Coordinates)

3. Invert Elevation

4. Type: FREE to be connected to the surface model.
   Normal, Fixed, Tidal or Timeseries can also be modeled but they will not be connected to the surface flow model.

5. Flap gate (optional)

6. Click the button to open a dialog box that calls shapefiles attributes and assign them to the storm drain features.

.. image:: image\stormd006.png

Import SWMM.inp
---------------

An existing SWMM.inp project can be imported in a FLO-2D Surface System.
Click on Import SWMM.inp and browse the project folder that contains the file.

.. image:: image\stormd007.png

This button loads inlets/junctions, outfalls and conduits from an \*.INP file.
The Storm Drain data needs to be schematized, the table components that can be opened from the Storm Drain Editor will contain the variables from the
SWMM.inp file.
Additional data is needed for the SWMMFLO.DAT, SWMMOUTF.DAT and SWMMFLORT.DAT files.

QGIS FLO-2D layers will be filled up with the data from the following \*.INP groups:

-  Inlets/Junctions

-  Outfalls

-  Conduits

-  Cross sections

-  Losses

-  Coordinates (required coordinates only)

Export SWMM.inp
---------------

Export SWMM.inp file in a FLO-2D format prior to running.
The SWMM.INP can be created from shapefiles and then exported or it might be modified from an existing SWMM.INP.

.. image:: image\stormd008.png

Data save in the Components tables is written to the .INP file using this function.

Components: Inlets/Junctions
----------------------------

Edit components that already exist using the Components editors for Inlets/Junctions, Outfalls and Conduits.

.. image:: image\stormd009.png

A dialog is shown with data for the selected component, in this case the Inlets/Junctions were selected, the user can edit the tables.

.. image:: image\stormd010.png

Components: Outfalls
--------------------

Edit components that already exist using the Components editors for Inlets/Junctions, Outfalls and Conduits.

.. image:: image\stormd011.png

A dialog is shown with data for the selected component, in this case the Outfalls were selected, the user can edit the tables.

.. image:: image\stormd012.png

Components: Conduits
--------------------

Edit components that already exist using the Components editors for Inlets/Junctions, Outfalls and Conduits.

.. image:: image\stormd013.png

A dialog is shown with data for the selected component, in this case the Outfalls were selected, the user can edit the tables.

.. image:: image\stormd014.png

Rating Tables
-------------

Set up the rating tables by adding a rating table to the table editor and assigning the table to the correct inlet.

.. image:: image\stormd015.png

Use the Inlet Editor to assign the table to the Type 4 inlet.

.. image:: image\stormd016.png

External Inflow Data
--------------------

Set up the external inflow data for a storm drain node.
Use the Inlet/Junction editor to set up external inflow parameters and data.

.. image:: image\stormd017.png

Use the Internal Inflow tools to define parameters and select time series data.

Simple parameters are used in this case.

-  Inflow constituent: Flow only (no pollutants)

-  Basline flow: 0 cfs(cms)

-  Baseline pattern: hourly with no multiplier

-  Scale factor: none

-  Time series file: Example Project/QGIS Lesson 3/SDInflow.dat

.. image:: image\stormd018.png
