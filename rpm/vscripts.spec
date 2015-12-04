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
                dijara 
                recursivepie

%prep
%setup -q
%build
%install
install -m 755 -d $RPM_BUILD_ROOT%_targetdir
dirs=(      python \
            perl \
            awk \
            bash \
            ruby \
            )
for f in ${dirs[@]}
do
    install -m 755 -d $RPM_BUILD_ROOT%_targetdir/$f
done

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
            bakrename \
            mygitdiff \
            range \
            isitrunning \
            )
for f in ${bashfiles[@]}
do
    install -m 755 bash/${f}.bash $RPM_BUILD_ROOT%_targetdir/bash/${f}.bash
    ln -sf bash/${f}.bash $RPM_BUILD_ROOT%_targetdir/$f
done

echo "python commands..."
pyfiles=(   editdijara \
            grepy \
            grepymoje \
            dijara \
            recursivepie \
            )
for f in ${pyfiles[@]}
do
    install -m 755 python/${f}.py $RPM_BUILD_ROOT%_targetdir/python/${f}.py
    ln -sf python/${f}.py $RPM_BUILD_ROOT%_targetdir/$f
done
install -m 755 python/bcolors.py $RPM_BUILD_ROOT%_targetdir/python/bcolors.py
install -m 755 python/debug.py $RPM_BUILD_ROOT%_targetdir/python/debug.py
install -m 755 python/nfilename.py $RPM_BUILD_ROOT%_targetdir/python/nfilename.py


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

%_targetdir/bash/grepdijara.bash
%_targetdir/grepdijara

%_targetdir/bash/grp.bash
%_targetdir/grp

%_targetdir/bash/mygitdiff.bash
%_targetdir/mygitdiff

%_targetdir/bash/myvalgrind.bash
%_targetdir/myvalgrind

%_targetdir/bash/remotegvim.bash
%_targetdir/remotegvim

%_targetdir/bash/simboli.bash
%_targetdir/simboli

%_targetdir/bash/spakujpromene.bash
%_targetdir/spakujpromene

%_targetdir/bash/svnbc3.bash
%_targetdir/svnbc3

%_targetdir/bash/svndiff.bash
%_targetdir/svndiff

%_targetdir/bash/svnst.bash
%_targetdir/svnst

%_targetdir/bash/range.bash
%_targetdir/range

%_targetdir/bash/gitst.bash
%_targetdir/gitst

%_targetdir/bash/isitrunning.bash
%_targetdir/isitrunning

# python
%_targetdir/python/bcolors.py
%_targetdir/python/debug.py
%_targetdir/python/nfilename.py

%_targetdir/python/editdijara.py
%_targetdir/editdijara

%_targetdir/python/grepy.py
%_targetdir/grepy

%_targetdir/python/grepymoje.py
%_targetdir/grepymoje

%_targetdir/python/dijara.py
%_targetdir/dijara

%_targetdir/python/recursivepie.py
%_targetdir/recursivepie

