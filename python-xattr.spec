%define real_name xattr

Summary:	Extended attributes for python
Name:		python-xattr
Version:	0.8.0
Release:	2
License:	GPL
Group:		Development/Python
URL:		http://pypi.python.org/pypi/xattr
Source:		https://pypi.python.org/packages/34/17/91e70a1bcd2f0cf82824b744a63234431f5a47ea844f67076ce48166cdde/xattr-%{version}.tar.gz
Provides:	pyxattr = %{version}-%{release}
BuildRequires:	attr-devel
BuildRequires:	python-cffi
BuildRequires:	python2-cffi
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)

%description
python-xattr is a C extension module for Python which implements
extended attributes manipulation. It is a wrapper on top of the
attr C library - see attr(5).

%package -n	python2-%{real_name}
Summary:	Extended attributes for python

%description -n python2-%{real_name}
This package includes Python 2 bindings for %{name}.

%prep
%setup -q -n %{real_name}-%{version}
cp -a . %py2dir
cp -a . %py3dir

%build
pushd %py3dir
CFLAGS="%{optflags}" %{__python} setup.py build
popd

pushd %py2dir
CFLAGS="%{optflags}" %{__python2} setup.py build
popd


%install
# python2
pushd %py2dir
%{__python2} setup.py install --root="%{buildroot}" --prefix="%{_prefix}" --install-purelib=%{python2_sitearch}
mv %{buildroot}%{_bindir}/xattr %{buildroot}%{_bindir}/xattr2
popd

# python3
pushd %py3dir
%{__python} setup.py install --root="%{buildroot}" --prefix="%{_prefix}" --install-purelib=%{python_sitearch}
popd


%files
%{py_platsitedir}/*
%{_bindir}/xattr

%files -n python2-%{real_name}
%{py2_platsitedir}/
%{_bindir}/xattr2
