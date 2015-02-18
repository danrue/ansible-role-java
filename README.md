Java
=========

This role will install different flavors of Java as specifies in the role variables.  Currently the only supported repository to download artifacts from is a specified S3 bucket.

*note*: change tests/test.yml to point to real bucket and s3 base path before running tests!

Requirements
------------

This role utilizes a local S3_file  module, and requires boto.  By default, this role will install the required package if it is missing.  You can then either use the required ENV variables, or set s3_key and s3_secret.

Role Variables
--------------
| variable | description | default | mandatory
|----------|-------------|---------|----------
| `java_version` | formatted like `<major>u<update>` | 8u21 | no
| `java_arch` | architecture type | x64 | no
| `java_install_path` | base path to install to. | /opt/java | no
| `java_type` | only 'oracle' is supported at this time | none | yes
| `java_links` | a dictionary/hash in the form of `{ relative path: destination }` Eg. `{ '.' : /opt/java/java6 }` | none | no
| `java_s3_bucket` | S3 bucket to download artifacts from | none | yes
| `java_s3_base` | base path in the s3 bucket | `/` | no
| `s3_key` | AWS S3 access key id | none | no
| `s3_secret` | AWS S3 secret access key | none | no

Dependencies
------------

No dependencies.

Example Playbook
----------------

An example playbook is included in the test directory, but here is a rundown on typical usage.

    - hosts: all
      roles:
      - { role: java, java_version: 6u45, java_arch: x64, java_install_path: /opt/java, java_type: oracle, java_links: { '.': /opt/java/java6 } }

License
-------

Apache 2.0

Author Information
------------------

Author: Ryan O'Keeffe (okeefferd@gmail.com)
