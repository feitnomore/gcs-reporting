## Filename: sc.py
 # Author: Marcelo Feitoza Parisi
 # 
 # Description: Report storage usage
 # by storage class on the bucket.
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

def exec(bucket_id, project_id):

    # Google Cloud Storage Client
    client = storage.Client()
    bucket = client.bucket(bucket_id, user_project=project_id)
    blobs = bucket.list_blobs()

    # This is where we'll accumulate the sizes for each storage class
    sizes = { 'standard'       : 0,
              'nearline'       : 0,
              'coldline'       : 0,
              'archive'        : 0,
              'multi_regional' : 0,
              'regional'       : 0
            }

    # This is where we'll sum the qty of objects on each storage class
    qty = { 'standard'       : 0,
            'nearline'       : 0,
            'coldline'       : 0,
            'archive'        : 0,
            'multi_regional' : 0,
            'regional'       : 0
          }

    try: 
        # Sum the size value according to storage class and count the objects on each class
        for blob in blobs:
            if blob.storage_class == "STANDARD":
                sizes['standard'] = sizes['standard'] + blob.size
                qty['standard'] = qty['standard'] + 1
            if blob.storage_class == "NEARLINE":
                sizes['nearline'] = sizes['nearline'] + blob.size
                qty['nealine'] = qty['nearline'] + 1
            if blob.storage_class == "COLDLINE":
                sizes['coldline'] = sizes['coldline'] + blob.size
                qty['coldline'] = qty['coldline'] + 1
            if blob.storage_class == "ARCHIVE":
                sizes['archive'] = sizes['archive'] + blob.size
                qty['archive'] = qty['archive'] + 1
            if blob.storage_class == "MULTI_REGIONAL":
                sizes['multi_regional'] = sizes['multi_regional'] + blob.size
                qty['multi_regional'] = qty['multi_regional'] + 1
            if blob.storage_class == "REGIONAL":
                sizes['regional'] = sizes['regional'] + blob.size
                qty['regional'] = qty['regional'] + 1
    except Exception as e:
        print(e)
        exit(1)

    # Generating our PrettyTable
    report_table = PrettyTable()
    report_table.field_names = ["STORAGECLASS", "OBJECTS", "SIZE"]
    report_table.align["STORAGECLASS"] = "l"
    report_table.align["SIZE"] = "r"
    report_table.add_row(["STANDARD",       qty['standard'],       str(byte.convert_size(sizes['standard']))])
    report_table.add_row(["NEARLINE",       qty['nearline'],       str(byte.convert_size(sizes['nearline']))])
    report_table.add_row(["COLDLINE",       qty['coldline'],       str(byte.convert_size(sizes['coldline']))])
    report_table.add_row(["ARCHIVE",        qty['archive'],        str(byte.convert_size(sizes['archive']))])
    report_table.add_row(["MULTI_REGIONAL", qty['multi_regional'], str(byte.convert_size(sizes['multi_regional']))])
    report_table.add_row(["REGIONAL",       qty['regional'],       str(byte.convert_size(sizes['regional']))])


    print(report_table)
