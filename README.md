AI VISION LAB
A modular python-based toolkit for image processing and computer vision tasks. 
this project currently implements automated face detection using Haar Cascades and includes utilities for grayscale conversion and edge detection
FEATURE:
1. FACE DETECTION: Automatically identifies and highlights faces in images using OpenCv
2. EDGE DETECTION: Implementation of Canny edge detection for structural analysis
3. GRAYSCALE CONVERSION: Quick pre-processing utilities for vision pipelines
4. MODULAR DESIGN: Easily extensible structure with dedicated processors for different CV tasks.

INSTALLATION
 clone the repository: 
    https://github.com/CODEWITHNDAHIRO/AI_Vision_lab.git
    cd AI_Vision_lab
 install dependencies:
    pip install -r requirements.txt

USAGE
1. Place an image name it input.jpg in the root directory.
2. Run the main script:
   python main.py
3. The processed image will be saved as output.jpg

PROJECT STRUCTURE 
 . main.py: Entry point of the application.
 . processors/: contains core logic for face_detection,edge_detection,and grayscale.
 . requirements.txt: List of necessary Python packaages (OpenCV,etc...)

CONTRIBUTING
contributions are welcome! if you'd like help improve this lab,please feel free to:
1.Open an Issue to report bugs or suggest features
2.Submit a pull Request with new vision processors or optimizations.
3.Help increase the project's activity by contributing to documentation or code
 
