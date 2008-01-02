
%define real_name pyxattr

Summary: Extended attributes for python
Name: python-xattr
Version: 0.2.2
Release: %mkrel 1
License: GPL
Group: Development/Python
URL: http://pyxattr.sourceforge.net/
Source: http://kent.dl.sourceforge.net/sourceforge/%{real_name}/%{real_name}-%{version}.tar.gz
Provides: pyxattr = %{version}-%{release}
BuildRequires: python-devel
BuildRequires: libattr-devel
Requires: python
BuildRoot: %{_tmppath}/%{name}--%{version}-%{release}-root

%description
python-xattr is a C extension module for Python which implements
extended attributes manipulation. It is a wrapper on top of the
attr C library - see attr(5).

%prep
%setup -n %{real_name}-%{version}

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
%{py_platsitedir}/xattr.so
# %{_docdir}/%{name}-%{version}/
%py_platsitedir/*.5.egg-info

