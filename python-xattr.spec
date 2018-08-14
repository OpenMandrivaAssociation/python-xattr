%define real_name xattr
# we don't want to provide private python extension libs
%define _exclude_files_from_autoprov %{python2_sitearch}/.*\\.so\\|%{python3_sitearch}/.*\\.so

Summary:	Extended attributes for python
Name:		python-xattr
Version:	0.9.6
Release:	1
License:	GPL
Group:		Development/Python
URL:		http://pypi.python.org/pypi/xattr
Source0:	https://github.com/xattr/xattr/archive/%{real_name}-%{version}.tar.gz
Provides:	pyxattr = %{version}-%{release}
BuildRequires:	attr-devel
BuildRequires:	pkgconfig(libffi)
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
