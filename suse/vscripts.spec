###############################################################################
# SUSE spec file for package: vscripts
#           


%define buildroot  /home/vladan/myrpm
%define _targetdir /opt/vscripts

Summary:    Administration helper script
Name:       vscripts 
Version:    0.0
Release:    3
License:    GPL
Source:     vscripts-%{version}.tar.gz
Packager:   %packager
BuildRoot:  %buildroot 
BuildArch:  noarch
# Prefix:     %_targetdir 

%description
Description: Administration helper scripts
 bash vscripts: bakrename 
                grepdijara 
                grp 
                mygitdiff 
                myvalgrind 
                remotegvim 
                simboli 
                spakujpromene 
                svnbc3 
                svndiff 
                svnst 
                range 

 python vscripts: 
                editdijara 
                grepy 
                grepymoje 
                recursivepie
 perl vscripts: 
                googlaj 
                lstr 
                myhead
                awkc 
                ggrep

%prep
# %setup
echo ".......................................... prepping"
echo "..Building %name-%version-%release"
echo "..Building %prefix"

%build
echo ".......................................... buildintg"
mkdir -p $RPM_BUILD_ROOT%_targetdir/python 
mkdir -p $RPM_BUILD_ROOT%_targetdir/perl 
mkdir -p $RPM_BUILD_ROOT%_targetdir/awk 
mkdir -p $RPM_BUILD_ROOT%_targetdir/bash 

cp -r $RPM_BUILD_DIR/%name-%version/bash/bakrename.bash $RPM_BUILD_ROOT%_targetdir/bash/bakrename.bash
cp -r $RPM_BUILD_DIR/%name-%version/python/bakrename $RPM_BUILD_ROOT%_targetdir/python/bakrename
cp -r $RPM_BUILD_DIR/%name-%version/bakrename $RPM_BUILD_ROOT%_targetdir/bakrename

cp -r $RPM_BUILD_DIR/%name-%version/bash/grepdijara $RPM_BUILD_ROOT%_targetdir/bash/grepdijara
cp -r $RPM_BUILD_DIR/%name-%version/grepdijara $RPM_BUILD_ROOT%_targetdir/grepdijara

cp -r $RPM_BUILD_DIR/%name-%version/bash/grp $RPM_BUILD_ROOT%_targetdir/bash/grp
cp -r $RPM_BUILD_DIR/%name-%version/grp $RPM_BUILD_ROOT%_targetdir/grp

cp -r $RPM_BUILD_DIR/%name-%version/bash/mygitdiff.bash $RPM_BUILD_ROOT%_targetdir/bash/mygitdiff.bash
cp -r $RPM_BUILD_DIR/%name-%version/mygitdiff $RPM_BUILD_ROOT%_targetdir/mygitdiff

cp -r $RPM_BUILD_DIR/%name-%version/bash/myvalgrind $RPM_BUILD_ROOT%_targetdir/bash/myvalgrind
cp -r $RPM_BUILD_DIR/%name-%version/myvalgrind $RPM_BUILD_ROOT%_targetdir/myvalgrind

cp -r $RPM_BUILD_DIR/%name-%version/bash/remotegvim $RPM_BUILD_ROOT%_targetdir/bash/remotegvim
cp -r $RPM_BUILD_DIR/%name-%version/remotegvim $RPM_BUILD_ROOT%_targetdir/remotegvim

cp -r $RPM_BUILD_DIR/%name-%version/bash/simboli $RPM_BUILD_ROOT%_targetdir/bash/simboli
cp -r $RPM_BUILD_DIR/%name-%version/simboli $RPM_BUILD_ROOT%_targetdir/simboli

cp -r $RPM_BUILD_DIR/%name-%version/bash/spakujpromene $RPM_BUILD_ROOT%_targetdir/bash/spakujpromene
cp -r $RPM_BUILD_DIR/%name-%version/spakujpromene $RPM_BUILD_ROOT%_targetdir/spakujpromene

cp -r $RPM_BUILD_DIR/%name-%version/bash/svnbc3 $RPM_BUILD_ROOT%_targetdir/bash/svnbc3
cp -r $RPM_BUILD_DIR/%name-%version/svnbc3 $RPM_BUILD_ROOT%_targetdir/svnbc3

cp -r $RPM_BUILD_DIR/%name-%version/bash/svndiff $RPM_BUILD_ROOT%_targetdir/bash/svndiff
cp -r $RPM_BUILD_DIR/%name-%version/svndiff $RPM_BUILD_ROOT%_targetdir/svndiff

cp -r $RPM_BUILD_DIR/%name-%version/bash/svnst $RPM_BUILD_ROOT%_targetdir/bash/svnst
cp -r $RPM_BUILD_DIR/%name-%version/svnst $RPM_BUILD_ROOT%_targetdir/svnst

cp -r $RPM_BUILD_DIR/%name-%version/bash/range.bash $RPM_BUILD_ROOT%_targetdir/bash/range.bash
cp -r $RPM_BUILD_DIR/%name-%version/range $RPM_BUILD_ROOT%_targetdir/range

cp -r $RPM_BUILD_DIR/%name-%version/bash/gitst $RPM_BUILD_ROOT%_targetdir/bash/gitst
cp -r $RPM_BUILD_DIR/%name-%version/gitst $RPM_BUILD_ROOT%_targetdir/gitst

cp -r $RPM_BUILD_DIR/%name-%version/bash/isitrunning.sh $RPM_BUILD_ROOT%_targetdir/bash/isitrunning.sh
cp -r $RPM_BUILD_DIR/%name-%version/isitrunning $RPM_BUILD_ROOT%_targetdir/isitrunning

cp -r $RPM_BUILD_DIR/%name-%version/python/bcolors.py $RPM_BUILD_ROOT%_targetdir/python/bcolors.py
cp -r $RPM_BUILD_DIR/%name-%version/python/debug.py $RPM_BUILD_ROOT%_targetdir/python/debug.py

cp -r $RPM_BUILD_DIR/%name-%version/python/editdijara.py $RPM_BUILD_ROOT%_targetdir/python/editdijara.py
cp -r $RPM_BUILD_DIR/%name-%version/editdijara $RPM_BUILD_ROOT%_targetdir/editdijara

cp -r $RPM_BUILD_DIR/%name-%version/python/grepy $RPM_BUILD_ROOT%_targetdir/python/grepy
cp -r $RPM_BUILD_DIR/%name-%version/grepy $RPM_BUILD_ROOT%_targetdir/grepy

cp -r $RPM_BUILD_DIR/%name-%version/python/grepymoje $RPM_BUILD_ROOT%_targetdir/python/grepymoje
cp -r $RPM_BUILD_DIR/%name-%version/grepymoje $RPM_BUILD_ROOT%_targetdir/grepymoje

cp -r $RPM_BUILD_DIR/%name-%version/python/recursivepie $RPM_BUILD_ROOT%_targetdir/python/recursivepie
cp -r $RPM_BUILD_DIR/%name-%version/recursivepie $RPM_BUILD_ROOT%_targetdir/recursivepie

cp -r $RPM_BUILD_DIR/%name-%version/perl/googlaj.pl $RPM_BUILD_ROOT%_targetdir/perl/googlaj.pl
cp -r $RPM_BUILD_DIR/%name-%version/googlaj $RPM_BUILD_ROOT%_targetdir/googlaj

cp -r $RPM_BUILD_DIR/%name-%version/perl/lstr.pl $RPM_BUILD_ROOT%_targetdir/perl/lstr.pl
cp -r $RPM_BUILD_DIR/%name-%version/lstr $RPM_BUILD_ROOT%_targetdir/lstr

cp -r $RPM_BUILD_DIR/%name-%version/perl/myhead.pl $RPM_BUILD_ROOT%_targetdir/perl/myhead.pl
cp -r $RPM_BUILD_DIR/%name-%version/myhead $RPM_BUILD_ROOT%_targetdir/myhead


cp -r $RPM_BUILD_DIR/%name-%version/perl/awkc.pl $RPM_BUILD_ROOT%_targetdir/perl/awkc.pl
cp -r $RPM_BUILD_DIR/%name-%version/awkc $RPM_BUILD_ROOT%_targetdir/awkc

cp -r $RPM_BUILD_DIR/%name-%version/perl/ggrep.pl $RPM_BUILD_ROOT%_targetdir/perl/ggrep.pl
cp -r $RPM_BUILD_DIR/%name-%version/ggrep $RPM_BUILD_ROOT%_targetdir/ggrep

cp -r $RPM_BUILD_DIR/%name-%version/perl/devetpet.pl $RPM_BUILD_ROOT%_targetdir/perl/devetpet.pl
cp -r $RPM_BUILD_DIR/%name-%version/devetpet $RPM_BUILD_ROOT%_targetdir/devetpet

cp -r $RPM_BUILD_DIR/%name-%version/perl/jsonparse.pl $RPM_BUILD_ROOT%_targetdir/perl/jsonparse.pl
cp -r $RPM_BUILD_DIR/%name-%version/jsonparse $RPM_BUILD_ROOT%_targetdir/jsonparse



%install
echo ".......................................... installing"
# install -m 755 -d $RPM_BUILD_ROOT/python %_targetdir
# install -m 755 -d $RPM_BUILD_ROOT/perl %_targetdir
# install -m 755 -d $RPM_BUILD_ROOT/bash %_targetdir
# install -m 755 -d $RPM_BUILD_ROOT/awk %_targetdir


%clean 
echo ".......................................... cleaning"
rm -rf  $RPM_BUILD_ROOT

%post
# echo "post installation  nothing..."

%files
%dir %_targetdir/python
%dir %_targetdir/perl
%dir %_targetdir/awk
%dir %_targetdir/bash

%_targetdir/bakrename
%_targetdir/python/bakrename
%_targetdir/bash/bakrename.bash

%_targetdir/grepdijara
%_targetdir/bash/grepdijara

%_targetdir/bash/grp
%_targetdir/grp

%_targetdir/bash/mygitdiff.bash
%_targetdir/mygitdiff

%_targetdir/myvalgrind
%_targetdir/bash/myvalgrind

%_targetdir/remotegvim
%_targetdir/bash/remotegvim

%_targetdir/bash/simboli
%_targetdir/simboli

%_targetdir/bash/spakujpromene
%_targetdir/spakujpromene

%_targetdir/bash/svnbc3
%_targetdir/svnbc3

%_targetdir/bash/svndiff
%_targetdir/svndiff

%_targetdir/bash/svnst
%_targetdir/svnst

%_targetdir/bash/range.bash
%_targetdir/range

%_targetdir/bash/gitst
%_targetdir/gitst

%_targetdir/bash/isitrunning.sh
%_targetdir/isitrunning

%_targetdir/python/bcolors.py
%_targetdir/python/debug.py

%_targetdir/python/editdijara.py
%_targetdir/editdijara

%_targetdir/python/grepy
%_targetdir/grepy

%_targetdir/python/grepymoje
%_targetdir/grepymoje

%_targetdir/python/recursivepie
%_targetdir/recursivepie

%_targetdir/perl/googlaj.pl
%_targetdir/googlaj

%_targetdir/perl/lstr.pl
%_targetdir/lstr

%_targetdir/perl/myhead.pl
%_targetdir/myhead

%_targetdir/perl/awkc.pl
%_targetdir/awkc

%_targetdir/perl/ggrep.pl
%_targetdir/ggrep

%_targetdir/perl/devetpet.pl
%_targetdir/devetpet

%_targetdir/perl/jsonparse.pl
%_targetdir/jsonparse

# /bash/gvimmoje
# /bash/home_backup.bash
# /bash/home_backup.old.bash
# /bash/kakojedisk.bash
# /bash/moje
# /bash/mydijara.bash
# /bash/perlmoje
# /bash/setup_scratchbox_vdso.bash
# /bash/start_xephyr.bash
# /bash/z_raspakuj.bash
# /configure
# /debian/changelog
# /debian/compat
# /debian/control
# /debian/copyright
# /debian/dirs
# /debian/docs
# /debian/files
# /debian/rules
# /debian/substvars
# /debian/vscripts.substvars
# /pera
# /perl/allFiles.pl
# /perl/bakrename.pl
# /perl/color.pl
# /perl/fileTimestamp.pl
# /perl/getopt.pl
# /perl/grepim.pl
# /perl/newestFile.pl
# /perl/perlmoje
# /perl/printenv
# /perl/sorting/simplesort.pl
# /perl/t/parse_excel.pl
# /perl/text_files.pl
# /perl/try.pl
# /perl/unix2win.pl
# /perl/widechars.pl
# /python/bakrename
# /python/bst.py
# /python/cline
# /python/dijara.py
# /python/gerp
# /python/gnuoptions.py
# /python/home_backup
# /python/is_it_cpp.py
# /python/json_parse.py
# /python/lowerthecase
# /python/lssize.py
# /python/nfilename.py
# /python/options
# /python/pbar_test.py
# /python/plf.py
# /python/progressbar.py
# /python/subshell.py
# /python/vregex.py
# /python/who_is_newest.py
# /README


