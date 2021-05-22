Storm Drain Editor
==================

The Storm Drain Editor tool has several functions to prepare the data that integrates the FLO-2D surface water model with the storm drain model.
This document will explain the functionality of each button.
For a step-by-step tutorial, use the QGIS Workshop Lessons or the Self-Help training package.

.. image:: ../../img/Storm-Drain/Storm002.png


1. The digitize storm drain buttons are inactive.
   It is recommended to create a storm drain network in separate storm drain shapefiles as discussed below.

2. the blue schematize button is used when the storm drain system is complete and ready to convert to the FLO-2D schema layers.

3. The simulate storm drain check box will turn on the storm drain switch in the Control Variables.

.. image:: ../../img/Storm-Drain/Storm003.png


Storm Drain Network
-------------------

The select component from shapefile feature is used to build a storm drain network from a set of shapefiles.
Some projects have a storm drain system already developed.
Some projects have no network and start from scratch.
Either way, this information will serve as a template for the data needed to create a storm drain system.

1. Load the shapefiles onto the map or digitize new shapefiles with QGIS.

.. image:: ../../img/Storm-Drain/Storm004.png


The shapefiles can be described as follow:

-  **Lesson3Outfalls.shp** is a point shapefile that contains the outfalls.

-  **Lesson3Conduits.shp** is a line shapefile that contains the conduits system.

-  **Lesson3InletsJunctions.shp** is a point shapefile that contains the Inlets, pumps, and Junctions.

The following data must be available in the shapefile to create the **SWMM.INP** files and the associated storm drain data files: **SWMMFLO.DAT**,
**SWMMOUTF.DAT** and **SWMMFLORT.DAT**.

.. _`conduits`:

conduits:

Name

String

Upstream Node Name

String\* this can be dummy data.
It is auto assigned by the plugin.

Downstream Node Name

String\* this can be dummy data.
It is auto assigned by the plugin.

Inlet Offset (optional)

Real precision 3

Outlet Offset (optional)


Shape

String

Number of Barrels

Integer

Max Depth (Diameter for circular)  (ft or m)

Real precision 3

Geom 2 (Width for rectangle) (ft or m)

Real precision 3

Geom 3 (ft or m)

Real precision 3

Geom 4 (ft or m)

Real precision 3

Length (ft or m)

Real precision 3

conduit roughness n

Real precision 4

Initial Flow (optional) (cfs or cms)

Real precision 3

Maximum Flow (optional)  (cfs or cms)

Real precision 3

Entry Loss Coef (optional)

Real precision 3

Exit Loss Coef (optional)

Real precision 3

Average Loss Coef (optional)

Real precision 3

Flap Gate

Integer


.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - **INLETS/JUNCTIONS**
     - Name
     - String

   * -
     - Type
     - Integer

   * -
     - Invert Elevation (ft or m)
     - Real precision 3

   * -
     - Maximum Depth (ft or m)
     - Real precision 3

   * -
     - Initial Depth (optional) (ft or m)
     - Real precision 3

   * -
     - Surcharge Depth (optional) (ft or m)
     - Real precision 3

   * -
     - Length/Perimeter (ft or m)
     - Real precision 3

   * -
     - Width/Area (ft or m or ft\ :sup:`2` or m\ :sup:`2`)
     - Real precision 3

   * -
     - Height/Sag/Surcharge Depth (ft or m)
     - Real precision 3

   * -
     - Weir Coefficient
     - Real precision 3

   * -
     - Feature (optional)
     - Integer

   * -
     - Curb Height (optional)
     - Real precision 3

   * -
     - Clogging Factor (optional)
     - Real precision 3

   * -
     - Time for Clogging (optional)
     - Real precision 3

   * - **OUTFALLS**
     - Name
     - String

   * -
     - Invert Elevation (ft or m)
     - Real precision 3

   * -
     - Flap Gate
     - Integer or String (0/1 or yes/no)

   * -
     - Allow Discharge Switch
     - Integer

   * -
     - Outfall Type
     - Integer

   * -
     - Water Depth (optional) (ft or m)
     - Real precision 3

   * -
     - Tide Curve (optional)
     - String

   * -
     - Time Series (optional)
     - String


Inlets/Junctions Shapefile
--------------------------

This is a sample of the attributes table for the Inlet/Junctions shapefile.

.. image:: ../../img/Storm-Drain/Storm005.png


The fields from the attribute table are selected using the Select Components from Shapefile dialog box.

.. image:: ../../img/Storm-Drain/Storm006.png


.. image:: ../../img/Storm-Drain/Storm007.png

Conduits Shapefiles
-------------------

This is a sample of the attributes table for the conduit shapefile.

.. image:: ../../img/Storm-Drain/Storm008.png


The fields from the attribute table are selected using the Select Components from Shapefile dialog box.

.. image:: ../../img/Storm-Drain/Storm006.png


.. image:: ../../img/Storm-Drain/Storm009.png


Outfall Shapefiles
------------------

This is a sample of the attributes table for the outfall shapefile.

.. image:: ../../img/Storm-Drain/Storm010.png

The fields from the attribute table are selected using the Select Components from Shapefile dialog box.

.. image:: ../../img/Storm-Drain/Storm006.png


.. image:: ../../img/Storm-Drain/Storm011.png


Import SWMM.inp
---------------

An existing SWMM.inp project can be imported in a FLO-2D Surface System.
Click on Import SWMM.inp and browse the project folder that contains the file.

.. image:: ../../img/Storm-Drain/Storm012.png


This button loads inlets/junctions, outfalls and conduits from an \*.INP file.
The Storm Drain data needs to be schematized; the table components that can be opened from the Storm Drain Editor will contain the variables from the
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

.. image:: ../../img/Storm-Drain/Storm013.png


Data save in the Components tables is written to the .INP file using this function.

Components: Inlets/Junctions
----------------------------

Edit components that already exist using the Components editors for Inlets/Junctions, Outfalls and Conduits.

.. image:: ../../img/Storm-Drain/Storm014.png


A dialog is shown with data for the selected component, in this case the Inlets/Junctions were selected, the user can edit the tables.

.. image:: ../../img/Storm-Drain/Storm015.png


Components: Outfalls
--------------------

Edit components that already exist using the Components editors for Inlets/Junctions, Outfalls and Conduits.

.. image:: ../../img/Storm-Drain/Storm016.png


A dialog is shown with data for the selected component, in this case the Outfalls were selected, the user can edit the tables.

.. image:: ../../img/Storm-Drain/Storm017.png


Components: Conduits
--------------------

Edit components that already exist using the Components editors for Inlets/Junctions, Outfalls and Conduits.

.. image:: ../../img/Storm-Drain/Storm018.png


A dialog is shown with data for the selected component, in this case the Outfalls were selected, the user can edit the tables.

.. image:: ../../img/Storm-Drain/Storm019.png


Auto-assign conduit nodes
-------------------------

This tool will automatically fill the node names required for the conduit connections.

.. image:: ../../img/Storm-Drain/Storm020.png


Conduits are connected to the node they touch both upstream and downstream by the name of the node.

.. image:: ../../img/Storm-Drain/Storm021.png


In a storm drain network there is a separate conduit feature between each node.
The auto-assign button finds the node in proximity of the end of each feature and assigns it to the table.
It is important to orient the conduit features so that the first vertex is near the inlet node and the last vertex is near the outlet node.
See the flow direction arrows in the following image.

.. image:: ../../img/Storm-Drain/Storm022.png


Rating Tables
-------------

Rating tables define the flow at a given depth.
They are used for headwalls.
There are two methods for building rating tables.
`Method 1 <#method-1.-create-with-the-flo-2d-plugin>`__ uses the plugin to build the tables.
This method is good if only a few tables are required.
`Method 2 <#method-2.-import-multiple-tables>`__ imports tables from a text file.
This method is better if many tables are required.

Method 1. Create with the FLO-2D plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set up the rating tables with the Plugin by adding a rating table to the table editor and assigning the table to the correct inlet.

.. image:: ../../img/Storm-Drain/Storm023.png


Use the Inlet Editor to assign the table to the Type 4 inlet.

.. image:: ../../img/Storm-Drain/Storm024.png


Method 2. Import multiple tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Click the Import Rating Table… button.

.. image:: ../../img/Storm-Drain/Storm025.png


2. Select all of the rating tables that match the type 4 inlets.

3. The plugin will load the tables based on the node name and automatically assign each table.

.. image:: ../../img/Storm-Drain/Storm026.png


4. Tables are space or tab delimited and are created using culvert equations or HY-8.

.. image:: ../../img/Storm-Drain/Storm027.png


External Inflow Data
--------------------

Set up the external inflow data for a storm drain node.
Use the Inlet/Junction editor to set up external inflow parameters and data.

.. image:: ../../img/Storm-Drain/Storm028.png


Use the Internal Inflow tools to define parameters and select time series data.

Simple parameters are used in this case.

-  Inflow constituent: water only (no pollutants)

-  Basline flow: 0 cfs(cms)

-  Baseline pattern: hourly with no multiplier

-  Scale factor: none

-  Time series file: Example Project/QGIS Lesson 3/SDInflow.dat

.. image:: ../../img/Storm-Drain/Storm029.png

