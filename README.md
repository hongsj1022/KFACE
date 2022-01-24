- Directory for image data and mat file
- Please make excel file with all image data path containing filename
  

- Please make mat file(version 7.3) containing following contents with matlab
	Data path : All image data path containing filename
	Attributes name : Male, 10s, 20s, 30s, 40s, 50s
	Labels : For each data, express whether it is 0 or 1 for each attribute
	You can make excel file first, and import excel file at matlab.

- Feature extraction

python --data_dir <your_data_dir> --save_feature <xxx.csv> --save_label <yyy.csv> kfacefeature_extraction.py

if error occurs with h5py, change mat file to h5py by using following command.
python mat73_to_pickle.py <filename.mat>


- Model training

python --feature <xxx.csv> --label <yyy.csv> --save_model <your_model.pkl> kfacetrain.py


- Prediction

python --model <your_model.pkl> --input_dir <test_image_dir> --output_dir <result_image_dir> kfacepred.py


- Data_extension directory
There are python files to extend image data with rotating, flipping, and changing brightness.
And face_extract.py extracts only face in image and save it.
In each python file, it is required data and excel file containing data path.
After configure dataset and excel file,  
Usage : python 12_brightness.py
                    face_extract.py
                    image_flip.py
                    image_rotate.py