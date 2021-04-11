# gcs-reporting

## Usage
This application was built to take simple reports from Google Cloud Storage Bucket.  
Python3 and Pip3 is needed to run it.

1 - Install Google Cloud Storage Python SDK
    sudo pip3 install --upgrade google-cloud-storage

2 - Install gsutil  
    sudo pip3 install gsutil

3 - Install gcloud  
    https://cloud.google.com/sdk/docs/install

4 - Install requirements
    sudo pip3 install -r requirements.txt

5 - In case needed, change permissions
    chmod +x gcs-reporting

6 - Run the tool
    ./gcs-reporting --help