# Created by pyp2rpm-3.1.3
%global pypi_name mrglog

Name:           python-%{pypi_name}
Version:        0.1.0
Release:        1%{?dist}
Summary:        MRG log module

License:        Apache 2.0
URL:            https://github.com/ltrilety/mrglog
Source0:        
BuildArch:      noarch
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
 mrglog 'MRG' logger module

%package -n     python2-%{pypi_name}
Summary:        MRG log module
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
 mrglog 'MRG' logger module

%package -n     python3-%{pypi_name}
Summary:        MRG log module
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 mrglog 'MRG' logger module


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install
cp %{buildroot}/%{_bindir}/mrglog_demo.py %{buildroot}/%{_bindir}/mrglog_demo.py-3
ln -sf %{_bindir}/mrglog_demo.py-3 %{buildroot}/%{_bindir}/mrglog_demo.py-%{python3_version}

%py2_install
cp %{buildroot}/%{_bindir}/mrglog_demo.py %{buildroot}/%{_bindir}/mrglog_demo.py-2
ln -sf %{_bindir}/mrglog_demo.py-2 %{buildroot}/%{_bindir}/mrglog_demo.py-%{python2_version}


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/mrglog_demo.py
%{_bindir}/mrglog_demo.py-2
%{_bindir}/mrglog_demo.py-%{python2_version}

%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/mrglog_demo.py-3
%{_bindir}/mrglog_demo.py-%{python3_version}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Nov 04 2016 Martin Bukatovic <mbukatov@redhat.com> - 0.1.0-1
- Initial package.
