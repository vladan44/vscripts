# VSCRIPTS

## Debian

### Build with:

```bash
$ dpkg-buildpackage -uc -us
```

  for skipping signing package.

### Install with: 

```bash
$ sudo dpkg --install vscripts-<version>.deb
```

### Uninstall with: 
```bash
$ sudo dpkg --remove vscripts-version
```


## Suse/RedHat/Fedora/CentOS

### Build with command in rpmbuild directory: 
    
```bash
 $ rpmbuild -v -ba SPECS/vscripts.spec  
```
    
### Install with: 

```bash
$ sudo rpm -Uvh vscripts-<version>.rpm
```

### Uninstall with:
```bash
$ sudo rpm -qa | grep -i vscripts
$ sudo rpm -e vscripts-<version>.noarch
```

### rpmbuild directory has to have the following structure
    
```
    rpmbuild
    |
    ├── BUILD
    ├── BUILDROOT
    ├── RPMS
    │   └── noarch
    ├── SOURCES
    │   └── vscripts-<version>.tar.gz
    ├── SPECS
    │   └── vscripts.spec
    └── SRPMS
```

