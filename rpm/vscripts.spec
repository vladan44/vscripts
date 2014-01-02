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
plfiles=(   awkc \
            ggrep \
            devetpet \
            jsonparse \
            lstr \
            myhead \
            googlaj \
            filetime \
            printbin \
            )
for f in ${plfiles[@]}
do
    install -m 755 perl/${f}.pl $RPM_BUILD_ROOT%_targetdir/perl/${f}.pl
    ln -sf perl/${f}.pl $RPM_BUILD_ROOT%_targetdir/$f
done

echo "bash commands..."
bashfiles=( grepdijara\
            grp \
            myvalgrind \
            remotegvim \
            simboli \
            spakujpromene \
            svnbc3 \
            svndiff \
            svnst \
            gitst \
            )
for f in ${bashfiles[@]}
do
    install -m 755 bash/${f} $RPM_BUILD_ROOT%_targetdir/bash/${f}
    ln -sf perl/${f} $RPM_BUILD_ROOT%_targetdir/$f
done

shfiles=(   bakrename \
            mygitdiff \
            range \
            )
for f in ${shfiles[@]}
do
    install -m 755 bash/${f}.bash $RPM_BUILD_ROOT%_targetdir/bash/${f}.bash
    ln -sf perl/${f}.bash $RPM_BUILD_ROOT%_targetdir/$f
done

install -m 755 bash/isitrunning.sh $RPM_BUILD_ROOT%_targetdir/bash/isitrunning.sh
ln -sf bash/isitrunning.sh $RPM_BUILD_ROOT%_targetdir/isitrunning

echo "python commands..."
pyfiles=(   grepy \
            grepymoje \
            recursivepie \
            )
for f in ${pyfiles[@]}
do
    install -m 755 python/${f} $RPM_BUILD_ROOT%_targetdir/python/${f}
    ln -sf python/${f} $RPM_BUILD_ROOT%_targetdir/$f
done
install -m 755 python/bcolors.py $RPM_BUILD_ROOT%_targetdir/python/bcolors.py
install -m 755 python/debug.py $RPM_BUILD_ROOT%_targetdir/python/debug.py
install -m 755 python/editdijara.py $RPM_BUILD_ROOT%_targetdir/python/editdijara.py
ln -sf python/editdijara.py $RPM_BUILD_ROOT%_targetdir/editdijara 


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
%_targetdir/perl/printbin.pl
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

