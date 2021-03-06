Name:           sourcehut-core
Version:        0.62.3
Release:        2%{?dist}
Summary:        Sourcehut core functionality

License:        APGL
URL:            https://git.sr.ht/~sircmpwn/core.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/core.sr.ht/archive/%{version}.tar.gz
Source1:        core.ini

BuildRequires:  python3-srht
Requires:       python3-srht

%description
Sourcehut core functionality

%global debug_package %{nil}

%prep
%autosetup -n core.sr.ht-%{version}


%build

%install
mkdir -p %{buildroot}/%{_sysconfdir}/sr.ht/
mkdir -p %{buildroot}/%{_bindir}

install -m 0755 srht-keygen %{buildroot}/%{_bindir}/srht-keygen
install -m 0755 srht-migrate %{buildroot}/%{_bindir}/srht-migrate
install -m 0755 srht-replicate-db %{buildroot}/%{_bindir}/srht-replicate-db
install -m 0755 srht-update-profiles %{buildroot}/%{_bindir}/srht-update-profiles

cp %{SOURCE1} %{buildroot}/%{_sysconfdir}/sr.ht/core.ini



%files
%license LICENSE
%doc README.md
%config %{_sysconfdir}/sr.ht/core.ini
%{_bindir}/srht-keygen
%{_bindir}/srht-migrate
%{_bindir}/srht-replicate-db
%{_bindir}/srht-update-profiles

%changelog
* Sun Jun 14 2020 Tyler Griffiths <t@tyjgr.com>
- 
