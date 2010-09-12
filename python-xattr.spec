%define real_name xattr

Summary: Extended attributes for python
Name: python-xattr
Version: 0.6.1
Release: %mkrel 1
License: GPL
Group: Development/Python
URL: http://pypi.python.org/pypi/xattr
Source: http://pypi.python.org/packages/source/x/xattr/xattr-%{version}.tar.gz
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
%setup -q -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{py_platsitedir}/*
%{_bindir}/xattr
