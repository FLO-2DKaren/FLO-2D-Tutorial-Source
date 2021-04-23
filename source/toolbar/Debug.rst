
Data Warnings and Errors – DEBUG Tool
=====================================

The Data Warnings and Error button opens a system that helps the user
debug data files and search for data conflicts.

.. image:: ../img/debug1.png


1. Perform a debug run

2. `Export the \*.DAT Files <#_Export_FLO-2D_*.DAT_1>`__.

3. Click the Run FLO-2D button.

.. image:: ../img/debug2.png


4. This will automatically trigger the FLO-2D check system performed by
   the engine FLOPRO.EXE.

.. image:: ../img/debug3.png


.. image:: ../img/debug4.png


5. The model will execute, perform the data checks and then
   automatically shut down. Every time the debug is executed, a new
   debug file with a timestamp is saved to the project folder.

.. image:: ../img/debug5.png


6. Click the Error and Warning button to open the import dialog box.

.. image:: ../img/debug1.png

.. image:: ../img/debug6.png

Debug
-----

7. To import the Debug files, click the Import DEBUG File button. The
   DEBUG file will have a date and timestamp to track progress.

.. image:: ../img/debug7.png
   :alt: C:\Users\ALEJAN~1\AppData\Local\Temp\SNAGHTML5e3fa1e4.PNG


8. The import process will include several files that can be used to
   help users review surface features such as rim elevations, depressed
   elements and channel – floodplain interface. Click Yes to load the
   Errors and Warning Dialog box and import the review files.

.. image:: ../img/debug8.png

Conflicts
---------

The Current Project option will create a list of data conflicts. These
conflicts are not necessarily errors, they are generated based on the
conflict matrix. The conflict matrix is located Here:
c:\users\public\documents\FLO-2D Pro Documentation\Handouts\Conflict
Matrix.pdf

Levee Crests
------------

The final option is Levee Crest validation tool. It is used to review
the levees and grid element elevations.

Dialog Boxes
------------

The Errors and Warnings Dialog box shows all Errors, Conflicts, and
Warnings created by the file checking program. All of these boxes can be
used to sort and view and pan to cells with potential issues.

.. image:: ../img/debug9.png


.. image:: ../img/debug10.png


.. image:: ../img/debug11.png


Debug Layers
------------

The layers show points where there are differences between channel bank
and floodplain bank elevations, rim and floodplain inlet elevations, and
depressed elements and levee crest elevations. In this example, the
layers are grouped using a QGIS standard layer grouping procedure.

.. image:: ../img/debug12.png

Each layer has an attribute table that can be sorted and used to find
grid elements that may need elevation edits.

.. image:: ../img/debug13.png
