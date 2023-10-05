# HandHeld Object Modeling Using Neural Radiance Fields (NeRF)
We used the Nerfstudio opensource library to train the networks on the clouds.
the network can be trained locally using cuda on Nvidia GPUs.

Using a video \ set of images of a handheld object, we use image processing to extract the hand from the images and remove it, then we train the result frames on the cloud again using the nerfstudio library.
### steps
1. creating image frames out of an input video and resizing images.
2. running colmap on the images for preprocessing the data.
3. training the colmap output data using nerf.
4. creating a rendering result.

### Example of images Before Hand Extraction ( 219 Frames | 720 x 1280)

we exctracted the  frames from the video and we got the following sequence.

![before_hand_extraction.gif](data/before_hand_extraction.gif)

### Example of images After Hand Extraction ( 219 Frames | 480 x 853)

After removing the hands and the background noise, we got the following images.

![after_hand_extraction](data/after_hand_extraction.gif)

### Colmap Poses

After using Colmap on the sequence, we got the poses in this sequence around the object.

![colmap_poses](data/colmap_poses.png)

### Rendering Result
![render](renderResults/render.gif)
![render2](renderResults/render2.gif)
![render3](renderResults/render3.gif)
![render4](renderResults/render4.gif)
