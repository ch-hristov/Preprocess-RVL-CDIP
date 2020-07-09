# Preprocess the RVL-CDIP dataset into a grouped by category format

The RVL-CDIP should be downloaded from the original website - https://www.cs.cmu.edu/~aharley/rvl-cdip/.
This repository is particularly useful if you want to train a model on all images without carrying about benchmarks. For example to train a network for later use for transfer learning :).

0. Move the downloaded file in a folder which has a lot of disk space.

1. run `tar -xvzf "./rvl-cdip.tar.gz"` 

2. The directory should look something like the image, without the dataset folder (that one is created automatically by this script)

![How your folder should look like before running this script](snapshot.png)

3. Use the compose.py to build the per category dataset. Note it might take a while.

`python compose.py`

4. Done
