import geopandas as gpd

# load GIS data
df_main = "/Users/sophiesunderland/Desktop/CMSE802F26/Africa_GIS/Africa_GIS.gdb"

# load road layer
df = gpd.read_file(df_main, layer="AFR_Infra_Transport_Road")

def road_density(country = " "):
    # create a GeoDataFrame for the roads in the current country
    roads = df[df["Country"] == country]
    # project the roads to a projected coordinate system for area calculations
    roads_proj = roads.to_crs("ESRI:102022")
    
    # load shapefile for current country and project to the same coordinate system
    country_sf = gpd.read_file(f"/Users/sophiesunderland/Desktop/CMSE802F26/Shapefiles/Shapefiles/{country}/{country}_Constituencies.shp")
    country_sf_proj = country_sf.to_crs("ESRI:102022")

    # intersect roads with constituencies 
    intersection = gpd.overlay(
        roads_proj,
        country_sf_proj,
        how="intersection")

    # create road variable length by summing the length of the roads in each constituency
    intersection["road_length"] = intersection.geometry.length
    intersection = intersection.groupby("Cons_name", as_index=False)["road_length"].sum()
    # transform from m into km
    intersection["length_km"] = intersection["road_length"] / 1000
    # select road length and constituency name columns
    intersection_sub = intersection[["road_length", "length_km", "Cons_name"]]

    # calculate constituency areas in km^2
    country_sf_proj["const_area_km2"] = country_sf_proj.geometry.area / 1_000_000

    # left join constituency areas with road lengths to get a combined dataframe
    country_combined = country_sf_proj.merge(intersection_sub, on="Cons_name", how="left")
    # calculate road density
    country_combined["road_density"] = (country_combined["length_km"] / country_combined["const_area_km2"])
    
    return country_combined
    
def transportation_density(country = "", layer = " "):
    # create a GeoDataFrame for either roads/railways 
    transportation = gpd.read_file(df_main, layer = layer)
    # filter for the current country
    transportation = transportation[transportation["Country"] == country]
    # project the roads to a projected coordinate system for area calculations
    trans_proj = transportation.to_crs("ESRI:102022")
    
    # load shapefile for current country and project to the same coordinate system
    country_sf = gpd.read_file(f"/Users/sophiesunderland/Desktop/CMSE802F26/Shapefiles/Shapefiles/{country}/{country}_Constituencies.shp")
    country_sf_proj = country_sf.to_crs("ESRI:102022")

    # intersect roads with constituencies 
    intersection = gpd.overlay(
        trans_proj,
        country_sf_proj,
        how="intersection")

    # create road variable length by summing the length of the roads in each constituency
    intersection["length"] = intersection.geometry.length
    intersection = intersection.groupby("Cons_name", as_index=False)["length"].sum()
    # transform from m into km
    intersection["length_km"] = intersection["length"] / 1000
    # select road length and constituency name columns
    intersection_sub = intersection[["length", "length_km", "Cons_name"]]

    # calculate constituency areas in km^2
    country_sf_proj["const_area_km2"] = country_sf_proj.geometry.area / 1_000_000

    # left join constituency areas with road lengths to get a combined dataframe
    country_combined = country_sf_proj.merge(intersection_sub, on="Cons_name", how="left")
    # calculate road density
    country_combined["density"] = (country_combined["length_km"] / country_combined["const_area_km2"])
    
    return country_combined

df_all = gpd.read_file("/Users/sophiesunderland/Desktop/CMSE802F26/Africa_GIS/Africa_GIS.gdb")

def density_all(layer = " "):
    # Loop over all countries in main dataset 
    for country in df_all["Country"].dropna().unique():
        # create a GeoDataFrame for the selected layer
        df_sub = gpd.read_file(df_main, layer = layer)
        # filter for the current country
        df_sub = df_sub[df_sub["Country"] == country]
        # project the layer to a projected coordinate system for area calculations
        sub_proj = df_sub.to_crs("ESRI:102022")
        
        # load shapefile for current country and project to the same coordinate system
        country_sf = gpd.read_file(f"/Users/sophiesunderland/Desktop/CMSE802F26/Shapefiles/Shapefiles/{country}/{country}_Constituencies.shp")
        country_sf_proj = country_sf.to_crs("ESRI:102022")

        # intersect layer with constituencies 
        intersection = gpd.overlay(
            sub_proj,
            country_sf_proj,
            how="intersection")

        # identify the variable name based on the layer
        var = ""
        if layer == "AFR_Infra_Transport_Road":
            var = "road"
        elif layer == "AFR_Infra_Transport_Rail":
            var = "rail"
        elif layer == "AFR_Infra_Power_Transmission":
            var = "power"
        
        # create length variable by summing the length of the selected layer/variable in each constituency
        intersection[var] = intersection.geometry.length.groupby(intersection["Cons_name"]).transform("sum")
        # transform from m into km
        intersection[var + "_km"] = intersection[var] / 1000
        # select road length and constituency name columns
        intersection_sub = intersection[[var, var + "_km", "Cons_name"]]
        
        # calculate constituency areas in km^2
        country_sf_proj["const_area_km2"] = country_sf_proj.geometry.area / 1_000_000
       
         # left join constituency areas with lengths to get a combined dataframe
        country_combined = country_sf_proj.merge(intersection_sub, on="Cons_name", how="left")
        # calculate density
        country_combined[var + "_density"] = (country_combined[var + "_km"] / country_combined["const_area_km2"])
        
        # add necessary columns to original country shapefile        
        country_sf = country_sf.merge(
        country_combined[["Cons_name", var + "_km", var + "_density"]],on="Cons_name",how="left")

        # save to the original country shapefile
        country_sf.to_file(f"/Users/sophiesunderland/Desktop/CMSE802F26/Shapefiles/Shapefiles/{country}/{country}_Constituencies.shp")
        print(f"Finished processing {country} for layer {layer}")
        
        
def count_all(layer = " "):
    # Loop over all countries in main dataset 
    for country in df_all["Country"].dropna().unique():
        # create a GeoDataFrame for the selected layer
        df_sub = gpd.read_file(df_main, layer = layer)
        # filter for the current country
        df_sub = df_sub[df_sub["Country"] == country]
        # project the layer to a projected coordinate system for area calculations
        sub_proj = df_sub.to_crs("ESRI:102022")
        
        # load shapefile for current country and project to the same coordinate system
        country_sf = gpd.read_file(f"/Users/sophiesunderland/Desktop/CMSE802F26/Shapefiles/Shapefiles/{country}/{country}_Constituencies.shp")
        country_sf_proj = country_sf.to_crs("ESRI:102022")

        # intersect layer with constituencies 
        intersection = gpd.overlay(
            sub_proj,
            country_sf_proj,
            how="intersection")

        # identify the variable name based on the layer
        var = ""
        if layer == "AFR_Mineral_Facilities":
            var = "facilities"
        elif layer == "AFR_Mineral_Deposits":
            var = "deposits"
        elif layer == "AFR_Infra_Power_Stations":
            var = "stations"
        elif layer == "AFR_Infra_Transport_Ports":
            var = "ports"

        # create count variable by summing the number of points in the selected layer/variable in each constituenc
        intersection[var] = intersection.groupby(intersection["Cons_name"]).size().reset_index(name=var)
        # select count and constituency name columns
        intersection_sub = intersection[[var, "Cons_name"]]
       
        # left join constituency areas with lengths to get a combined dataframe
        country_combined = country_sf_proj.merge(intersection_sub, on="Cons_name", how="left")
        
        # add necessary columns to original country shapefile        
        country_sf = country_sf.merge(
        country_combined[["Cons_name", var]],on="Cons_name",how="left")
        
        # save to the original country shapefile
        country_sf.to_file(f"/Users/sophiesunderland/Desktop/CMSE802F26/Shapefiles/Shapefiles/{country}/{country}_Constituencies.shp")
        print(f"Finished processing {country} for layer {layer}")