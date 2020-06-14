# Created by pyp2rpm-3.3.4
%global pypi_name pystache

Name:           python-%{pypi_name}
Version:        0.5.4
Release:        15%{?dist}
Summary:        Mustache for Python

License:        MIT
URL:            http://github.com/defunkt/pystache
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
.. Do not edit this file. This file is auto-generated for PyPI by setup.py ..
using pandoc, so edits should go in the source files rather than here.Pystache
.. figure:: figure:: < is a Python implementation of Mustache < Mustache is a
framework-agnostic, logic-free templating system inspired by ctemplate < and

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
.. Do not edit this file. This file is auto-generated for PyPI by setup.py ..
using pandoc, so edits should go in the source files rather than here.Pystache
.. figure:: figure:: < is a Python implementation of Mustache < Mustache is a
framework-agnostic, logic-free templating system inspired by ctemplate < and


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# %check
# %{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc pystache/tests/examples/readme.py README.md
%{_bindir}/pystache
%{_bindir}/pystache-test
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Jun 13 2020 Tyler Griffiths <t@tyjgr.com> - 0.5.4-1
- Initial package.
