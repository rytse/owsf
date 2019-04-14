# OWSF (Open Weapon Site Finder)

![Intersections](https://cdn-images-1.medium.com/max/1000/1*dhY45s6L3Cqh82NMGwHGww.png)
![Intersection mapped out on Google Maps](https://cdn-images-1.medium.com/max/1000/1*ZpqoD2puhxw5aMiZ5eHi0w.png)

We used Google's Earth Engine to locate the sites of a patriot battery or a early warning system. So anywhere in the world these artifacts appear, they may point to a location of a patriot battery, or other early warning system. Displaying a combination of VH and VV polarizations will result in overlapping ascending and descending orbit interferences, we see that they consistently converge.

These intersections, when put on the ArcGIS maps(using their coordinates) lead us to discover that they are locations used by military or some military activity. 

We ran a Convolutional Neural Network that was fed the images of all such locations and others during training to find out all the other(basically predict with a degree of confidence) locations of the sites of potential military operations.

More information available on this project's [website](https://rytse.github.io/owsf/).

### Map View Link:

[Click Here!](https://cbsimmons4.github.io/owsf/)

## Built With

* [ArcGIS Online](http://www.arcgis.com/index.html) - Map
* [Google Cloud Platform](https://cloud.google.com) - VM
* [Tensorflow](https://tensorflow.org) - ML Framework
* [Google Earth Engine](https://earthengine.google.com/) - Google Earth Engine

## Authors

* **Ryan Tse** - [rytse](https://github.com/rytse)
* **Adeeb Abbas** - [adeeb10abbas](https://github.com/adeeb10abbas)
* **Cameron Simmons** - [cbsimmons4](https://github.com/cbsimmons4)
