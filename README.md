# HandHeld Object Modeling Using Neural Radiance Fields (NeRF)
We used the Nerfstudio opensource library to train the networks on the clouds.
the network can be trained locally using cuda on Nvidia GPUs.

Using a video \ set of images of a handheld object, we use image processing to extract the hand from the images and remove it, then we train the result frames on the cloud again using the nerfstudio library.
### steps


### Images Before Hand Extraction
![example_image1](images/before_extracting_hand/example_image1.png)
![example_images2](images/before_extracting_hand/example_images2.png)
![example_image3](images/before_extracting_hand/example_image3.png)
### Images After Hand Extraction
![image_1](images/after_extracting_hand/image_1.png)
![image_2](images/after_extracting_hand/image_1.png)
![image_3](images/after_extracting_hand/image_1.png)
### Result
![render](images/render.gif)

