Summary: A documentation system for C and C++.
Name: doxygen
Version: 1.2.6
Release: 1
Epoch: 1
Source0: http://www.stack.nl/~dimitri/doxygen/dl/%{name}-%{version}.src.tar.gz
Group: Development/Tools
Copyright: GPL
URL: http://www.stack.nl/~dimitri/doxygen/index.html
Prefix: %{_prefix}
BuildPrereq: qt-devel >= 2.1 libstdc++-devel >= 2.96 /usr/bin/perl
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Doxygen is a documentation system for C and C++.  Doxygen can generate
an on-line class browser (in HTML) and/or a reference manual (in
LaTeX) from a set of documented source files. The documentation is
extracted directly from the sources.  Doxygen can be configured to
extract the code structure from undocumented source files.

%prep
%setup -q
export QTDIR=
. /etc/profile.d/qt.sh

# use Qt defined in $QTDIR
ln -s $QTDIR/include include
ln -s $QTDIR/lib lib

%build
export QTDIR=
. /etc/profile.d/qt.sh

./configure --prefix %{_prefix} --shared --release --with-doxywizard

# the compiler is ICEing and generating bad code at the moment,
# revert when fixed!!
#%ifarch %{ix86}
#perl -pi -e "s|-O2||" tmake/lib/linux-g++/tmake.conf
#%endif

make all docs

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}

for i in bin/*; do
    install -s -m 0755 $i ${RPM_BUILD_ROOT}%{_bindir}/`basename $i`
done

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc LANGUAGE.HOWTO README doc examples html
%{_bindir}/*

%changelog
* Wed Mar 14 2001 Jeff Johnson <jbj@redhat.com>
- update to 1.2.6

* Wed Feb 28 2001 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild

* Tue Dec 26 2000 Than Ngo <than@redhat.com>
- update to 1.2.4
- remove excludearch ia64
- bzip2 sources

* Mon Dec 11 2000 Than Ngo <than@redhat.com>
- rebuild with the fixed fileutils

* Mon Oct 30 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.2.3.

* Sun Oct  8 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.2.2.
- enable doxywizard.

* Sat Aug 19 2000 Preston Brown <pbrown@redhat.com>
- 1.2.1 is latest stable, so we upgrade before Winston is released.

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jul  4 2000 Jakub Jelinek <jakub@redhat.com>
- Rebuild with new C++

* Fri Jun 30 2000 Florian La Roche <laroche@redhat.de>
- fix QTDIR detection

* Fri Jun 09 2000 Preston Brown <pbrown@redhat.com>
- compile on x86 w/o optimization, revert when compiler fixed!!

* Wed Jun 07 2000 Preston Brown <pbrown@redhat.com>
- use newer RPM macros

* Tue Jun  6 2000 Jeff Johnson <jbj@redhat.com>
- add to distro.

* Tue May  9 2000 Tim Powers <timp@redhat.com>
- rebuilt for 7.0

* Wed Feb  2 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- recompile with current Qt (2.1.0/1.45)

* Wed Jan  5 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.0.0.
- recompile with qt-2.0.1 if available.
- relocatable package.

* Mon Nov  8 1999 Tim Powers <timp@redhat.com>
-updated to 0.49-991106

* Tue Jul 13 1999 Tim Powers <timp@redhat.com>
- updated source
- cleaned up some stuff in the spec file

* Thu Apr 22 1999 Jeff Johnson <jbj@redhat.com>
- Create Power Tools 6.0 package.
