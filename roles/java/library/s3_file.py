#!/usr/bin/env python

from boto.s3.connection import S3Connection, Key
import shlex
import json
import sys
import os.path
from ansible.module_utils.basic import *

module = AnsibleModule(
  argument_spec = dict(
    bucket = dict( required=True ),
    object = dict( required=True ),
    dest   = dict( required=True ),
    aws_access_key = dict( required=False,default=False),
    aws_secret_key = dict( required=False,default=False),
    mode = dict( required=False )
  )
)
if 'aws_access_key' in module.params and 'aws_secret_key' in module.params and module.params.get('aws_access_key') and module.params.get('aws_secret_key'):
  conn = S3Connection(module.params.get('aws_access_key'),module.params.get('aws_secret_key'))
else:
  conn = S3Connection()
bucket = conn.get_bucket(module.params.get('bucket'), validate=False)
k = bucket.new_key(module.params.get('object'))
# a file in which we can cache the etag; if etag matches, don't download
k_etag = "%s" % k.etag
etag_cache_file = "%s.etag" % module.params.get('dest')
# try to get the cached etag; if it fails, we know we need to download.
need_to_download = True
cached_etag = None
if os.path.isfile(etag_cache_file) and os.path.isfile(module.params.get('dest')):
  with open(etag_cache_file, 'r' ) as f:
    cached_etag = f.read()
  if cached_etag == k_etag:
    need_to_download = False
 
if need_to_download: 
  k.get_contents_to_filename(module.params.get('dest'))
  with open(etag_cache_file, 'w') as f:
    f.write( k_etag )
  module.exit_json(failed=False,changed=True,msg=("Redownloaded object because etag cache %s does not equal %s" % (cached_etag,k_etag)))
else:
  module.exit_json(failed=False,changed=False,msg=("Etag cache matches; file not downloaded") )
