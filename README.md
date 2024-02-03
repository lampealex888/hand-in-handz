# Getting Started

  ### Pre-requisites
  
  Python: (3.8.5)<br>
  Anaconda Distribution: To download click [here](https://www.anaconda.com/products/individual).
  
  ### Procedure

  Step 1: 
  ```bash
  conda create --name gest python=3.8.5
  ```
  
  Step 2:
  ```bash
  conda activate gest
  ```
  
  Step 3:
  ```bash
  pip install -r requirements.txt
  ```
  
  Step 4:
  ```bash 
  conda install PyAudio
  ```
  ```bash 
  conda install pywin32
  ```
  
  Step 5:
  ``` 
  cd to the GitHub Repo till src folder
  ```
  Command may look like: `cd C:\Users\.....\Gesture-Controlled-Virtual-Mouse\src`
  
  Step 6:
  
  For running the Gesture Controller:
  ```bash 
  python Gesture_Controller.py
  ```