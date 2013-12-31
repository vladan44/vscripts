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
%setup -q
%build
%install
install -m 755 -d $RPM_BUILD_ROOT%_targetdir
install -m 755 -d $RPM_BUILD_ROOT%_targetdir/python
install -m 755 -d $RPM_BUILD_ROOT%_targetdir/perl
install -m 755 -d $RPM_BUILD_ROOT%_targetdir/awk
install -m 755 -d $RPM_BUILD_ROOT%_targetdir/bash
install -m 755 -d $RPM_BUILD_ROOT%_targetdir/ruby
pwd
install -m 755 perl/awkc.pl $RPM_BUILD_ROOT%_targetdir/perl/awkc.pl
ln -sf perl/awkc.pl $RPM_BUILD_ROOT%_targetdir/awkc

install -m 755 perl/devetpet.pl $RPM_BUILD_ROOT%_targetdir/perl/devetpet.pl
ln -sf perl/devetpet.pl $RPM_BUILD_ROOT%_targetdir/devetpet

install -m 755 perl/ggrep.pl $RPM_BUILD_ROOT%_targetdir/perl/ggrep.pl
ln -sf perl/ggrep.pl $RPM_BUILD_ROOT%_targetdir/ggrep


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

%_targetdir/perl/awkc.pl
%_targetdir/awkc
%_targetdir/perl/devetpet.pl
%_targetdir/devetpet
%_targetdir/perl/ggrep.pl
%_targetdir/ggrep

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


