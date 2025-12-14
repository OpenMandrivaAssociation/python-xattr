%global debug_package %{nil}
%define module xattr
# we don't want to provide private python extension libs
%define _exclude_files_from_autoprov %{python_sitearch}/.*\\.so\\

Summary:	Extended attributes for python
Name:		python-xattr
Version:	1.3.0
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.python.org/pypi/xattr
Source0:	https://github.com/xattr/xattr/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libattr)
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(python)
BuildRequires:	python-pkg-resources
BuildRequires:	python%{pyver}dist(cffi)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

Provides:	pyxattr = %{version}-%{release}

%description
python-xattr is a C extension  for Python which implements
extended attributes manipulation. It is a wrapper on top of the
attr C library - see attr(5).

%prep
%autosetup -n %{module}-%{version}

%build
export CFLAGS="%{optflags}"
%py_build

%install
%py_install

%files
%doc README.rst
%license LICENSE.txt
%{_bindir}/%{module}
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info

