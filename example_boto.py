#!/usr/bin/python
##
# Various functions of boto for S3
# with working examples.
# bgolliher@apple.com
##
 
import boto
import boto.s3
import boto.s3.connection
from boto.s3.key import Key
 
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
 
bucket_name = 'maps001_raster01'
 
conn = boto.connect_s3(
	aws_access_key_id = AWS_ACCESS_KEY_ID,
	aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
	host = 'map001.isoblob.apple.com',
	calling_format = boto.s3.connection.OrdinaryCallingFormat(),
	)
 
# to CREATE a bucket
# bucket = conn.create_bucket(bucket_name,location=boto.s3.connection.Location.DEFAULT)
bucket = conn.get_bucket(bucket_name)
 
testfile = 'pearljam.txt'
print 'Uploading %s to Amazon S3 bucket %s.' % (testfile, bucket_name)
 
k = Key(bucket)
k.key = testfile
k.set_contents_from_filename(testfile)
 
print "\nHey that looks like it worked!  How about we list 'dem keys?"
 
bucket = conn.get_bucket(bucket_name)
alist = bucket.list()
for key in alist:
	print key.name
 
print '\nHey that looks like it worked!  How about we read back %s.' % testfile
contents = k.get_contents_as_string()
print "The key '%s/%s' contains the following. " % (k.bucket.name,k.name)
print contents
 
localfilename = 'testfile_output'
print '\nCool!  I\'ll shove that into a file called %s now.' % localfilename
k.get_contents_to_filename(localfilename)

print '\nHey that looks like it worked!  How about we delete %s, so we can clean up after ourselves.' % testfile
k.delete_key()
