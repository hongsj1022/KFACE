# coding: utf-8
from __future__ import print_function
import sys
import os
import pandas as pd
from tqdm import tqdm
import argparse
import logging

import face_recognition
from face_recognition import face_locations
# I used mat73_to_pickle.py from https://github.com/emanuele/convert_matlab73_hdf5
from mat73_to_pickle import *

def main():

    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s][%(levelname)s] %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        stream=sys.stdout)

    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str,
                        default='KFACE/', required = True,
                        help='path to the data directory (default: KFACE/)')
    parser.add_argument('--save_feature', type=str,
                        default='kfacefeature.csv',
                        help='path to the feature file to be save (default: kfacefeature.csv)')
    parser.add_argument('--save_label', type=str,
                        default='kfacelabel.csv',
                        help='path to the label file to be save (default: kfacelabel.csv)')
    args = parser.parse_args()

    # set data paths
    data_dir = args.data_dir
    img_dir = os.path.join(data_dir, 'kface')
    attr_path = os.path.join(data_dir, 'kface_10s.mat')

    # read data
    print("reading data from {}".format(attr_path))
    logging.info("reading data from {}".format(attr_path))
    print("this process might take several minutes")
    logging.info("this process might take several minutes")
    f = h5py.File(attr_path, mode='r')
    data = recursive_dict(f)
    df_label = pd.DataFrame(data['label'].T, columns=data['AttrName'], index=data['name'])
    logging.info("Successfully changed matfile to df_label using pandas")
    # change "\\" to "/"
    df_label.index = [name.replace('\\', '/') for name in df_label.index]
    logging.info("Successfully changed \\ to / in df_label")

    # extract face features using face_recognition.face_encodings
    # take about 10 minutes on my pc
    print("extracting face features from images")
    logging.info("Start extracting face features")
    feature_vecs = []
    fnames = []
    for fname in tqdm(df_label.index):
        img_path = os.path.join(img_dir, fname)
        logging.info("{}".format(attr_path))
        # face detection
        X_img = face_recognition.load_image_file(img_path)
        X_faces_loc = face_locations(X_img)
        # if the number of faces detected in a image is not 1, ignore the image
        if len(X_faces_loc) != 1:
            continue
        # extract 128 dimensional face features
        faces_encoding = face_recognition.face_encodings(X_img, known_face_locations=X_faces_loc)[0]
        feature_vecs.append(faces_encoding)
        fnames.append(fname)

    df_feat = pd.DataFrame(feature_vecs, index=fnames)
    df_label = df_label[df_label.index.isin(df_feat.index)]
    df_feat.sort_index(inplace=True)
    df_label.sort_index(inplace=True)
    
    logging.info("Saving feature and label")
 
    df_feat.to_csv(args.save_feature)
    df_label.to_csv(args.save_label)



if __name__ == "__main__":
    main()
