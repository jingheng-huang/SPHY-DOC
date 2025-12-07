# Run the Pre_Processing Tool

In this section, there will be an example to show how to use the pre-processing tool to set up the model,
and how to run the model manually or automatically.

The case basin is Gunt, which is located in the Pamir. 
![Alt text](image-17.png)

![Alt text](image-18.png)  
The detail basin information can be found in https://esurf.copernicus.org/articles/3/333/2015/

## Download the script
* Crrate a folder on your local PC, Here I create a folder called 'example' on F drive.Download the scripts from Github
(https://github.com/jingheng-huang/SphySetup)

![Alt text](image-25.png)
The description of the structure has been described in {doc}`Introduce_the_preprocessing_tool`.

## Prepare the basic inputs


Create a floder called "basinshp" and "observations". No matter where you put it. Here I put them under 'Example'


![Alt text](image-26.png) 

---
* In the basinshp folder, you need to put to a basin shpfile (**projection WGS84**) inside, this will be served as a standard basinshp for clipping the dem and etc. Make sure you have the correct the correct boundary. This website can help you check (`https://mghydro.com/watersheds/`)  
![Alt text](image-23.png)
---
* In the observations, you should have an excel observations.xlsx (whatever name you like), which saved all the observations you would like to use for autocalibration. Note if you don't need the auto-calibration, then this file is not necessary. I usually put all the observations under the `observation` folder, then merge them into a single excel xlsx file. The format has been described inin {doc}`Introduce_the_preprocessing_tool`.

![Alt text](image-24.png)
````{note} 
**Optional**: If you wish to calculate the regional mean glacier mass balance with specific glaciers, then you must prepare a csv file which store the glacier ID in RGIV7. The format has been described in chapter2. You can also skip the preparation for this file, the programme will output the regional mean glacier mass balance using all the glaciers inside the basin.
````

<span style="color:blue">Note the folder name is flexible, the key point is to prepare a basin boundary shapefile and (if auto-calibration is needed) the observations.xls file, no matter where you put them. </span>

## Set up the configuration file
Prepare the configuration file, follow the instruction in {ref}`Introduction of the Configuration file Section <preprocessing_tool_config_section>`.

![Alt text](image-28.png)

## Run the Tool
Once the configuration file is ready, go to the SphySetup-main directory and run:

`./run_preprocess.sh preprocess_Alahca.cfg`

````{note}  Make sure that run_preprocess.sh is located in the same directory as src. The configuration file preprocess_Alahca.cfg can be saved anywhere.  

![Alt text](image-29.png)

````
During the first run, the script will take some time to clip the river shapefiles in order to speed up the subsequent processing.
After this step is completed, a folder named `input` will be created inside the output directory specified in the `configuration` file.
Open this folder and use QGIS or any other GIS software to open the file sub_basins.map, and check whether the generated watershed boundaries match the actual ones.

![Alt text](image-31.png)

````{important}

<span style="color:blue">Note that this step is very important. If the generated boundaries differ noticeably from the actual watershed boundaries, consider the following: <span/>

* Check whether the DEM resolution matches the model resolution.  
For example, if the model resolution is set to 1000 m, then the HydroDEM resolution should also be roughly around 1000 m.

* Check whether the river network is correct.  
The river network shpfile is located in the cachefolder inside the `SphySetup-main/src/` directory.
If the river network appears to extend beyond the watershed boundary or shows incorrect connections with rivers in another basin, consider manually correcting the river network or using a different river network data source.

* Consider using a different HydroDEM data source or manually editing the DEM.  
QGIS provides plugins that allow you to freely modify raster values.  
**Note:** Only modify the HydroDEM, which is specifically used for watershed extraction, not the actual DEM file.
````

If you confirm that the watershed boundary matches the actual boundary, you may press y (yes) to proceed to the next few steps.
![Alt text](image-33.png)  
![Alt text](image-34.png)  
![Alt text](image-35.png)   
![Alt text](image-36.png)   

Once the run finishes, a single package of files required to run the model will be created in the output directory specified in the configuration file. The method for running the model is described in the {doc}`Run_model` chapter.

![Alt text](image-37.png)   

````{hint}

The newest version of 'pestpp-glm' or 'pestpp-ies' can be downloaded from https://github.com/usgs/pestpp

If you encounter issues running tsproc.exe, you may need to compile it yourself. For reference, see: https://github.com/smwesten-usgs/tsproc

````