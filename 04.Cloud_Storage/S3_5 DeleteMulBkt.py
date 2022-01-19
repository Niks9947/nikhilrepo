def deleteBucketObjects(bktName):
    import boto3

    AWS_REGION="us-west-1"
    S3Service=boto3.resource("s3",region_name=AWS_REGION)

    S3Service.Bucket(bktName).objects.delete()
    print("Delete Bucket: ",bktName)

buckets=["bkt-19jannikhil","bkt0358nikhil","bkt0525nikhilml1"]
for bin in buckets:
    deleteBucketObjects(bn)
