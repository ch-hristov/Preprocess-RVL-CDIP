# Preprocess the RVL-CDIP dataset into a grouped by category format

The RVL-CDIP should be downloaded from the original website - https://www.cs.cmu.edu/~aharley/rvl-cdip/. Make sure you download the `labels_only.tar.gz` as well. This directory is particularly useful if you want to train a model on all images without carrying about benchmarks. For example to train a network for later use for transfer learning :).

0. Move the 2 downloaded files in a disk space which has 80 gb free space (incl the 37gb download)

1. run `tar -xvzf "./rvl-cdip.tar.gz"` 

2. The directory should look something like the image, without the dataset folder (that one is created automatically by this script)

![How your folder should look like before running this script](snapshot.png)

3. Use the compose.py to build the per category dataset. 
`python compose.py`

4. Done
