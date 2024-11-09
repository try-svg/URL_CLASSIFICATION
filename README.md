
# URL Classifier using NLP and Machine Learning


## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Local Device Installation](#local-device-installation)
- [Training Data Collection](#training-data-collection)
- [Data Modeling and Model Architecture](#data-modeling-and-model-architecture)
- [Model Performance](#model-performance)

## Overview

The URL Classifier is a powerful machine learning application designed to classify URLs as safe or malicious. In today's cybersecurity landscape, identifying potentially harmful URLs is crucial in mitigating cyber threats and phishing attacks. This project leverages both Natural Language Processing (NLP) and lexical features to create URL classifier.


## Usage

To utilize this project, you have two options:

 
1. Run the project locally using the installation steps provided below.

Once you have access, follow these steps:

1. Input the URL you want to classify.
2. The classifier will predict whether the URL is safe or malicious.

## Local Device Installation
### REQUIREMENTS
To use this project effectively, ensure you have the following prerequisites:

- Python 3.8 or higher
- numpy 1.23.5
- pandas 1.5.3
- scikit_learn 1.2.2
- tensorflow 2.12.0
- nltk 3.8.1

### Installation
To set up this project, follow these steps:

1. Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/try-svg/URL_Classifier
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On Linux/MacOS:
     ```bash
     source env/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Training Data Collection

The data for this project was meticulously collected from various sources:

**Used for Training:**

- [Malicious_phish Kaggle Dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)
- [URLhause Phishing Links](https://urlhaus.abuse.ch/)
- [Moz Top 500 Domains](https://moz.com/top-brands#:~:text=Learn%20about%20Moz%E2%80%99s%20newest%20metric%2C%20Brand%20Authority%20,%20%2093%20%2036%20more%20rows%20)
- [Top 1000 Domains from Tranco](https://tranco-list.eu/)
- [Top 1000 Domains from Majestic Million](https://majestic.com/reports/majestic-million)
- [Top 1000 Domains from Cisco Umbrella](https://s3-us-west-1.amazonaws.com/umbrella-static/index.html)
- [Top 1000 Domains from DomCop](https://www.domcop.com/top-10-million-domains)

**Used for Testing:**

- [Phishing_Site_URLs_Kaggle Dataset](https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls)

For comprehensive insights into data processing, please refer to the "Data Processing Notebook."

## Data Modeling and Model Architecture

Our URL Classifier project employs a two-pronged approach to URL classification:

1. **NLP-based Model**: This model harnesses the power of N-Gram techniques to identify patterns in URLs. Specifically, it uses 3-Gram (Character-Gram) vectorization. The N-Gram model is adept at recognizing subtle patterns in URLs often associated with malicious intent, such as direct IP addresses or keywords like "pay," "offer," "OTP," and more.

2. **Lexical Features Model**: This model is based on a set of 18 lexical features associated with URLs. These features include whether the URL has an IP address, the presence of "http" or "https," URL length, the count of dots (.), the count of "www," and more. These features contribute to the model's ability to differentiate between safe and malicious URLs.

The features used for the lexical features method are:

- having_ip_address: Whether the URL includes an IP address or not
- abnormal_url: Whether the URL is in proper formatting or not
- count_dot: The number of dots (.) in the URL
- count_www: The number of "www" in the URL
- count_atrate: The number of "@" in the URL
- no_of_dir: The number of directories in the URL
- no_of_embed: The number of "/" in the URL
- count_https: The number of "https" in the URL
- count_http: The number of "http" in the URL
- count_percent: The number of "%" in the URL
- count_ques: The number of "?" in the URL
- count_hyphen: The number of "-" in the URL
- count_equal: The number of "=" in the URL
- Length of URL
- Hostname Length
- Count of Digits
- Count of Alpha-Numerical Characters
- Length of First Directory

The two models are merged as a TensorFlow model, which takes both inputs and outputs a final prediction based on a weighted average of the two scores.

The model performance is evaluated using accuracy, precision, recall, and F1-score metrics.<br>
For more information, see the modules in Utilities and the [URL Classification Paper](https://ieeexplore.ieee.org/document/10181514).

## Model Performance

The performance of our machine learning model is impressive:

- **Testing Data Accuracy**: 98.4%
- **Unseen Dataset Accuracy**: 71.1%

These results underscore the model's ability to effectively classify URLs, which is critical for cybersecurity. For a comprehensive understanding of how the model is trained and validated, refer to the "Model Training Notebook."





