Name:           sourcehut-meta
Version:        0.44.2
Release:        5%{?dist}
Summary:        Profile and credential storage for Sourcehut

License:        AGPL
URL:            https://git.sr.ht/~sircmpwn/meta.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/meta.sr.ht/archive/%{version}.tar.gz
#Source1:        sourcehut-meta.conf
Source2:        sourcehut-meta.service
Source3:        meta-srht.conf
BuildRequires:  python3-srht, python3-metasrht, sassc
Requires:       python3-srht, python3-metasrht, sassc

%description

%global debug_package %{nil}

%prep
%autosetup -n meta.sr.ht-%{version}

%build
rm static
cp -rL _static static
sassc scss/main.scss -I /usr/lib/python3.8/site-packages/srht/scss/ > static/main.css



%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/srht/meta/html/
mkdir -p %{buildroot}/%{_sysconfdir}/sr.ht
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}/systemd/system
mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d/

cp config.example.ini %{buildroot}%{_sysconfdir}/sr.ht


cp -r static %{buildroot}/usr/share/srht/meta/html/static

install -m 0755 run.py %{buildroot}/usr/share/srht/meta/run.py


# install -m 0755 metasrht-createuser %{buildroot}%{_bindir}/metasrht-createuser
# install -m 0755 metasrht-daily %{buildroot}%{_bindir}/metasrht-daily
# install -m 0755 metasrht-initdb %{buildroot}%{_bindir}/metasrht-initdb
# install -m 0755 metasrht-invoicestats %{buildroot}%{_bindir}/metasrht-invoicestats
# install -m 0755 metasrht-migrate %{buildroot}%{_bindir}/metasrht-migrate
# install -m 0755 scripts/revoke-expired-tokens %{buildroot}%{_bindir}/metasrht-revoke-expired-tokens

cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/systemd/system/
cp %{SOURCE3} %{buildroot}/%{_sysconfdir}/httpd/conf.d/meta-srht.conf

chmod a+xr -R %{buildroot}/usr/share/srht/

%files
%license LICENSE
%doc README.md
# %{_bindir}/metasrht-createuser
# %{_bindir}/metasrht-daily
# %{_bindir}/metasrht-initdb
# %{_bindir}/metasrht-invoicestats
# %{_bindir}/metasrht-migrate
# %{_bindir}/metasrht-revoke-expired-tokens

%config %{_sysconfdir}/sr.ht/config.example.ini
%config %{_sysconfdir}/httpd/conf.d/meta-srht.conf
%{_sysconfdir}/systemd/system/sourcehut-meta.service

/usr/share/srht/meta/



%changelog
* Fri Jun 12 2020 Tyler Griffiths <t@tyjgr.com>
- 