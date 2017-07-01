%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE icon theme faenza
Name:		mate-icon-theme-faenza
Version:	1.18.0
Release:	1
Group:		Graphical desktop/Other
License:	GPLv2+
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	icon-naming-utils
BuildRequires:	mate-common

%description
This icon theme uses Faenza and Faience icon themes by ~Tiheum and
some icons customized for MATE by Rowen Stipe.

%prep
%setup -q

%build
#NOCONFIGURE=1 ./autogen.sh
%configure \
	--enable-icon-mapping \
	%{nil}

%install
%makeinstall_std

%post
/bin/touch --no-create %{_datadir}/icons/matefaenza &>/dev/null || :
/bin/touch --no-create %{_datadir}/icons/matefaenzagray &>/dev/null || :
/bin/touch --no-create %{_datadir}/icons/matefaenzadark &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/matefaenza &>/dev/null
    /bin/touch --no-create %{_datadir}/icons/matefaenzagray &>/dev/null
    /bin/touch --no-create %{_datadir}/icons/matefaenzadark &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/matefaenza &>/dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/matefaenzagray &>/dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/matefaenzadark &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/matefaenza &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/matefaenzagray &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/matefaenzadark &>/dev/null || :

%files
%doc COPYING AUTHORS NEWS README
%{_datadir}/icons/matefaenza/
%{_datadir}/icons/matefaenzagray/
%{_datadir}/icons/matefaenzadark/

