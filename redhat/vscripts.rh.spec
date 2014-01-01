###############################################################################
# REDHAT spec file for package: vscripts
#           

Name:       vscripts 
Version:    0.0
Release:    3
Summary:    Administration helper script
Source0:    vscripts-%{version}.%{release}.tar.gz
License:    GPL
BuildRoot:  %{_tmppath}/%{name}-buildroot
BuildArch:  noarch

%define _targetdir /usr/local/bin

%description
Description: Administration helper scripts
 perl vscripts: 
                awkc
                devetpet
                ggrep
                googlaj
                lstr
                myhead
                jsonparse
                printbin
                filetime

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
                gitst
                isitrunning

 python vscripts: 
                editdijara 
                grepy 
                grepymoje 
                recursivepie

%prep
%setup -q
%build
%install
install -m 755 -d $RPM_BUILD_ROOT%_targetdir
install -m 755 -d $RPM_BUILD_ROOT%_targetdir/python
install -m 755 -d $RPM_BUILD_ROOT%_targetdir/perl
install -m 755 -d $RPM_BUILD_ROOT%_targetdir/awk
install -m 755 -d $RPM_BUILD_ROOT%_targetdir/bash
install -m 755 -d $RPM_BUILD_ROOT%_targetdir/ruby

echo "perl commands..."
install -m 755 perl/awkc.pl $RPM_BUILD_ROOT%_targetdir/perl/awkc.pl
ln -sf perl/awkc.pl $RPM_BUILD_ROOT%_targetdir/awkc

install -m 755 perl/devetpet.pl $RPM_BUILD_ROOT%_targetdir/perl/devetpet.pl
ln -sf perl/devetpet.pl $RPM_BUILD_ROOT%_targetdir/devetpet

install -m 755 perl/ggrep.pl $RPM_BUILD_ROOT%_targetdir/perl/ggrep.pl
ln -sf perl/ggrep.pl $RPM_BUILD_ROOT%_targetdir/ggrep

install -m 755 perl/googlaj $RPM_BUILD_ROOT%_targetdir/perl/googlaj
ln -sf perl/googlaj $RPM_BUILD_ROOT%_targetdir/googlaj

install -m 755 perl/jsonparse.pl $RPM_BUILD_ROOT%_targetdir/perl/jsonparse.pl
ln -sf perl/jsonparse.pl $RPM_BUILD_ROOT%_targetdir/jsonparse

install -m 755 perl/lstr.pl $RPM_BUILD_ROOT%_targetdir/perl/lstr.pl
ln -sf perl/lstr.pl $RPM_BUILD_ROOT%_targetdir/lstr

install -m 755 perl/myhead.pl $RPM_BUILD_ROOT%_targetdir/perl/myhead.pl
ln -sf perl/myhead.pl $RPM_BUILD_ROOT%_targetdir/myhead

install -m 755 perl/filetime.pl $RPM_BUILD_ROOT%_targetdir/perl/filetime.pl
ln -sf perl/filetime.pl $RPM_BUILD_ROOT%_targetdir/filetime

install -m 755 perl/printbin.pm $RPM_BUILD_ROOT%_targetdir/perl/printbin.pm
ln -sf perl/printbin.pm $RPM_BUILD_ROOT%_targetdir/printbin

echo "bash commands..."
install -m 755 bash/bakrename.bash $RPM_BUILD_ROOT%_targetdir/bash/bakrename.bash
ln -sf bash/bakrename.bash $RPM_BUILD_ROOT%_targetdir/bakrename

install -m 755 bash/grepdijara $RPM_BUILD_ROOT%_targetdir/bash/grepdijara
ln -sf bash/grepdijara $RPM_BUILD_ROOT%_targetdir/grepdijara

install -m 755 bash/grp $RPM_BUILD_ROOT%_targetdir/bash/grp
ln -sf bash/grp $RPM_BUILD_ROOT%_targetdir/grp

install -m 755 bash/mygitdiff.bash $RPM_BUILD_ROOT%_targetdir/bash/mygitdiff.bash
ln -sf bash/mygitdiff.bash $RPM_BUILD_ROOT%_targetdir/mygitdiff

install -m 755 bash/myvalgrind $RPM_BUILD_ROOT%_targetdir/bash/myvalgrind
ln -sf bash/myvalgrind $RPM_BUILD_ROOT%_targetdir/myvalgrind

install -m 755 bash/remotegvim $RPM_BUILD_ROOT%_targetdir/bash/remotegvim
ln -sf bash/remotegvim $RPM_BUILD_ROOT%_targetdir/remotegvim

install -m 755 bash/simboli $RPM_BUILD_ROOT%_targetdir/bash/simboli
ln -sf bash/simboli $RPM_BUILD_ROOT%_targetdir/simboli

install -m 755 bash/spakujpromene $RPM_BUILD_ROOT%_targetdir/bash/spakujpromene
ln -sf bash/spakujpromene $RPM_BUILD_ROOT%_targetdir/spakujpromene

install -m 755 bash/svnbc3 $RPM_BUILD_ROOT%_targetdir/bash/svnbc3
ln -sf bash/svnbc3 $RPM_BUILD_ROOT%_targetdir/svnbc3

install -m 755 bash/svndiff $RPM_BUILD_ROOT%_targetdir/bash/svndiff
ln -sf bash/svndiff $RPM_BUILD_ROOT%_targetdir/svndiff

install -m 755 bash/svnst $RPM_BUILD_ROOT%_targetdir/bash/svnst
ln -sf bash/svnst $RPM_BUILD_ROOT%_targetdir/svnst

install -m 755 bash/gitst $RPM_BUILD_ROOT%_targetdir/bash/gitst
ln -sf bash/gitst $RPM_BUILD_ROOT%_targetdir/gitst

install -m 755 bash/range.bash $RPM_BUILD_ROOT%_targetdir/bash/range.bash
ln -sf bash/range.bash $RPM_BUILD_ROOT%_targetdir/range

install -m 755 bash/isitrunning.sh $RPM_BUILD_ROOT%_targetdir/bash/isitrunning.sh
ln -sf bash/isitrunning.sh $RPM_BUILD_ROOT%_targetdir/isitrunning

echo "python commands..."
install -m 755 python/editdijara.py $RPM_BUILD_ROOT%_targetdir/python/editdijara.py
ln -sf python/editdijara.py $RPM_BUILD_ROOT%_targetdir/editdijara 

install -m 755 python/grepy.py $RPM_BUILD_ROOT%_targetdir/python/grepy.py
ln -sf python/grepy.py $RPM_BUILD_ROOT%_targetdir/grepy 

install -m 755 python/grepymoje.py $RPM_BUILD_ROOT%_targetdir/python/grepymoje.py
ln -sf python/grepymoje.py $RPM_BUILD_ROOT%_targetdir/grepymoje 

install -m 755 python/recursivepie.py $RPM_BUILD_ROOT%_targetdir/python/recursivepie.py
ln -sf python/recursivepie.py $RPM_BUILD_ROOT%_targetdir/recursivepie 

install -m 755 python/bcolors.py $RPM_BUILD_ROOT%_targetdir/python/bcolors.py
install -m 755 python/debug.py $RPM_BUILD_ROOT%_targetdir/python/debug.py


%clean 
echo ".......................................... cleaning"
rm -rf  $RPM_BUILD_ROOT

%post
echo "post installation  nothing..."

%files
%dir %_targetdir/python
%dir %_targetdir/perl
%dir %_targetdir/awk
%dir %_targetdir/bash
%dir %_targetdir/ruby

# perl
%_targetdir/perl/awkc.pl
%_targetdir/awkc
%_targetdir/perl/devetpet.pl
%_targetdir/devetpet
%_targetdir/perl/ggrep.pl
%_targetdir/ggrep
%_targetdir/perl/googlaj.pl
%_targetdir/googlaj
%_targetdir/perl/lstr.pl
%_targetdir/lstr
%_targetdir/perl/myhead.pl
%_targetdir/myhead
%_targetdir/perl/jsonparse.pl
%_targetdir/jsonparse
%_targetdir/perl/printbin.pm
%_targetdir/printbin
%_targetdir/perl/filetime.pl
%_targetdir/filetime

#bash
%_targetdir/bash/bakrename.bash
%_targetdir/bakrename

%_targetdir/bash/grepdijara
%_targetdir/grepdijara

%_targetdir/bash/grp
%_targetdir/grp

%_targetdir/bash/mygitdiff.bash
%_targetdir/mygitdiff

%_targetdir/bash/myvalgrind
%_targetdir/myvalgrind

%_targetdir/bash/remotegvim
%_targetdir/remotegvim

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

# python
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

