# Updated by spec2scl-1.1.3
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.2.1
%global pypi_name mrglog

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.1.1
Release:        1%{?dist}
Summary:        MRG log module

License:        Apache 2.0
URL:            https://github.com/ltrilety/mrglog
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  %{?scl_prefix_python}python-devel
BuildRequires:  %{?scl_prefix_python}python-setuptools
%{?scl:BuildRequires: %{scl}-build %{scl}-runtime}
%{?scl:Requires: %{scl}-runtime}

%description

%prep
# TODO: use %setup -q -n instead?
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{?scl:scl enable %{scl} - << \EOF}
%{__python} setup.py build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
%{__python} setup.py install --skip-build --root %{buildroot} --install-purelib %{python_sitelib} --install-scripts %{python_sitelib}/../../../bin
%{?scl:EOF}

%files
%doc README.rst
%{_bindir}/mrglog_demo.py
%dir %{python_sitelib}/__pycache__/
%{python_sitelib}/__pycache__/*
%{python_sitelib}/%{pypi_name}.py
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Nov 08 2016 Martin Bukatovic <mbukatov@redhat.com> - 0.1.1-1
- Initial package.
