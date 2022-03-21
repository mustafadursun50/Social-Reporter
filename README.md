# SocialReporter
As a master thesis a system was developed, which recognizes the interesting moments in events of the university, in order to post it in the social media.

## Requirements
It is recommended to use following versions: 

```
Python=3.7.1
pip=21.1.2
```


## How to setup
- All required packages are summarized in requirements.txt. Install all these packages via command: 
``
pip -r requirements.txt
``
- Folder adapted_python_libs contains two modified Python classes (`object_detection.py` and `facial_emotion_recognition.py`). 
The just installed classes must be overwritten with these.
  1. Navigate to the install location of ``object_detection.py``. This should be in: 
  ``
  C:\Users\{username}\AppData\Local\Programs\Python\Python37\Lib\site-packages\cvlib\object_detection.py
  ``
  2. Replace it's content with: 
  ``
  adapted_python_libs/object_detection.py
  ``
  3. save replaced file.
  4. Repeat the process for ``facial_emotion_recognition.py``

- Install Tessarct as described here
``
https://medium.com/@marioruizgonzalez.mx/how-install-tesseract-orc-and-pytesseract-on-windows-68f011ad8b9b
``. Select as installation location: ``C:/Program Files (x86)/Tesseract-OCR``. 
- You can also choose another installation location. Then adjust the corresponding paths in ``config.py (lines 31 and 32)``.



## How to use
- Start main program via command:
``
python social_reporter.py
``
  - The files are loaded one after the other from the folder ``input`` and analyzed
  - The files in the folder must have the following format: ``Cam01_20211015_174122``
  - If a social media relevant image is given, the image will be extracted to the folder: ``output``
  - In addition, an entry will be written in the file ``output/contents.csv``

- Start collage maker via command:
``
python collage_maker.py
``
  - Photo collages are created from the folder ``output``
  - If there are enough single images, the collage will be created again in the folder ``output``


