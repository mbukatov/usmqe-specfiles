# Created by pyp2rpm-3.1.3
%global pypi_name pytest-ansible-playbook

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Pytest fixture which runs given ansible playbook file

License:        Apache 2.0
URL:            https://gitlab.com/mbukatov/pytest-ansible-playbook
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
pytestansibleplaybook This repository contains pytest_ plugin_ which provides
an easy way to run particular ansible playbooks_ during setup phase of a test
case. This is useful when you already have some playbook files you would like
to reuse during test setup or plan to maintain test setup in ansible playbooks
for you to be able to use it both during test run setup and directly via
ansible ...

%package -n     python2-%{pypi_name}
Summary:        Pytest fixture which runs given ansible playbook file
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-pytest >= 2.9.2
Requires:       python-setuptools
%description -n python2-%{pypi_name}
pytestansibleplaybook This repository contains pytest_ plugin_ which provides
an easy way to run particular ansible playbooks_ during setup phase of a test
case. This is useful when you already have some playbook files you would like
to reuse during test setup or plan to maintain test setup in ansible playbooks
for you to be able to use it both during test run setup and directly via
ansible ...

%package -n     python3-%{pypi_name}
Summary:        Pytest fixture which runs given ansible playbook file
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-pytest >= 2.9.2
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
pytestansibleplaybook This repository contains pytest_ plugin_ which provides
an easy way to run particular ansible playbooks_ during setup phase of a test
case. This is useful when you already have some playbook files you would like
to reuse during test setup or plan to maintain test setup in ansible playbooks
for you to be able to use it both during test run setup and directly via
ansible ...


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

%py2_install


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst

%{python2_sitelib}/pytest_ansible_playbook.py*
%{python2_sitelib}/pytest_ansible_playbook-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_ansible_playbook.py
%{python3_sitelib}/pytest_ansible_playbook-%{version}-py?.?.egg-info

%changelog
* Fri Nov 04 2016 Martin Bukatovic <mbukatov@redhat.com> - 0.3.0-1
- Initial package.
