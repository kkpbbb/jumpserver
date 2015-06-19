Name:           jumpserver
Version:        2.0.0
Release:        1%{?dist}
Summary:        xiaobing modified jumpserver support freeipa
License:        LGPL
#BuildArch:     noarch

Source0:        jumpserver.zip
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


BuildRequires:  automake autoconf gcc xz ncurses-devel patch python-devel git python-pip gcc-c++
BuildRequires:  nodejs npm

Requires:       automake autoconf gcc xz ncurses-devel patch python-devel git python-pip gcc-c++
Requires:       openldap-devel
Requires:       mysql-devel
Requires:       nodejs
Requires:       python




# disable debug packages and the stripping of the binaries
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}


%define installpath     /opt/jumpserver

%description
Xiao bing build free jumpserver support freeipa

%prep
%setup -q -n %{name}-master


%build
cd websocket
npm install


%install
rm -rf %{buildroot}
install -d $RPM_BUILD_ROOT%{installpath}
install -d $RPM_BUILD_ROOT%{installpath}/logs
cp -R * $RPM_BUILD_ROOT%{installpath}/
install -d $RPM_BUILD_ROOT/etc/profile.d
cp ./docs/zzjumpserver.sh $RPM_BUILD_ROOT/etc/profile.d
%{__install} -Dp -m0755 service.sh $RPM_BUILD_ROOT%{_initrddir}/%{name}



%pre

%clean
rm -rf %{buildroot}


%post
pip install --force-reinstall  -r %{installpath}/docs/requirements.txt -i http://pypi.douban.com/simple --log %{installpath}/pip_install.log 
/sbin/chkconfig --add %{name}
/sbin/service %{name} start 2>&1 >/dev/null


%preun
if [ "$1" = 0 ]; then
    /sbin/service %{name} stop &>/dev/null
    /sbin/chkconfig --del %{name}
fi
exit 0

%postun
if [ "$1" != 0 ]; then
    /sbin/service %{name} start 2>&1 >/dev/null
fi

%files
%defattr(-,root,root)
%{installpath}/*
%attr(0777, root, root) %{installpath}/logs
%config(noreplace) %{installpath}/jumpserver.conf
%attr(0644, root, root) /etc/profile.d/zzjumpserver.sh
%config %{_initrddir}/%{name}



%changelog
* Tue Jul 18 2015 xiaobing@aaa.com
- init 
