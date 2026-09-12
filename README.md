# Territorial Inequality
This project develops a reproducible workflow for constructing spatial measures of state presence across subnational territories in Africa. The project uses geospatial data on physical and economic infrastructure from the US Geological Survey compilation of Mineral Industries and Related Infrastructure [@GISdata]. These measures are calculated at the electoral constituency level using shapefiles. The resulting measures capture variation in state presence both within and across countries and their territories.

--- 

# Start Here

1. Create the project environment.

   ```bash
   make init
   ```

2. Unzip the GIS infrastructure and shapefile data. Make sure you are in the project working directory.

   ```bash
   unzip -q Africa_GIS.gdb.zip -d Africa_GIS
   unzip -q Shapefiles.zip -d Shapefiles
   ```

---

# Basic workflow

The workflow consists of the following steps:

1. Load infrastructure data. To see all available layers in the GIS data, use:
```python
layers = fiona.listlayers(gdb_dat)
print("Available layers:", layers)
```
To select a specific layer, use:
```python
roads = gpd.read_file(gdb_dat, layer="AFR_Infra_Transport_Road")
```

2. Use functions to calculate a specific infrastructure measure for a single country. For example, `def road_density` takes as input a country name string and returns constituency-level measures of road density (km) per constituency area (km^2). The function does the following: 
- Standardize coordinate reference systems (CRSs) between GIS layer and country shapefile.
- Perform spatial joins between infrastructure and constituency boundaries.
- Calculate constituency-level measures of infrastructure density.
- Merge the measures with the corresponding constituency shapefile.
- Return the final constituency-level dataset.

Open [Milestone1.ipynb](Milestone1.ipynb) for a guided notebook walkthrough.

As the user works along, tests can be run to confirm the code is working as expected. Use the following to confirm whether calculations are behaving as expected:

```
make test
```


