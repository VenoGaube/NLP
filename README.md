# Machine translator

This is the repository of a Machine Translation project made for the Natural Language Processing course. It contains used python scripts, python notebooks and results of the quality of translations.

Machine translator was created with **OpenNMT-py** framework and was trained on the **Google Colab** platform.

Our general model was trained on different corpora from **OpenSubtitles 2018**, **EUparl, EMEA**, **DGT** and **ELRC**. General corpus can be accessed through the Python notebook file if you would like to train the model from scratch, but there is also a pretrained model available if you would just like to perform translations on a given file. Our own, military corpora gathered from different Slovenian military documents will also be available through the notebook as well as here on Github.

**domain_data** includes our domain corpora data division, the **helper_fuctions** were used to preprocess the data and **evaluation** consists of scripts for automatically calculating certain translation quality matrices.

## Instructions

We would recommand using the **Machine_Translator.ipynb** file in Google Colab. The file is structured in a way that will guide you through the whole process of machine translation, starting with setting up the evironment, building the vocabulary out of the corpora, training the model and finally translating texts of choice.





