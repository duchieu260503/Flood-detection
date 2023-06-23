# Flood Detection

An AI model that detect real-time water area and water level for further purposes.

## Description

In this project, I trained a YOLOv8n custom model on [this](https://www.kaggle.com/datasets/gvclsu/water-segmentation-dataset) dataset on Kaggle, as well as the ones I labeled myself using Roboflow's help, to make the model able to detect water in an image/video. 

Once the model is ready, some additional information needs to be provided to measure the water level: The line's 2 tips coordinates that are perpendicular with the water surface. This is crucial to calculate the water level.

![Technical Approach](https://github.com/duchieu260503/Flood-detection/blob/main/Technical%20approach.JPG)

Additionally, the number of pixels in a real-life meter, the tip's real height, and the water level that may trigger a warning.

![Calculate distance](https://github.com/duchieu260503/Flood-detection/blob/main/Calculate%20distance.JPG)

The result can be displayed while the program is running, as well as an output video is saved on the local machine.

## Getting Started

### Dependencies

Use [this](https://github.com/ultralytics/ultralytics/blob/main/requirements.txt) requirements list in order to run YOLOv8 on the local machine.

### Installing



### Executing program

You can either run the program in your favourite code editor (VS Code, Jupyter Notebook, ...) or simply by command.

If you are running the code by command, locate the repository location then type:
```
python main.py
```
A GUI interface will pop-up and assist you with the launch of the program.

## Help

The program is still imperfect, as the model only works best with single-area per image, which means the model can not detect 2-or-more water areas in a single frame.

Also, the intersections-calculating algorithms will pose some troubles when 2 or more intersections were found between the line and the annotation mask, so the line coordinates should be chosen carefully.

## Authors

Pham Duc Hieu

Email: duchieu260503@gmail.com


## License

This project is free to use, re-use, or develop, as long as the YOLOv8 [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) is satisfied.
