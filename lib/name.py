## Filename: name.py
 # Author: Marcelo Feitoza Parisi
 # 
 # Description: Report the objects
 # on the bucket sorted by name.
 # 
 # ###########################
 # # DISCLAIMER - IMPORTANT! #
 # ###########################
 # 
 # Stuff found here was built as a
 # Proof-Of-Concept or Study material
 # and should not be considered
 # production ready!
 # 
 # USE WITH CARE!
##
from lib import byte
from google.cloud import storage
from prettytable import PrettyTable

def exec(bucket_id, project_id, reverse_opt):

    # Google Cloud Storage Client
    client = storage.Client()
    bucket = client.bucket(bucket_id, user_project=project_id)
    blobs = bucket.list_blobs()

    # Will hold our local list of objects
    blob_list = []

    try: 
        for blob in blobs:
            # For each object we'll save name, owner, class, size and date
            this_blob = { 'name': blob.name,
                         'owner': blob.owner,
                         'class': blob.storage_class,
                         'size' : blob.size,
                         'date' : str(blob.updated).split('.')[0].split('+')[0]
                         }
            # Append object to our list
            blob_list.append(this_blob)
    except Exception as e:
        print(e)
        exit(1)

    # Sort our object list by name using our reverse_opt
    sorted_list = sorted(blob_list, key=lambda k: blob.name, reverse=reverse_opt)

    # Generating our PrettyTable
    report_table = PrettyTable()
    report_table.field_names = ["NAME", "OWNER", "CLASS", "SIZE", "DATE"]
    report_table.align["NAME"] = "l"
    report_table.align["SIZE"] = "r"
    report_table.align["DATE"] = "r"
    for blob in sorted_list:
        report_table.add_row([blob['name'], blob['owner'], blob['class'], str(byte.convert_size(blob['size'])), blob['date']])

    print(report_table)


