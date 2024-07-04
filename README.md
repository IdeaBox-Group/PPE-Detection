# PPE-Detection
This is the documentation of PPE Detection Project created by IdeaBox. The idea is to detect workers that wear PPE using CCTV to ensure the safety of the worksite.

## How to Use
1. Download the requirements
   This PPE application should be delivered in a .zip file. Extract the zip file into whereever you wish to install it. Make sure that the location is widely accessible.
   
3. Set up your environment
   Make sure python is installed on your computer, then run this line on the terminal.
   
   ```
   python -m venv env
   env\Scripts\activate
   pip install -r requirements.txt
   ```
5. Run the code
   Navigate to the location where you extracted the zip file.
   
   ```
   python main.py
   ``` 
## Documentation
We use YOLOv8 to detect the PPE, you can look at the training stage in [this](https://colab.research.google.com/drive/187Al1GHehgeVaiZflh95KQ1IoXRpyLQA?hl=id#scrollTo=u1a7Fk2T5ZGo)

## Links
Test Video : [Youtube](https://www.youtube.com/watch?v=s1n6nBhVzdo)
Test Image : [WikiMedia](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/69_Fisk_IRT_work_vests_jeh.jpg/800px-69_Fisk_IRT_work_vests_jeh.jpg)

## Collaborators
Ideabox Team
