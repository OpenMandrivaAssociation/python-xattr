%define real_name pyxattr
%define short_name xattr

Summary: Extended attributes for python
Name: python-xattr
Version: 0.4
Release: %mkrel 5
License: GPL
Group: Development/Python
URL: http://pyxattr.sourceforge.net/
Source: http://kent.dl.sourceforge.net/sourceforge/%{real_name}/%{real_name}-%{version}.tar.gz
Provides: pyxattr = %{version}-%{release}
%py_requires -d
BuildRequires: libattr-devel
BuildRequires: python-setuptools
BuildRoot: %{_tmppath}/%{name}--%{version}-%{release}-root

%description
python-xattr is a C extension module for Python which implements
extended attributes manipulation. It is a wrapper on top of the
attr C library - see attr(5).

%prep
%setup -qn %{short_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

# move doc at the right place
# mv %{buildroot}/%{_docdir}/%{real_name}-%{version}/ %{buildroot}/%{_docdir}/%{name}-%{version}/


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/xattr
%{py_platsitedir}/*
