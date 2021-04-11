<!--- Filename: README.md
  --- Author: Marcelo Feitoza Parisi
  --- 
  --- Description: Readme file for
  --- gcs-reporting tool.
  ---  
  --- ###########################
  --- # DISCLAIMER - IMPORTANT! #
  --- ###########################
  --- 
  --- Stuff found here was built as a
  --- Proof-Of-Concept or Study material
  --- and should not be considered
  --- production ready!
  --- 
  --- USE WITH CARE!
--->

# gcs-reporting

## Usage
This application was built to take simple reports from Google Cloud Storage Bucket.  
There are 4 main subsystems:

* storageclass - This one prints a report of bucket storage usage by storage class:  
`./gcs-reporting storageclass --help`
* size - This one prints a report on the top objects/files in storage usage on the bucket.  
`./gcs-reporting size --help`
* date - This one prints the olders files on the bucket.  
`./gcs-reporting date --help`
* name - This one prints all the objects on the bucket ordered by name.  
`./gcs-reporting name --help`

Main parameters are:
* `--bucket <bucket-name>`
* `--project <project-id>`

## Development info
This is how the tool is organized:
* gcs-reporting - Shellscript wrapper to main.py.  
  Checks if Python/Pip/Requirements are installed.
* main.py - This is where to tool is invoked.  
  Simply calls the argument parser and invokes the correct subsystem.
* lib/cmd.py - This is the argument parser.  
  Parses the command line arguments sent by the shellscript to main.py
* lib/sc.py - Usage by storageclass.  
  Gets the usage by storageclass and prints.
* lib/size.py - Top objects/files on the bucket by size.  
  Gets the list of files in the bucket and sorts by size.
* lib/date.py - Oldest objects/files on the bucket.  
  Gets the list of files in the bucket and sorts by date.
* lib/name.py - List objects/files   
  Gets the list of files in the bucket and sorts by name.
* lib/byte.py - To convert size of objects/files.  
  Got his one from stackoverflow.

To generate requirements run:  
```pip3 freeze > requirements.txt```

## Requirements
* Google Cloud Storage Python SDK  
  `sudo pip3 install --upgrade google-cloud-storage`
* gsutil  
  `sudo pip3 install gsutil`
* gcloud  
  https://cloud.google.com/sdk/docs/install
* requirements.txt  
  `sudo pip3 install -r requirements.txt`