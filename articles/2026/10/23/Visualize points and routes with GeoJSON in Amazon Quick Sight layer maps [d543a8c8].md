---
id: "d543a8c819225bfc"
title: "Visualize points and routes with GeoJSON in Amazon Quick Sight layer maps"
url: "https://aws.amazon.com/blogs/machine-learning/visualize-points-and-routes-with-geojson-in-amazon-quick-sight-layer-maps"
link: "https://aws.amazon.com/blogs/machine-learning/visualize-points-and-routes-with-geojson-in-amazon-quick-sight-layer-maps"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-23T16:24:55Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Amit Makashir"]
language: "en"
summary: "With Amazon Quick Sight layer maps, you can now plot points and routes, like store locations across a city or flights leaving an airport. Geospatial maps help businesses spot patterns that are tied to location, like how a region is performing or where customers are concentrated. Amazon Quick Sight supports this with multiple map types, including point maps, filled maps, and layer maps. When…"
tags: ["Amazon Quick Sight", "Intermediate (200)", "Technical How-to"]
orgs: ["Amazon"]
topics: ["agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 2309
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Visualize points and routes with GeoJSON in Amazon Quick Sight layer maps

AWS Machine Learning Blog · Amit Makashir · 2026-10-23

Artificial Intelligence
Visualize points and routes with GeoJSON in Amazon Quick Sight layer maps
With Amazon Quick Sight layer maps, you can now plot points and routes, like store locations across a city or flights leaving an airport. Geospatial maps help businesses spot patterns that are tied to location, like how a region is performing or where customers are concentrated. Amazon Quick Sight supports this with multiple map types, including point maps, filled maps, and layer maps. When layer maps first launched, you could upload a GeoJSON file to draw custom shape layers, such as sales territories or districts, and join those shapes to a dataset. That handled regions and boundaries well, but it didn’t cover the individual locations inside them or the routes running between them.
Layer maps now support two more geometry types from the same GeoJSON workflow: Point and LineString. Points mark specific locations, such as individual store or facility sites. A LineString traces the route between locations, like a delivery path or a flight between airports.
Amazon Quick Sight, the business intelligence (BI) capability of Amazon Quick, is a unified BI service. It delivers modern interactive dashboards, natural language querying, pixel-perfect reports, machine learning (ML) insights, and embedded analytics at scale. Amazon Quick brings together AI agents for business insights, research, and automation in one integrated experience, helping you work smarter and faster while maintaining security and access policies.
In this post, we walk through the dataset and GeoJSON structure that layer maps require. We also explain how points and lines work in a layer map visual and when to choose each. Finally, we cover advanced techniques for controlling the viewport, layering geometries, and updating GeoJSON files programmatically.
Dataset structure considerations
A layer map gets its shapes from a GeoJSON file and its metrics from a Quick Sight dataset, and a shared key joins the two. How you structure each one determines what the map can show. This section covers what you need before you start and how a GeoJSON file is organized.
Prerequisites
The following are the prerequisites that you need before creating a layer map in Quick Sight:
- A GeoJSON file describing your geometry.
- A Quick Sight dataset holding the metrics and dimensions.
- A join key shared between the Quick Sight dataset and the GeoJSON file.
- The GeoJSON file must be saved in .geojson format, with a maximum supported file size of 100 MB.
Structure of the GeoJSON file
GeoJSON is a JSON-based format for describing geographic features such as points and lines.
The structure of the file is as follows:
- FeatureCollection is the whole file. It has a type of FeatureCollection and a features array.
- Feature is a single map element. It carries a geometry (the shape) and a properties object, which holds the join key.
- geometry has a type (Point, LineString, or Polygon) and its coordinates. The coordinates hold a single [longitude, latitude] position for a Point, and an ordered list of positions for a LineString.
Configuring the Quick Sight dataset and its GeoJSON
In Quick Sight, when you configure a layer in a layer map visual, there are two primary settings to consider. The first is the Geometry type to visualize, which sets which geometry from the GeoJSON file renders: Points, Lines, or Polygons. A layer renders one geometry type at a time, so when a file mixes types like the preceding example, only Features of the selected type appear on the map. The second is matching the Shape file key field to the Dataset key field, which links each Feature in the GeoJSON to a row in your Quick Sight dataset. The field names don’t need to be identical, but the values do. The following two examples show this end to end, first a LineString layer and then a Point layer.
Example: LineString layer
Consider example data showing a flight from JFK to a destination city like Los Angeles. The GeoJSON structure for a single datapoint is configured as follows:
The corresponding row in the Quick Sight dataset contains the following information:
The route_id field is used to join the Quick Sight dataset with the GeoJSON file. The GeoJSON holds one such feature per route, and the dataset one row per route. The Geometry type to visualize is set to Lines.
Example: Point layer
Consider example data showing a retail store location like Long Island City. The GeoJSON structure for a single datapoint is configured as follows:
The corresponding row in the Quick Sight dataset contains the following information:
The store_id field is used to join the Quick Sight dataset with the GeoJSON file. The GeoJSON holds one such feature per store, and the dataset one row per store. The Geometry type to visualize is set to Points.
Lines on layer map visuals
Layer map visuals now support LineString geometry, connecting an ordered list of coordinates into a single path. As covered in the data structure section, each route is one feature, and its coordinates are the ordered positions the map connects in sequence.
Use lines when the relationship between locations is what you want to show, such as flight paths, delivery routes, shipping lanes, or pipeline segments. The visual draws each path from the coordinates in your GeoJSON file rather than generating it from your data at load time. A field from your joined dataset can determine the line color encoding, so you can group routes by whatever that field represents. In addition to color, you can customize lines with width and opacity controls to adjust visual prominence and clarity on the map. The join key in the GeoJSON properties object ties each LineString to the dataset row behind its tooltip and color.
For example, an airport operations team might map the flights leaving New York (JFK) on a given day. The GeoJSON file holds one LineString per route, keyed by a route ID that joins to the dataset. Each line starts at JFK and ends at its destination, such as Los Angeles, Chicago, or Miami. The dataset supplies the origin, destination, and carrier that show up in the tooltip.
Points on layer map visuals
Amazon Quick Sight offers a native point map visual type that geocodes location names automatically and refreshes with your SPICE schedule or Direct Query connection. It supports dynamic point sizing, color encoding, and point styles such as cluster points and heatmap density gradients. It works best with data that changes frequently and where you want the map to respond to those changes visually.
With the added support for GeoJSON point layers in layer map visuals, Quick Sight now offers a second point mapping capability with a few key differences. Layer map visual points use a uniform marker size and don’t support geocoding, so you provide explicit coordinates in the GeoJSON file. In return, you can control the viewport precisely, locking the map to an exact geographic region, and disabling panning and zooming.
The following table summarizes the key differences:
Choose layer map visual points when:
- You require a locked, non-scrollable viewport.
- Your locations are fixed and curated (such as regional offices, distribution centers, retail stores) rather than changing with each data refresh.
- You plan to combine points with other geometry types (covered in the advanced use cases section).
Consider a retail brand whose regional managers use a Quick Sight dashboard to track store performance across a metro area. The GeoJSON file contains a Point feature for each store with a store ID property that joins to the dataset. The dataset holds the metrics (store type, monthly revenue, daily foot traffic) that drive the tooltip and color encoding. You position the map at the zoom level covering the metro area, then disable map navigation so the map renders at a consistent view on every load. Managers can’t accidentally zoom out to a national or global view.
Advanced use cases
The previous sections cover a standard layer map setup. Use the following techniques when you need more control over what readers see, want to combine geometry types in a single view, or need geometry that changes over time.
Controlling the viewport
When you need to control the viewport in layer map visuals, you can pan and zoom to the view you want manually. Then disable map navigation to lock it in place. For use cases where you need more precise boundaries or programmatic control, you can set the exact viewport coordinates through the visual definition using the Quick Sight APIs.
The layer map visual stores its viewport configuration in the MapState property within ChartConfiguration. This property accepts two fields:
- Bounds: The geographic coordinates defining the minimum visible area (North, South, East, West).
- MapNavigation: ENABLED or DISABLED to control whether readers can pan and zoom.
Although the bounds property is not exposed on the console, you can set these bounds when working with the dashboard definition JSON for programmatic asset management. For example, to define the bounds, modify the MapState block in the visual definition, then call the CreateDashboard or UpdateDashboard APIs.
The bounds define the minimum area that is guaranteed to be visible. The map zooms to make sure this entire area fits within the visual container. For the tightest fit with minimal extra space added to the map, match the aspect ratio of your bounds to the shape of your visual container.
Layering geometries
For use cases that require combining multiple geometry types into a single view, you can layer visuals on top of each other. For example, the following screenshot demonstrates plotting customer locations as points within US regional boundaries defined by polygons. This composition shows which territories have the highest customer density and can be used to correlate with other metrics present in the dataset like performance.
This second example demonstrates combining points as stops along a delivery route path. The LineString draws the planned route, and Point features mark each scheduled stop along the way.
To layer geometries, you stack multiple layer map visuals on top of each other, following these steps:
- Use free-form layout: Change the sheet layout setting to free-form so that visuals can overlap and stack.
- Create two layer map visuals: Create the two layer map visuals that you combine into a single view, such as one using a Point GeoJSON file and one using a LineString GeoJSON file.
- Use matching bounds: Using the approach previously described for controlling the viewport, verify all layer map visuals use identical bounds to have the same underlying map view.
- Disable panning and zooming: For each layer map visual, disable the panning and zooming under Map options so that alignment stays the same.
- Hide the base map and background on upper layer: Set the upper visual’s background to hidden under Display settings and disable the base map under Map options.
- Stack the visuals: Move the top visual on top of the base layer using drag-and-drop or by matching precise size and position coordinates under Display settings.
Layer ordering follows the visual stacking order in the free-form layout. To change a visual’s position in the stack, choose the menu icon (three dots) on the visual, then choose Send backward or Bring forward. Readers can access the tooltip of the topmost visual, so place the layer that readers need details from on top. Each sheet supports up to five layer map visuals.
Dynamically updating GeoJSON
Unlike other Quick Sight visuals where data refreshes through SPICE or Direct Query, layer map geometry lives in the GeoJSON file itself. When your dataset refreshes on schedule, the metrics update (for example, colors change and tooltip values refresh), but the geometry remains at its original position.
To update what appears on the map, like a new route, new point locations, or updated boundaries, you need to update the GeoJSON file and republish the dashboard. You can replace a GeoJSON file manually through the Quick Sight console by editing the layer map visual within the Analysis and uploading a new file. This works for infrequent changes such as updating territory boundaries quarterly or adding a new store location.
For automated, on-demand, or dynamic updates, the process involves Amazon Simple Storage Service (Amazon S3) and the Quick Sight APIs outlined in the following steps:
- Upload the new GeoJSON to Amazon S3: Generate your updated geometry and save it to an Amazon S3 bucket. Custom solutions can use other AWS services such as Amazon Location Service to create the GeoJSON files.
- Reference the file on the dashboard definition: The dashboard definition contains a StaticFiles array with a SpatialStaticFile entry for each GeoJSON file. Modify the file reference to the S3 location of your updated file entry for each GeoJSON file.
- Call the UpdateDashboard API: Submit the updated definition with the new file reference using the UpdateDashboard API.
- Call the UpdateDashboardPublishedVersion API: Publish the change so it is visible to dashboard readers with the UpdateDashboardPublishedVersion API.
The following example uses this pattern to support on-demand map updates in an embedded dashboard to generate optimal routes between locations and waypoints. Although outside the scope of this post, this represents an advanced use case that combines each of the preceding approaches.
Conclusion
In this post, we showed how to use Point and LineString geometry in Amazon Quick Sight layer maps to plot specific locations and the routes between them. We covered the GeoJSON structure and dataset join that layer maps require, and compared layer map points with the native point map. We also walked through advanced techniques for controlling the viewport, layering separate visuals into one view, and refreshing GeoJSON files with Amazon S3 and the Quick Sight APIs.
To learn more about layered maps, refer to the Amazon Quick Sight layered maps documentation. Visit the Amazon Quick Community to connect with peers and stay updated on the newest features and resources.
