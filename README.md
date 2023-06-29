# Flood Detection

An AI model that detect real-time water area and water level for further purposes.

## Description

In this project, I trained a YOLOv8n custom model on [this](https://www.kaggle.com/datasets/gvclsu/water-segmentation-dataset) dataset on Kaggle, as well as the ones I labeled myself using Roboflow's help, to make the model able to detect water in an image/video. The [model best.pt](https://github.com/duchieu260503/Flood-detection/blob/main/best.pt) is included in this repository.

Once the model is ready, some additional information needs to be provided to measure the water level: The line's 2 tips coordinates that are perpendicular with the water surface. This is crucial to calculate the water level.

![Technical Approach](https://github.com/duchieu260503/Flood-detection/blob/main/media/Technical%20approach.JPG)

Additionally, the number of pixels in a real-life meter, the tip's real height, and the water level that may trigger a warning.

The result can be displayed while the program is running, as well as an output video is saved on the local machine.

## Getting Started

### Dependencies

Tested on Python 3.11.3 and PIP 23.1.2

### Installing

Locate to your workspace folder using -cd command then type: 
```
git clone https://github.com/duchieu260503/Flood-detection.git
```
Libraries used:

- [Tkinter](https://docs.python.org/3/library/tkinter.html)

- [Ultralytics](https://ultralytics.com/) and its [requirements](https://github.com/ultralytics/ultralytics/blob/main/requirements.txt)

- [Shapely](https://shapely.readthedocs.io/en/stable/index.html)
  
To install all the libraries needed, type:
```
cd Flood-detection
pip install -r requirements.txt
```

### Executing program

You can either run the program in your favourite code editor (VS Code, Jupyter Notebook, ...) or simply by command.
```
python main.py
```
A GUI interface will pop-up and assist you with the launch of the program.

### Run example

Once the GUI pop up, it will look like this:

![GUI](https://github.com/duchieu260503/Flood-detection/blob/main/media/GUI.JPG)

Then type exactly like the GUI's suggestions on every entry, and select the video in the media folder.

The result will look something like this:

https://github.com/duchieu260503/Flood-detection/assets/16372230/defb4c22-a549-40b6-82e3-be5eebe6fad6

And the result video will be saved in the Flood-detection folder.

## To be developed

The program is still imperfect, as the model only works best with single-area per image, which means the model can not detect 2-or-more water areas in a single frame.

Also, the intersections-calculating algorithms will pose some troubles when 2 or more intersections were found between the line and the annotation mask, so the line coordinates should be chosen carefully.

This will be fixed and modified in future updates.

## Authors

Pham Duc Hieu

Email: duchieu260503@gmail.com


## License

This project is free to use, re-use, or develop, as long as the YOLOv8 [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) is satisfied.
