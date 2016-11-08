# Created by pyp2rpm-3.2.1
%global pypi_name mrglog

Name:           python-%{pypi_name}
Version:        0.1.1
Release:        1%{?dist}
Summary:        MRG log module

License:        Apache 2.0
URL:            https://github.com/ltrilety/mrglog
Source0:        
BuildArch:      noarch
 
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        MRG log module

%description -n python%{python3_pkgversion}-%{pypi_name}



%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}
cp %{buildroot}/%{_bindir}/mrglog_demo.py %{buildroot}/%{_bindir}/mrglog_demo.py-3
ln -sf %{_bindir}/mrglog_demo.py-3 %{buildroot}/%{_bindir}/mrglog_demo.py-%{python3_version}


%files -n python%{python3_pkgversion}-%{pypi_name} 
%doc README.rst
%{_bindir}/mrglog_demo.py
%{_bindir}/mrglog_demo.py-3
%{_bindir}/mrglog_demo.py-%{python3_version}
%dir %{python3_sitelib}/__pycache__/
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Nov 08 2016 Martin Bukatovic <mbukatov@redhat.com> - 0.1.1-1
- Initial package.
