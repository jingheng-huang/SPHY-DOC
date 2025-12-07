# Introduction of Pre-Processing Tool

## Overview of the Structure

````{admonition} Files
![Alt text](image-1.png)

📁 Tools  
* Scripts that assist with data preparation or post‑processing of model outputs.

📁 global_database  
* Global datasets required for running the model. Can be downloaded from xxx.

📁 src  
* Source code.

📄 environment.yml  
* YAML file for creating the conda environment with all required dependencies.

📄 preprocess_Alahca.cfg  
* Example configuration file defining the model resolution and all required input paths/settings.

````

👉 Run the program using: `./run_preprocess.sh XX.cfg`  
`XX.cfg` is the global configuration file. A detailed description of all settings is provided in the next section.

---

(preprocessing_tool_config_section)=
## Introduction to the Configuration File

`preprocess_Alahca.cfg` is an example configuration file. All parameters required to run this tool are specified here.  
There are **six sections** in total.

---

### 1. General Settings
![Alt text](image-13.png)

* **program_path**: folder where the `src` directory (main script) is located.  
* **out_folder**: directory where the outputs will be saved (not model results; this is the folder where you will run the model).  
* **main_and_subbasin_shps**: path to the basin and sub‑basin shapefiles (if available).  
* **model_res**: spatial resolution of the model grid (unit: meters).  
* **ys and ye**: start and end year of the simulation.  
* **spinupyears**: number of spin‑up years.  
* **forcing_cut**: whether to trim the forcing data in the database to the specified time range.

---

### 2. Forcing Settings
![Alt text](image-14.png)

* **prcp_bands_num**: number of elevation bands (based on elevation quantiles). Set this to 1 if no elevation bands are needed.  
* **pcrp_correction_factors**: precipitation correction factors for each elevation band (unit: %).  
* **tem_bands_num**: number of temperature elevation bands (based on elevation quantiles).  
* **t_deltas**: temperature offsets for each band (°C).  
* **tem_lapserate**: temperature lapse rate used for downscaling the forcing dataset to the fine‑resolution grid (unit: °C/m).  
Typical value: **0.0065 °C/m**.  
The model computes the elevation difference between the forcing DEM and the basin DEM, and then applies the lapse rate to downscale temperature.

  <span style="color:blue">You may leave `tem_lapserate` empty. The program will automatically compute a lapse rate based on the elevation–temperature relationship in the forcing dataset.</span>

* **gradient_downscale_flag**: enable lapse‑rate downscaling (1 = on, 0 = off).  
* **p_gradients**: precipitation gradient for downscaling (unit: %/m).

---

### 3. Glacier Settings
![Alt text](image-15.png)

* **choose_rgi_id_zone_file**: a CSV file where the first row contains the region codes (RGI V7) and the second row contains the glacier IDs.  
Example:  
![Alt text](image-6.png)  
🔔 You can generate this file using the script in the **Tools** folder.

* **glacier_resolution**: resolution for glacier modeling, depending on the input DEM for glaciers (specified in the Database section).  
* **glacier_tem_lapse**: temperature lapse rate for downscaling the coarse forcing dataset to the fine glacier grid (typical: −0.0065 °C/m).

---

### 4. Statistics Settings
![Alt text](image-16.png)

* **scf_statistic_flag**: enable snow‑cover statistics (1 = on, 0 = off).  
* **snow_threshold_min**: minimum snow depth threshold (e.g., mm) to classify a pixel as snow‑covered.  
* **statistic_bands_number**: number of elevation bands used for snow statistics.  
* **wintermonth**: months considered as winter for winter‑discharge outputs.

---

### 5. Calibration Settings
![Alt text](image-10.png)

* **pest_flag**: enable automatic model calibration using PEST (1 = on, 0 = off).  
If set to 1, all parameters in this section must be provided.  

* **observation_file**: Excel `.xlsx` file containing all observation data used for calibration. Example structure:  
![Alt text](image-11.png)  
`TR` = total runoff, `WR` = winter runoff.  
Values 1 to N correspond to basins/sub‑basins in the same order as specified in `main_and_subbasin_shps`.  
`scf` = snow‑cover fraction.  
<span style="color:#d00000;">❗ For SCF, indices 1 to N refer to elevation bands, **not** sub‑basins.</span>  
`gmb_mean` = annual glacier mass balance for the entire basin.

* **observation_sheetname_date**: sheet name and time range (YYYY‑MM‑DD) used for each dataset.  
* **simufiles_to_compare**: simulation output files to compare with observations.  
❗ Output filenames are fixed — do **not** rename them.

Supported calibration files:

1. **Total runoff** — `'QAllDTS.csv': 'value1'`  
   Values 1 to N correspond to basins/sub‑basins.

2. **Winter discharge** — `'WRDTS.csv': 'value1'`  
   Used to give extra weight to winter low‑flow.  
   You may also use `'WBDTS.csv'` when winter discharge represents most baseflow.

3. **Glacier mass balance** — `'simu_GMB.csv': 'value'`  
   Only one value is produced for glacier mass balance (not split by sub‑basins).

4. **Snow‑cover fraction** — `'SCF_TSS_Monthly.csv': '1'`  
   <span style="color:#d00000;">❗ 1 to N correspond to elevation bands (low → high), not basins.</span>

Additional settings:

* **calculate_components_period**: start and end year for calculating runoff components.  
* **hostnam**: hostname or IPv4 of the compute node (`hostname` or `hostname -I`).  
* **partion**: partition name (check using `sinfo`).  
* **agents_num**: number of agents/simultaneous jobs (suggested: 2 × number of parameters + 1).  
* **commment**: description of this auto‑calibration run; will be saved in `pest_run_report.csv`.

`pest_run_report.csv` stores all parameter combinations tested by PEST, plus basic statistics (e.g., NSE and component contributions).

---

### 6. Database Settings
![Alt text](image-12.png)

This section defines the sources of all datasets.  
You may use your own datasets as long as the data formats are consistent.

````{Note}
* It is recommended to provide **absolute paths** rather than relative paths.  
* For different model resolutions, use HydroDEM files with similar resolutions.  
  HydroDEM is a hydrologically conditioned DEM (pit‑filled, corrected), suitable for watershed boundary extraction.  
  <span style="color:red;">If the extracted watershed boundary differs significantly from reality, adjust the data source in this section.  
  In the worst case, you may manually edit the DEM elevations.</span>
````
