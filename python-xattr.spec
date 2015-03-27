%define real_name xattr

Summary: Extended attributes for python
Name: python-xattr
Version: 0.7.5
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
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

%files
%{py_platsitedir}/*
%{_bindir}/xattr
