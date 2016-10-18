#!/bin/bash    
#    
#   ------------------------------------------------------- 
#    rpmbuild directory has to have the following structure
#    
#    rpmbuild
#    |
#    ├── BUILD
#    ├── BUILDROOT
#    ├── RPMS
#    │   └── noarch
#    ├── SOURCES
#    │   └── vscripts-<version>.tar.gz
#    ├── SPECS
#    │   └── vscripts.spec
#    └── SRPMS
#

dirs=(
    rpmbuild/BUILD
    rpmbuild/BUILDROOT
    rpmbuild/RPMS/noarch
    rpmbuild/SOURCES
    rpmbuild/SPECS
    rpmbuild/SRPMS
)

for dir in ${dirs[@]}
do
    echo mkdir -pv $dir
done
