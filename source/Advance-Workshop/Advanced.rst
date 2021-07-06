**FLO-2D\ ©**

**PRO VERSION**

**Two-Dimensional**

**Flood Routing Model**

**Workshop Lessons FLO-2D Plugin for QGIS 2021**

Table of Contents
=================

`Table of Contents i <#table-of-contents>`__

`Module 1, Project Recovery and Debug 5 <#module-1-project-recovery-and-debug>`__

`Required Data 5 <#required-data>`__

`Step 1: Create a recovery file 6 <#step-1-create-a-recovery-file>`__

`Step 2: Recover a project 6 <#step-2-recover-a-project>`__

`Step 3: Open the project 8 <#step-3-open-the-project>`__

`Step 4: Export the FLO-2D data 10 <#step-4-export-the-flo-2d-data>`__

`Step 5: Run the debug engine 14 <#step-5-run-the-debug-engine>`__

`Step 6: Debug the project in QGIS 15 <#step-6-debug-the-project-in-qgis>`__

`Step 7: Load the conflict table 17 <#step-7-load-the-conflict-table>`__

`Step 8: Load the levee table 18 <#step-8-load-the-levee-table>`__

`Module 2 Part I – Hydraulic Structures 20 <#module-2-part-i-hydraulic-structures>`__

`Required Data 20 <#required-data-1>`__

`Step 1: Setup the project 21 <#step-1-setup-the-project>`__

`Step 2: Import data 22 <#step-2-import-data>`__

`Step 3: Format the data layers 23 <#step-3-format-the-data-layers>`__

`Step 4: Build the structures into the User Layers.
26 <#step-4-build-the-structures-into-the-user-layers.>`__

`Step 5: Assign the structure attributes 27 <#step-5-assign-the-structure-attributes>`__

`Step 6: Assign the rating tables 28 <#step-6-assign-the-rating-tables>`__

`Step 7: Schematize the data 30 <#step-7-schematize-the-data>`__

`Step 8: Save, export, and run 31 <#step-8-save-export-and-run>`__

`Module 2 Part II – Advanced Hydraulic Structures 33 <#module-2-part-ii-advanced-hydraulic-structures>`__

`Required Data 33 <#required-data-2>`__

`Step 1: Setup the project 34 <#step-1-setup-the-project-1>`__

`Step 2: Simplify the map 35 <#step-2-simplify-the-map>`__

`Step 3: Build a new structure 36 <#step-3-build-a-new-structure>`__

`Step 4: Measure the culvert length 38 <#step-4-measure-the-culvert-length>`__

`Step 5: Complete the structure data and schematize.
39 <#step-5-complete-the-structure-data-and-schematize.>`__

`Step 6: Correct invert elevation 40 <#step-6-correct-invert-elevation>`__

`Step 7: Save, export, and run.
43 <#step-7-save-export-and-run.>`__

`Module 2 Part III – Bridge Hydraulic Structure 48 <#module-2-part-iii-bridge-hydraulic-structure>`__

`Required Data 48 <#required-data-3>`__

`Step 1: Load the project 49 <#step-1-load-the-project>`__

`Step 2: Define the bridge variables and coefficients 50 <#step-2-define-the-bridge-variables-and-coefficients>`__

`Plan view parameters 50 <#plan-view-parameters>`__

`Profile parameters 51 <#profile-parameters>`__

`Bridge opening ratio 52 <#bridge-opening-ratio>`__

`Bridge tables 53 <#bridge-tables>`__

`Bridge variables dialog 55 <#bridge-variables-dialog>`__

`Step 3: Build the cross section data 57 <#step-3-build-the-cross-section-data>`__

`Step 4: Save, export and run.
59 <#step-4-save-export-and-run.>`__

`Module 3 – Prescribed Dam Breach 61 <#module-3-prescribed-dam-breach>`__

`Required Data 61 <#required-data-4>`__

`Step 1: Load the project 62 <#step-1-load-the-project-1>`__

`Step 2.
Load the aerial and hydrography 63 <#step-2.-load-the-aerial-and-hydrography>`__

`Step 3.
Review hydrology 65 <#step-3.-review-hydrology>`__

`Step 4.
Set up the reservoir 68 <#step-4.-set-up-the-reservoir>`__

`Step 5.
Create the levee 69 <#step-5.-create-the-levee>`__

`Step 6.
Define the breach 71 <#step-6.-define-the-breach>`__

`Step 7.
Remove the dam elevation (method 1) 74 <#step-7.-remove-the-dam-elevation-method-1>`__

`Step 8.
Remove the dam elevation thin slice (method 2) 75 <#step-8.-remove-the-dam-elevation-thin-slice-method-2>`__

`Step 9.
Export and run the model 77 <#step-9.-export-and-run-the-model>`__

`Step 10.
Add a culvert 81 <#step-10.-add-a-culvert>`__

`Step 11.
Downstream Boundary 85 <#step-11.-downstream-boundary>`__

`Step 12.
Common mistakes demo 87 <#step-12.-common-mistakes-demo>`__

`Bad reservoir or leaky levee component 87 <#bad-reservoir-or-leaky-levee-component>`__

`Dam elevation not removed 88 <#dam-elevation-not-removed>`__

`Module 5 Part I – Create a Watershed Model 90 <#module-5-part-i-create-a-watershed-model>`__

`Required Data 90 <#required-data-5>`__

`Step 1: Load the project 91 <#step-1-load-the-project-2>`__

`Step 2.
Load the hydrography map 92 <#step-2.-load-the-hydrography-map>`__

`Step 3.
Review the watershed.
94 <#step-3.-review-the-watershed.>`__

`Step 4.
Create the grid.
95 <#step-4.-create-the-grid.>`__

`Step 5.
Interpolate Elevation.
96 <#step-5.-interpolate-elevation.>`__

`Step 6.
Calculate Roughness 97 <#step-6.-calculate-roughness>`__

`Step 7.
Save and create a recovery point.
97 <#step-7.-save-and-create-a-recovery-point.>`__

`Step 8.
Determine the total rainfall 98 <#step-8.-determine-the-total-rainfall>`__

`Step 9.
Sample the rainfall raster 103 <#step-9.-sample-the-rainfall-raster>`__

`Step 10.
Set up the rainfall 104 <#step-10.-set-up-the-rainfall>`__

`Step 11.
Calculate infiltration 106 <#step-11.-calculate-infiltration>`__

`Step 12.
Alternate infiltration method 2 108 <#step-12.-alternate-infiltration-method-2>`__

`Step 13.
Export infiltration data.
110 <#step-13.-export-infiltration-data.>`__

`Step 14.
Recalculate the elevation.
112 <#step-14.-recalculate-the-elevation.>`__

`Step 15.
Export INFIL.DAT 112 <#step-15.-export-infil.dat>`__

`Step 16.
Format the CN data 114 <#step-16.-format-the-cn-data>`__

`Step 17.
Reload the infiltration data.
114 <#step-17.-reload-the-infiltration-data.>`__

`Step 18.
Save, export, and run 117 <#step-18.-save-export-and-run>`__

`Step 19.
Map the velocity vectors and import them into QGIS 118 <#step-19.-map-the-velocity-vectors-and-import-them-into-qgis>`__

`Step 20.
Create a floodplain cross section.
122 <#step-20.-create-a-floodplain-cross-section.>`__

`Step 21.
Save, export, and run again 123 <#step-21.-save-export-and-run-again>`__

`Module 5 Part II – Watershed Mudflow Model 125 <#module-5-part-ii-watershed-mudflow-model>`__

`Required Data 125 <#required-data-6>`__

`Step 1: Load the project 126 <#step-1-load-the-project-3>`__

`Step 2.
Create inflow hydrograph 128 <#step-2.-create-inflow-hydrograph>`__

`Step 3.
Assign the hydrograph to a BC node.
130 <#step-3.-assign-the-hydrograph-to-a-bc-node.>`__

`Step 4.
Set a global bulking factor.
131 <#step-4.-set-a-global-bulking-factor.>`__

`Step 5.
Export and run the model 132 <#step-5.-export-and-run-the-model>`__

`Step 6.
Set up the mudflow.
133 <#step-6.-set-up-the-mudflow.>`__

`Step 5.
Export and run the Mudflow model 136 <#step-5.-export-and-run-the-mudflow-model>`__

`Module 6 – Erosion Dam Breach 139 <#module-6-erosion-dam-breach>`__

`Required Data 139 <#required-data-7>`__

`Step 1: Load the project 140 <#step-1-load-the-project-4>`__

`Step 2: Initial conditions reservoir 141 <#step-2-initial-conditions-reservoir>`__

`Step 3: Review dam geometry 143 <#step-3-review-dam-geometry>`__

`Step 4.
Review dam material 144 <#step-4.-review-dam-material>`__

`Step 5.
Review general breach parameters 145 <#step-5.-review-general-breach-parameters>`__

`Step 6.
Create the breach point 145 <#step-6.-create-the-breach-point>`__

`Step 7.
Export and run the model 149 <#step-7.-export-and-run-the-model>`__

`Step 8.
Review the data 151 <#step-8.-review-the-data>`__

`Module 7 – Tailings Dam Tool 152 <#module-7-tailings-dam-tool>`__

`Required Data 152 <#required-data-8>`__

`Step 1: Load the project 153 <#step-1-load-the-project-5>`__

`Step 2.
Find inflow node 154 <#step-2.-find-inflow-node>`__

`Step 3.
Run the Tailings Dam Tool 154 <#step-3.-run-the-tailings-dam-tool>`__

`Step 4.
Dam geometry 155 <#step-4.-dam-geometry>`__

`Step 5.
Volume 156 <#step-5.-volume>`__

`Step 6.
Geotech data 157 <#step-6.-geotech-data>`__

`Step 7.
Foundation geotechnical data from TUV report 157 <#step-7.-foundation-geotechnical-data-from-tuv-report>`__

`Step 8.
Saturated tailings depth 158 <#step-8.-saturated-tailings-depth>`__

`Step 9.
Tailings dam tool 159 <#step-9.-tailings-dam-tool>`__

`Step 7.
Export and run the model 163 <#step-7.-export-and-run-the-model-1>`__

`Module 8 – Storm Drain Shapefile Development 166 <#module-8-storm-drain-shapefile-development>`__

`Required Data 166 <#required-data-9>`__

`Step 1: Load the project 167 <#step-1-load-the-project-6>`__

`Step 2: Import shapefiles for storm drain features 168 <#step-2-import-shapefiles-for-storm-drain-features>`__

`Step 3.
Add missing columns to shapefiles 172 <#step-3.-add-missing-columns-to-shapefiles>`__

`Module 9 – Storm Drain Schematize 173 <#module-9-storm-drain-schematize>`__

`Required Data 173 <#required-data-10>`__

`Step 1: Select components from shapefile layer 174 <#step-1-select-components-from-shapefile-layer>`__

`Step 2: Calculate the conduit node connections 177 <#step-2-calculate-the-conduit-node-connections>`__

`Step 3: Import Rating Tables 178 <#step-3-import-rating-tables>`__

`Step 4: Schematize storm drain components 179 <#step-4-schematize-storm-drain-components>`__

`Step 5: Export SWMM.INP file 180 <#step-5-export-swmm.inp-file>`__

`Step 6: Export the project 182 <#step-6-export-the-project>`__

`Step 7: Run the simulation 184 <#step-7-run-the-simulation>`__





