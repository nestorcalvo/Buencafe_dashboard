import boto3
import pandas as pd

class DatabaseHelper:
    """
    Helper class to access the S3 bucket and 
    """
    def __init__(self, db_name):
        self.db_name = db_name
        self.s3 = boto3.client('s3')

    def list_files(self):
        """
        List of files in bucket
        """
        my_bucket = self.s3.Bucket(self.db_name)
        for my_bucket_object in my_bucket.objects.all():
            print(my_bucket_object)

    def get_csv(self, filename):
        """
        Read a csv from the S3 and store the data in a variable
        """
        obj = self.s3.get_object(Bucket= self.db_name, Key= filename) 
        # get object and file (key) from bucket
        initial_df = pd.read_csv(obj['Body']) # 'Body' is a key word
        return initial_df