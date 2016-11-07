# Created by pyp2rpm-3.2.1
%global pypi_name pytest-ansible-playbook

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Pytest fixture which runs given ansible playbook file

License:        Apache 2.0
URL:            https://gitlab.com/mbukatov/pytest-ansible-playbook
Source0:        
BuildArch:      noarch
 
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Pytest fixture which runs given ansible playbook file
 
Requires:       python%{python3_pkgversion}-pytest >= 2.9.2
Requires:       python%{python3_pkgversion}-setuptools
%description -n python%{python3_pkgversion}-%{pypi_name}



%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}


%files -n python%{python3_pkgversion}-%{pypi_name} 
%doc README.rst
%dir %{python3_sitelib}/__pycache__/
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_ansible_playbook.py
%{python3_sitelib}/pytest_ansible_playbook
%{python3_sitelib}/pytest_ansible_playbook-%{version}-py?.?.egg-info

%changelog
* Mon Nov 07 2016 Martin Bukatovic <mbukatov@redhat.com> - 0.3.0-1
- Initial package.
