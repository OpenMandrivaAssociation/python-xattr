%define real_name xattr

Summary: Extended attributes for python
Name: python-xattr
Version: 0.7.8
Release: 1
License: GPL
Group: Development/Python
URL: http://pypi.python.org/pypi/xattr
Source: http://pypi.python.org/packages/source/x/xattr/xattr-%{version}.tar.gz
Provides: pyxattr = %{version}-%{release}
BuildRequires: attr-devel
BuildRequires: python-setuptools

%description
python-xattr is a C extension module for Python which implements
extended attributes manipulation. It is a wrapper on top of the
attr C library - see attr(5).

%prep
%setup -q -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
python setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

%files
%{py_puresitedir}/*
%{_bindir}/xattr


%changelog
* Sun Nov 07 2010 Funda Wang <fwang@mandriva.org> 0.6.1-3mdv2011.0
+ Revision: 594710
- rebuild
- rebuild for py 2.7

* Sun Sep 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.1-1mdv2011.0
+ Revision: 577778
- new version

* Sun Dec 27 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.0-1mdv2010.1
+ Revision: 482902
- Update to new version 0.5.0

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.4-5mdv2010.0
+ Revision: 442546
- rebuild

* Mon Dec 29 2008 Funda Wang <fwang@mandriva.org> 0.4-4mdv2009.1
+ Revision: 320913
- adjust BR

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.4-4mdv2009.0
+ Revision: 259864
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.4-3mdv2009.0
+ Revision: 247736
- rebuild

* Sat Jan 05 2008 Jérôme Soyer <saispo@mandriva.org> 0.4-1mdv2008.1
+ Revision: 145719
- New release
- Mistake

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 24 2007 Gaëtan Lehmann <glehmann@mandriva.org> 0.2.2-1mdv2008.0
+ Revision: 55049
- 0.2.2


* Wed Aug 09 2006 glehmann
+ 08/09/06 20:57:54 (55140)
use py_platsitedir

* Sun Jul 30 2006 glehmann
+ 07/30/06 10:28:03 (42708)
Import python-xattr

* Wed Feb 15 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.2.1-1mdk
- New release 0.2.1

* Wed Dec 14 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.2-1mdk
- first mandriva package

* Sun Sep 11 2005 Dag Wieers <dag@wieers.com> - 0.2-1 - +/
- Initial package. (using DAR)

