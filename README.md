# YOLOv5 and OAK D LITE

## Basic Overview:

1. Fly drone over area where objects are located
2. Take video using OAK D Lite camera
   - capVideo.py
   - The video taken will be save into a Video folder
3. Get images from the video frames
   - run getImgs.py, modify path of desired video to get images from
   - The images will be saved into an Images folder
4. Make an account in [Roboflow](https://roboflow.com/). Upload images saved to begin labeling images before training process
   - Recommended that the number of images per class(type of object) should be 1.5k
   - Recommended that the number of instances per class should be >= 10k.
5. Once images are labeled, follow tutorial to begin training process and export necessary blob file to run with oak d lite
   - Depthai Yolov5 Tutorial
     - https://colab.research.google.com/github/luxonis/depthai-ml-training/blob/master/colab-notebooks/YoloV5_training.ipynb
6. Helpful Links:
   - Roboflow yolov5 video tutorial: https://www.youtube.com/watch?v=MdF6x6ZmLAY
   - Robofloww yolov5 google colab: https://colab.research.google.com/drive/1gDZ2xcTOgR39tGGs-EZ6i3RTs16wmzZQ
   - Roboflow yolov5 blog: https://blog.roboflow.com/how-to-train-yolov5-on-a-custom-dataset/
