
# Phishing-Website-Kavach-ML

This project has been created for the G20 hackathon. 

This is the machine learning component of the Phishing Website Detector Chrome Extension. It uses Gradient Boosting algorithm to classify URLs as either safe or potentially malicious.




## Table of Contents

    1. Overview
    2. Dataset
    3. Feature Extraction
    4. Model Training
    5. Model Evaluation

### Overview-
#
The Gradient Boosting algorithm is a popular machine learning algorithm used for classification tasks. It builds an ensemble of decision trees, where each subsequent tree is trained to correct the errors of the previous tree. This process continues until a pre-defined stopping criteria is met. In this project, we used Gradient Boosting algorithm to classify URLs as either safe or potentially malicious. The model was trained on a dataset of URLs, where each URL was labeled as either safe or phishing.

### Dataset- 
#
The dataset is borrowed from Kaggle, https://www.kaggle.com/eswarchandt/phishing-website-detector .

A collection of website URLs for 11000+ websites. Each sample has 30 website parameters and a class label identifying it as a phishing website or not (1 or -1).
The overview of this dataset is, it has 11054 samples with 32 features. Download the dataset from the link provided.

### Feature Extraction- 
#
To extract features from the URLs, we used the following techniques:

    1. Using the IP Address
    2. Long URL to Hide the Suspicious Part
    3. Using URL Shortening Services “TinyURL”
    4. URL’s having “@” Symbol
    5. URL’s having “@” Symbol
    6. Adding Prefix or Suffix Separated by (-) to the Domain
    7. Sub Domain and Multi Sub Domains
    8. HTTPS (Hyper Text Transfer Protocol with Secure Sockets Layer) 
    9. Domain Registration Length
    10. Favicon
    11. Using Non-Standard Port 
    12. The Existence of “HTTPS” Token in the Domain Part of the URL
    13. Request URL
    14. Links in <Meta>, <Script> and <Link> tags
    15. Website Forwarding
    16. Using Pop-up Window

    and many more which can be found using the reseach paper in the same repository "Phishing Websites Features.docx"

### Model Training-

The Gradient Boosting model was trained using the Scikit-learn library in Python. We used a train-test split of 80-20, where 80% of the dataset was used for training and 20% was used for testing. The hyperparameters of the model were tuned using grid search with 5-fold cross-validation. The final model achieved an accuracy of 98.9% on the test set.

### Model Evaluation
To evaluate the performance of the model, we used the following metrics:

    1. Accuracy: The proportion of correctly classified URLs.
    2. Precision: The proportion of URLs classified as phishing that are actually phishing.
    3. Recall: The proportion of phishing URLs that are correctly classified as phishing.

The model achieved the following performance metrics on the test set:

    Accuracy: 97.4%
    Precision: 98.6%
    Recall: 99.4%
## Installation

Downlaod the Github repo. 

Then copy the below command in the terminal and run to install the requirements for the project.
```bash
  !pip install -r requirements.txt 
```
After installing the requirements run 
```bash
   python app.py
```


## Images

    
    ![raksh](https://user-images.githubusercontent.com/96487546/229447038-5725e5a0-eee2-416c-ba49-39bcadb53b53.jpg)
    
    
    ![flask api js css](https://user-images.githubusercontent.com/96487546/229447132-6e492b2d-d69e-43bc-8be2-c5b1b2ed743a.jpg)   
    
    
    ![bbce4c45-3292-4361-959c-5028e3f8d8d0](https://user-images.githubusercontent.com/96487546/229447203-f2c2e019-5fac-4aff-8874-bba1639e6ae8.jpg)
    
    
    ![extension](https://user-images.githubusercontent.com/96487546/229447247-286e3da6-847e-475d-861d-7ba433e196f9.jpg)
