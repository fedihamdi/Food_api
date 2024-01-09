import csv
import boto3

s3 = boto3.client(
    's3',
    aws_access_key_id='AKIAQU5IYEAQ5XY5Q55Q',
    aws_secret_access_key='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',
    region_name='eu-west-3'
) #1

obj = s3.get_object(Bucket='test-script-hetic', Key='transactions.csv') #2
data = obj['Body'].read().decode('utf-8').splitlines() #3
records = csv.reader(data) #4
headers = next(records) #5
print('headers: %s' % (headers)) 
for eachRecord in records: #6
    print(eachRecord)