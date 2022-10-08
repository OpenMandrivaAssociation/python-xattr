%global debug_package %{nil}
%define real_name xattr
# we don't want to provide private python extension libs
%define _exclude_files_from_autoprov %{python_sitearch}/.*\\.so\\

Summary:	Extended attributes for python
Name:		python-xattr
Version:	0.9.9
Release:	1
License:	GPL
Group:		Development/Python
URL:		http://pypi.python.org/pypi/xattr
Source0:	https://github.com/xattr/xattr/archive/v%{version}.tar.gz
Provides:	pyxattr = %{version}-%{release}
BuildRequires:	attr-devel
BuildRequires:	pkgconfig(libffi)
BuildRequires:	python-cffi
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
BuildRequires:	python-pkg-resources

%description
python-xattr is a C extension module for Python which implements
extended attributes manipulation. It is a wrapper on top of the
attr C library - see attr(5).

%prep
%autosetup -n %{real_name}-%{version}

%build
export CFLAGS="%{optflags}"
%py_build


%install
%py_install -- --install-purelib=%{python_sitearch}

%files
%{py_platsitedir}/*
%{_bindir}/xattr
