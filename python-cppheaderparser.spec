%global pypi_name cppheaderparser
 
Name:           python-%{pypi_name}
Version:        2.7.4
Release:        1
Summary:        Parse C++ header files and generate a data structure
License:        BSD
URL:            http://senexcanis.com/open-source/cppheaderparser/
Source0:        https://pypi.io/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%description
Parse C++ header files and generate a data structure representing the
class.

%prep
%autosetup -n CppHeaderParser-%{version}
rm -rf %{pypi_name}.egg-info
# Remove outdated parts (Python 2.x)
rm -rf CppHeaderParser/{examples,docs}
sed -i -e '/^#!\//, 1d' CppHeaderParser/CppHeaderParser.py
 
%build
%py_build

%install
%py_install

%files
%doc README.txt README.html
%{python_sitelib}/CppHeaderParser/
%{python_sitelib}/CppHeaderParser-%{version}-py%{python_version}.egg-info/
