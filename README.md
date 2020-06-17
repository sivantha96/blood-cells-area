# blood-cells-area

Detect all the blood cells and calculate the area of them from a given video

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install following packages before using the [blood-cells-area](https://github.com/sivantha96/blood-cells-area)

```bash
pip install cv2 numpy
```

## Usage

Open a terminal in the source directory and run the following command

```bash
python main.py
```

## Using a different video file

**Method 01** - Replace the **video.mp4** file with the file you want

**Method 02** - Add the file you want (**your-file-name.mp4**) to the source directory and do the following change

```python
vid = cv2.VideoCapture("your-file-name.mp4")
```
