# Generated by spec2scl
%global scl_name_prefix rh-
%global scl_name_base usmqetools
%global scl_name_version 10
%global scl %{scl_name_prefix}%{scl_name_base}%{scl_name_version}

## General notes about python3x SCL packaging
# - the names of packages are NOT prefixed with 'python3-' (e.g. are the same as in Fedora)
# - the names of binaries of Python 3 itself are both python{-debug,...} and python3{-debug,...}
#   so both are usable in shebangs, the non-versioned binaries are preferred.
# - the names of other binaries are NOT prefixed with 'python3-'.
# - there are both macros in '3' variant and non-versioned variant, e.g. both %%{__python}
#   and %%{__python3} are available

%global nfsmountable 1

%scl_package %scl
%global _turn_off_bytecompile 1

%global install_scl 1

# Do not produce empty debuginfo package.
%global debug_package %{nil}

Summary: Package that installs %scl
Name: %scl_name
Version: 1.0
Release: 1%{?dist}
License: GPLv2+
Source1: README
Source2: LICENSE
BuildRequires: help2man
BuildRequires: scl-utils-build
%if 0%{?install_scl}
# Put your scl requires here
%endif

%description
This is the main package for %scl Software Collection.

%package runtime
Summary: Package that handles %scl Software Collection.
Requires: scl-utils

%description runtime
Package shipping essential scripts to work with %scl Software Collection.

%package build
Summary: Package shipping basic build configuration
Requires: scl-utils-build

%description build
Package shipping essential configuration macros to build %scl Software Collection.

%package scldevel
Summary: Package shipping development files for %scl

%description scldevel
Package shipping development files, especially usefull for development of
packages depending on %scl Software Collection.

%prep
%setup -T -c

# This section generates README file from a template and creates man page
# from that file, expanding RPM macros in the template file.
cat >README <<'EOF'
%{expand:%(cat %{SOURCE1})}
EOF

# copy the license file so %%files section sees it
cp %{SOURCE2} .

%build
# generate a helper script that will be used by help2man
cat >h2m_helper <<'EOF'
#!/bin/bash
[ "$1" == "--version" ] && echo "%{scl_name} %{version} Software Collection" || cat README
EOF
chmod a+x h2m_helper

# generate the man page
help2man -N --section 7 ./h2m_helper -o %{scl_name}.7

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_scl_scripts}/root
mkdir -p %{buildroot}%{_root_prefix}/lib/rpm/redhat
cat >> %{buildroot}%{_scl_scripts}/enable << EOF
export PATH=%{_bindir}\${PATH:+:\${PATH}}
export LD_LIBRARY_PATH=%{_libdir}\${LD_LIBRARY_PATH:+:\${LD_LIBRARY_PATH}}
export MANPATH=%{_mandir}:\${MANPATH}
EOF
%scl_install


# Create the scldevel subpackage macros                                                             

cat >> %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel << EOF
%%scl_%{scl_name_base} %{scl}
%%scl_prefix_%{scl_name_base} %{scl_prefix}
EOF


# install generated man page
mkdir -p %{buildroot}%{_mandir}/man7/
install -m 644 %{scl_name}.7 %{buildroot}%{_mandir}/man7/%{scl_name}.7

%files
%if 0%{?rhel} <= 6
%files runtime
%else
%files runtime -f filesystem
%endif
%doc README LICENSE
%scl_files
%{_mandir}/man7/%{scl_name}.*

%files build
%{_root_sysconfdir}/rpm/macros.%{scl}-config

%files scldevel
%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel

%changelog
* Wed Nov 09 2016 Martin Bukatovic <mbukatov@redhat.com> - 1.0-1
- Initial package.
