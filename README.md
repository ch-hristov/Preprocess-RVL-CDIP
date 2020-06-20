# Preprocess the RVL-CDIP dataset into a grouped by category format

The RVL-CDIP should be downloaded from the original website - https://www.cs.cmu.edu/~aharley/rvl-cdip/. Make sure you download the `labels_only.tar.gz` as well.

0. Move the 2 downloaded files in a disk space which has 80 gb free space (incl the 37gb download)

For Windows: run `tar -xvzf "./rvl-cdip.tar.gz"` 

1. Use the compose.py to build the per category dataset. 
*IMPORTANT* Remember to replace all the paths to your own.
`python compose.py <main folder>`

This composes the dataset but it has a lot of folders by default. Run step 2 afterwards

2. This dataset contains a lot of subfolders, that's why you need to also run the following command
`python flatten.py <main folder>`

This command will flatten each subfolder of 'main folder' argument. 
