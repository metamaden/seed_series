# seed_series
This is a project in generative image production. It will explore the impact of randomization on various image modification tasks.

# SMPTE seed series

This series explores random pixel offsets applied to a base image of the SMPTE television test pattern. These images are available as NFTs in the [SMPTE seed series](https://opensea.io/collection/smpte-seed) gallery on OpenSea.

The base image was [downloaded](https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/SMPTE_Color_Bars_16x9.svg/1024px-SMPTE_Color_Bars_16x9.svg.png) then modified with the python script [`make_new_smpte_seed.py`](https://github.com/metamaden/seed_series/blob/main/series/generative/smpte/src/make_new_smpte_seed.py).

The script to generate the first 11 images in this seed series is callable from windows command line using `run_series_script.exe`. See below for an example image.

![SMPTE seed 7 image](https://github.com/metamaden/seed_series/blob/main/series/generative/smpte/img/smpte_seed_7.jpg?raw=true)

# Rococo flowers

This series applies the [Inception V3](https://ai.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html) Deep Dream image filter algorithm to a fine art image. Code for this project comes from [this tutorial](https://www.tensorflow.org/tutorials/generative/deepdream), with light modifications. The base image for this series is "Flowers in a Rococo Vase" by Paul Cézanne, and was downloaded from the National Gallery of Art website [here](https://www.nga.gov/collection/art-object-page.46580.html).

Images in this series were captured over the course of a single continuous run of model training, where training progress is denoted by the "steps" in file names. Before training, the seed of 1 was set to ensure run reproducibility. The images are available as NFTs from the [Rococo flowers](https://opensea.io/collection/rococo-flowers) collection on OpenSea. An example of the image at step 50 is shown:

![Rococo flowers, step 50, seed 1](https://github.com/metamaden/seed_series/blob/main/series/generative/rococo_flowers/img/rococo-flowers_step50_seed1.jpg?raw=true)
