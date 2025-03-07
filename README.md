# Alfa Zeta Flip Dot Display XY5 28x7 Python

[日本語版はこちら](README_JP.md)

This project provides Python code to control the Alfa Zeta Flip Dot Display XY5 28x7 using a Raspberry Pi 4B and RASPI HAT. The `frames` directory includes demo frames and the original video file `V.mp4` used to generate these frames. There are three main functionalities included in this directory:

## Table of Contents

- [Demo](#demo)
- [MP4 Conversion](#mp4-conversion)
- [Frame Display](#frame-display)
- [Installation](#installation)
- [Usage](#usage)
- [Control Instructions](CONTROL.md)

## Demo

The `demo.py` script allows you to display specific patterns on the flip-dot display. It uses a matrix like the one below, consisting of 0s and 1s, to create patterns:

```python
matrix = [
    "0000000000000000000000000000",
    "0000000000100000000000000010",
    "1101100000100000000100010000",
    "1010101110101010101110111010",
    "1010101010110010100100010010",
    "1000101110101011100110011010",
    "0000000000000000000000000000"
]
```

## MP4 Conversion

The `MP4.py` script converts video files into black and white, resizes them to 28x7, and converts them into frames using OpenCV. These frames are saved into a directory called `frames`.

## Frame Display

The `start.py` script reads frames from the `frames` directory and displays them on the flip-dot display at 15 frames per second.

## Installation

To set up the environment for this project, follow these steps:

1. **Enable Serial Port and Disable Serial Console**:
    1. Open the Raspberry Pi configuration tool:
    ```bash
    sudo raspi-config
    ```
    2. Navigate to `Interfacing Options` and select `Serial`.
    3. When asked "Would you like a login shell to be accessible over serial?", select `No`.
    4. When asked "Would you like the serial port hardware to be enabled?", select `Yes`.
    5. Exit the configuration tool and reboot your Raspberry Pi:
    ```bash
    sudo reboot
    ```

2. **Create and navigate to the `flip` directory**:
    ```bash
    mkdir flip
    cd flip
    ```

3. **Clone the repository into the `flip` directory**:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    ```

4. **Create a virtual environment**:
    ```bash
    python3 -m venv env
    ```

5. **Activate the virtual environment**:
    ```bash
    . /env/bin/activate
    ```

6. **Install the required dependencies**:
    ```bash
    pip install opencv-python pyserial
    ```

These steps will set up your environment to run the scripts provided in this repository.

## Usage

**Note**: Before running any of the scripts, you must activate the virtual environment:
```bash
. /env/bin/activate


## Usage

**Note**: Before running any of the scripts, you must activate the virtual environment:
```bash
. /env/bin/activate

### Demo

1. **Activate the virtual environment**:
    ```bash
    . /env/bin/activate
    ```

2. **Run the demo script**:
    ```bash
    python demo.py
    ```