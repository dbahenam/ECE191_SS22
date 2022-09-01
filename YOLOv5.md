# YOLOv5 and OAK D LITE

1. Fly drone over desired detected objects
2. Take video using OAK D Lite camera
   - capVideo.py
   - The video taken will be save into a Video folder
3. Get images from the video frames
   - run getImgs.py, modify path of desired video to get images from
   - The images will be saved into an Images folder
4. Make an account in Roboflow.com to begin labeling images and training
5.
6. Once images are labeled and model is trained, follow tutorial below to export necessary blob file to run with oak d lite
   https://colab.research.google.com/github/luxonis/depthai-ml-training/blob/master/colab-notebooks/YoloV5_training.ipynb
   - Helpful Links:
     https://www.youtube.com/watch?v=MdF6x6ZmLAY
     https://colab.research.google.com/drive/1gDZ2xcTOgR39tGGs-EZ6i3RTs16wmzZQ
     https://blog.roboflow.com/how-to-train-yolov5-on-a-custom-dataset/
7.
