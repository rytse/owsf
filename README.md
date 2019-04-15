# OWSF (Open Weapon Site Finder)

![Intersections](https://cdn-images-1.medium.com/max/1000/1*dhY45s6L3Cqh82NMGwHGww.png)
![Intersection mapped out on Google Maps](https://cdn-images-1.medium.com/max/1000/1*ZpqoD2puhxw5aMiZ5eHi0w.png)

We used the Google Earth Engine to pull data from the Sentinel1 satellite. We analyzed Sentinel's C-band radar data and looked for places where missiles' guidance radars cause consistent interference. We detected this low-power but consistent interference by tracking the pixels that were the "brighest" over the longest period of time. Using this multi-temporal analysis method, we were able to detect several types of military radar systems (more on this later), but by applying a clever polarimetry trick, we were able to isolate C-band phased array radars, which are most commonly used for Patriot surface-to-air missiles. Specifically, we analyzed the "bright spots" in each polarization, and noted that phased array radars interfere with each polarization differently. These differences allowed us to identify Patriot missiles by distinct X-pattern shown below. From images like these, we performed image processing to isolate the coordinates of the missile sites. While we did not have time to run our image processing payload on the entire Earth, we applied our methods to several geographic regions, including part so the US, the Middle East, Western Europe, and Eastern Asia. The sites that we found are indicated below on the map.

More information available on this project's [website](https://rytse.github.io/owsf/) and [DevPost](https://devpost.com/software/owsf).

## Built With

* [ArcGIS Online](http://www.arcgis.com/index.html) - Map
* [Google Cloud Platform](https://cloud.google.com) - VM
* [Tensorflow](https://tensorflow.org) - ML Framework
* [Google Earth Engine](https://earthengine.google.com/) - Google Earth Engine

## Authors

* **Ryan Tse** - [rytse](https://github.com/rytse)
* **Adeeb Abbas** - [adeeb10abbas](https://github.com/adeeb10abbas)
* **Cameron Simmons** - [cbsimmons4](https://github.com/cbsimmons4)
