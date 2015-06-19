#!/bin/sh
SOURCE_FILE=jumpserver.zip
SPEC_FILE=jumpserver.spec
cd
rm -rf $SOURCE_FILE
wget "https://github.com/kkpbbb/jumpserver/archive/master.zip" -O $SOURCE_FILE
/bin/cp -f $SOURCE_FILE ~/rpmbuild/SOURCES/
sudo yum-builddep -y ~/rpmbuild/SPECS/$SPEC_FILE
rpmbuild -bb ~/rpmbuild/SPECS/$SPEC_FILE 
