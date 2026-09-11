# Project Proposal
## Mapping territorial inequality across Africa

By Sophie Sunderland

## Summary

<!-- Provide a short summary of the project and its purpose. -->

African states are characterized by uneven patterns of state presence across territory. Existing studies argue that these uneven patterns should affect political outcomes, including access to public services and citizens' perceptions of government performance (e.g., [@Brinkerhoff2018]). However, many studies do not use spatial data to measure variation in state presence. Studies that do incorporate spatial data can often only capture state presence by a single measure, limiting the ability to compare types of presence within a single territory.

This purpose of this project is to use computational methods to processing GIS data on state presence across over 30 countries in Africa. Beyond processing the data, the project will also introduce a reproducible workflow for calculating measures of state presence using reusable functions that loop over countries in my dataset and merge measures to country constituency-level shapefiles. Calculating these measures will allow me to compare variation in state presence both across different types of infrastructure within a single territory and also presence between different territories. 

## Overview

<!-- Describe the research domain or problem area in a way that is understandable to a broad audience. Explain why this work matters and how computation or software supports it. -->

Historically, the projection of state power has varied widely across territory in African states. In precolonial Africa, the high cost of projecting power and the absence of imperatives to consolidate state authority resulted in concentrated cores of political authority [@Herbst2000]. Similar patterns of broadcasting power persisted into the colonial period. While some studies highlight the colonial state as a coercive actor (e.g., [@Young1994]), its reach was highly varied, even within countries [@Boone2003]. State power was largely projected into territories of economic or political relevance to the regime, such as resource-rich areas and capital cities [@Mann2008]. Even following independence, many nationalist leaders refrained from making strong efforts to extend the state into peripheral regions [@Herbst2000].

As a result, contemporary African states are characterized by persistent, uneven patterns of state presence. A growing literature has focused on the implications of uneven presence for political outcomes. Additionally, scholars have increasingly utilized spatial data to produce measures of presence for these analyses. For example, studies find that territories with less physical distance from urban centers, like regional or national capitals, receive better public service delivery and development outcomes [@Brinkerhoff2018; @Muller2023]. However, these measures cannot fully capture variation in state presence across territory. Relying on a single indicator of presence, like distance from a capital, overlooks heterogeneity within territories, as well as alternative forms of state presence within these territories. Other studies, such as those which rely on state capacity as a measure of presence, rarely or never include spatial data in the construction of these measures (e.g., [@Hendrix2010]).

Thus, the gap is an absence of quantitative, spatial measures capturing state presence in territories. This limits our understanding of where states have established a visible presence, how state presence varies across territory within countries, and how these spatial patterns relate to political outcomes. In short, variation in state presence cannot be studided without spatial measurements. 

Computational methods provide the tools to address this gap by analyzing GIS data across a large number of territories. By combining spatial data on state presence using physical and economic infrastructure with subnational territorial boundaries, computational methods facilitate constructing multiple measures of state presence across territory. These measures will allow for systematic comparisons of territorial inequality in state presence both within and between territories.

## Software or Project Description

<!-- Describe the software you will develop or improve. Explain the main functionality, the intended users, and the expected impact of the work. -->

I will develop a reproducible workflow and dataset of constituency-level infrastructure measures across more than 30 countries in Africa. The workflow will automate the processing of spatial data and the calculation of standardized infrastructure measures. The final dataset will provide novel measures of territorial inequality that can be compared both within and across countries.

The dataset is intended to serve as a publicly available resource for academics studying territory in Africa. By making constituency-level spatial measures available, the project will allow scholars to examine how territorial variation is related to political outcomes without having to rely on independent sources of spatial data. By facilitating comparison across countries, the dataset will make research more 
systematic research beyond individual country studies, where many spatial analyses are currently limited in scope.

## Project Goals and Timeline

<!-- Describe the short-term, medium-term, and long-term goals for the project. Include a brief timeline for the semester and indicate what will be completed by the first milestone and by the end of the semester. -->

The short-term goal for this project is to calculate measures of state presence for each infrastructure type in a single country. Then, my medium-term goal is to extend these calculations to the full set of countries for which I have working shapefiles. The long-term goal is to use these measures to compare variation in state presence across territories, both across different types of infrastructure and across different countries. I also plan to do an application of these measures by analyzing their association with a political outcome, such as assessments of government performance.

I aim to complete the short-term goal by the end of September. During October, I will work toward the medium-term goal of extending the workflow to achieve coverage of all countries in the shapefile dataset. During November, I will focus on identifying any issues and refining the measures. By the end of the semester, I aim to produce a reproducible workflow, a basic dataset of constituency-level infrastructure measures for as many countries as possible, visualizations of these measures, and comparisons of variation in these measures across and within countries.

## Methods and Workflow

<!-- Describe the main workflow, tools, or methods the project will use. Mention the software engineering practices you plan to apply, such as testing, documentation, environment management, or quality checks. -->

My main workflow will use reusable functions to loop over countries in my shapefile dataset, calculate measures of different types of infrastructure within each country's electoral constituencies, and merge these measures with the corresponding country constituency shapefile. I plan to create general functions for repeated spatial calculations, such as infrastructure density per constituency area and infrastructure counts within a constituency. These functions will be designed to produce multiple measures from different types of spatial data. For example, a density function could be used to calculate both road length per constituency area and railroad length per constituency area.

I will use tools including projecting data from one coordinate reference system (CRS) to a different CRS, spatial joins, and visualization of geographic data. Many of these tools are available in the GeoPandas library. 

This approach reduces the need to create variable or country specific code. I will document the workflow for using these reusable functions and the steps necessary to process each type of infrastructure data. I will also include checks to identify missing geographic data or inconsistent CRS between the infrastructure data and constituency shapefiles. To test functions, I will use an individual country and infrastructure type to ensure the measure is constructed accurately before applying the function to the entire country shapefile dataset.

## Anticipated Challenges

<!-- List the main challenges you anticipate and how you might respond to them. -->

One challenge is that I will be working with both GIS data and country constituency-level shapefiles, geographic data that each have their own CRS. These data may not align with one another, which impacts whether spatial merges and joins can be done. To respond to this, I develop a test to check whether the layers share the same CRS and make this a requirement for measurement calculations to proceed.

Another challenge is that some countries may have missing infrastructure data. Missing data may bias measures as showing high levels of inequality when it is instead the result of data availability. To respond to this, I will distinguish between true zero measures of infrastructure and missing data. I will also document countries with any data missingness.

## Expected Outcomes

<!-- Describe what success would look like for this project by the end of the semester. -->
A successful project would develop a reproducible workflow for computing quantitative spatial measures of territorial inequality across subnational territories in Africa. I plan to prioritize developing strong measures with the available spatial data over having complete coverage for every country on the continent. In other words, a successful project will develop a reproducible measurement framework that can be applied across additional countries in the future.

In addition, a successful project will develop at least one measure for each type of physical and economic infrastructure. For example, road networks can be measured as road density given constituency area. Density can also be normalized by constituency population or by distinguishing between major national roads and regional-level roads. However, rather than developing every possible measure for an infrastructure type, a successful project will have one robust measure for all infrastructure types. 

A successful project will also merge all of the constructed measures with country electoral constituency shapefiles to allow for the visualization of the measures.
