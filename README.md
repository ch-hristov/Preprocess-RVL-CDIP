# preprocess-rvl-cdip
Preprocess the RVL-CDIP dataset into a grouped by category format


The RVL-CDIP should be downloaded from the original website - https://www.cs.cmu.edu/~aharley/rvl-cdip/


1. Use the compose.py to build the per category dataset. Remember to replace all the paths to your own.
1. Use the notebook to build the per category dataset (make sure to change the paths to fit your own)
2. This dataset contains a lot of subfolders, that's why you need to also run the following command

`python flatten.py <main folder>`

This command will flatten each subfolder of 'main folder' argument. 
