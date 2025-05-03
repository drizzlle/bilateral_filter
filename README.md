# Bilateral Filter Implementation

This project implements a bilateral filter for image processing using Python, NumPy, and OpenCV.

## What is a Bilateral Filter?

A bilateral filter is a non-linear, edge-preserving smoothing filter. It replaces each pixel's intensity with a weighted average of intensity values from nearby pixels. The weights depend on both:
1. The spatial distance (like traditional Gaussian smoothing)
2. The difference in intensity values (this helps preserve edges)

## Project Structure

```
bilateral_filter/
├── data/           # Place input images here
├── results/        # Filtered images will be saved here
├── bilateral_filter.py
├── requirements.txt
└── README.md
```

## Setup and Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your input image in the `data` folder and name it `input_image.jpg`
2. Run the script:
```bash
python bilateral_filter.py
```

The script will:
- Load your input image
- Apply the bilateral filter
- Display a comparison of original and filtered images
- Save the filtered image in the `results` folder

## Parameters

The bilateral filter has three main parameters:
- `diameter`: Diameter of each pixel neighborhood (default: 9)
- `sigma_color`: Filter sigma in the color space (default: 75)
- `sigma_space`: Filter sigma in the coordinate space (default: 75)

You can adjust these parameters in the code to achieve different filtering effects. 