Name:           sourcehut-git
Version:        0.54.2
Release:        10%{?dist}
Summary:        Git services for Sourcehut

License:        AGPL
URL:            https://git.sr.ht/~sircmpwn/git.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/git.sr.ht/archive/%{version}.tar.gz
Source1:        sourcehut-git.service
Source2:        git-srht.conf
Source3:        git-gunicorn-run.py
Source4:        git.ini
Source5:        sourcehut-git.timer
Source6:        sourcehut-git-api.service
BuildRequires:  python3-scmsrht, python3-devel, python3-gitsrht, sourcehut-core, sourcehut-meta, sassc, node, npm, git, golang
Requires:       python3-scmsrht, python3-gitsrht, python3-pygit2, python3-minio, sourcehut-core, sourcehut-meta, python3-gunicorn, golang

%global debug_package %{nil}

%description
Git services for Sourcehut


%prep
%autosetup -n git.sr.ht-%{version}


%build
%py3_build

cd api/
go build 

cd ../gitsrht-dispatch/
go build 

cd ../gitsrht-keys/
go build 

cd ../gitsrht-shell/
go build 

cd ../gitsrht-update-hook/
go build 

cd ..



%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/srht/git/html
mkdir -p %{buildroot}/%{_sysconfdir}/sr.ht
mkdir -p %{buildroot}/%{_sysconfdir}/systemd/system
mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}/%{_bindir}

cp -r static %{buildroot}/usr/share/srht/git/html/static

install -m 0755 gitsrht-initdb %{buildroot}/%{_bindir}/gitsrht-initdb
install -m 0755 gitsrht-migrate %{buildroot}/%{_bindir}/gitsrht-migrate
install -m 0755 gitsrht-periodic %{buildroot}/%{_bindir}/gitsrht-periodic
install -m 0755 cloneperf %{buildroot}/%{_bindir}/cloneperf

install -m 0755 api/api %{buildroot}/%{_bindir}/gitsrht-api
install -m 0755 gitsrht-dispatch/gitsrht-dispatch %{buildroot}/%{_bindir}/gitsrht-dispatch
install -m 0755 gitsrht-keys/gitsrht-keys %{buildroot}/%{_bindir}/gitsrht-keys
install -m 0755 gitsrht-shell/gitsrht-shell %{buildroot}/%{_bindir}/gitsrht-shell
install -m 0755 gitsrht-update-hook/gitsrht-update-hook %{buildroot}/%{_bindir}/gitsrht-update-hook

install -m 0755 run.py %{buildroot}/usr/share/srht/git/run.py

cp %{SOURCE1} %{buildroot}/%{_sysconfdir}/systemd/system/sourcehut-git.service
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/httpd/conf.d/50-git-srht.conf
install -m 0755 %{SOURCE3} %{buildroot}/usr/share/srht/git/gunicorn-run.py
cp %{SOURCE4} %{buildroot}/%{_sysconfdir}/sr.ht/git.ini
cp %{SOURCE5} %{buildroot}/%{_sysconfdir}/systemd/system/sourcehut-git.timer
cp %{SOURCE6} %{buildroot}/%{_sysconfdir}/systemd/system/sourcehut-git-api.service


%files
%doc README.md
%license LICENSE
%{_sysconfdir}/sr.ht/git.ini
%{_sysconfdir}/systemd/system/sourcehut-git.service
%{_sysconfdir}/systemd/system/sourcehut-git.timer
%{_sysconfdir}/systemd/system/sourcehut-git-api.service
%{_sysconfdir}/httpd/conf.d/50-git-srht.conf
%{_bindir}/gitsrht-initdb
%{_bindir}/gitsrht-migrate
%{_bindir}/gitsrht-periodic
%{_bindir}/cloneperf
%{_bindir}/gitsrht-dispatch
%{_bindir}/gitsrht-keys
%{_bindir}/gitsrht-shell
%{_bindir}/gitsrht-update-hook
%{_bindir}/gitsrht-api
/usr/share/srht/git/run.py
/usr/share/srht/git/gunicorn-run.py
/usr/share/srht/git/html


%changelog
* Sun Jun 14 2020 Tyler Griffiths <t@tyjgr.com>
- 
