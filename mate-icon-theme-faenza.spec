%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE icon theme faenza
Name:		mate-icon-theme-faenza
Version:	1.18.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	icon-naming-utils
BuildRequires:	intltool
BuildRequires:	mate-common

Requires:	hicolor-icon-theme

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides a theme using Faenza and Faience icon themes by ~Tiheum
and some icons customized for MATE by Rowen Stipe.

%files
%doc COPYING AUTHORS NEWS README
%dir %{_iconsdir}/matefaenza
%{_iconsdir}/matefaenza/*
%ghost %{_iconsdir}/matefaenza/icon-theme.cache
%dir %{_iconsdir}/matefaenzagray
%{_iconsdir}/matefaenzagray/*
%ghost %{_iconsdir}/matefaenzagray/icon-theme.cache
%dir %{_iconsdir}/matefaenzadark
%{_iconsdir}/matefaenzadark/*
%ghost %{_iconsdir}/matefamatefaenzadarkenza/icon-theme.cache

#---------------------------------------------------------------------------

%prep
%setup -q

%build
#NOCONFIGURE=1 ./autogen.sh
%configure \
	--enable-icon-mapping \
	%{nil}

%install
%makeinstall_std

touch %{buildroot}%{_iconsdir}/matefaenza/icon-theme.cache
touch %{buildroot}%{_iconsdir}/matefaenzagray/icon-theme.cache
touch %{buildroot}%{_iconsdir}/matefaenzadark/icon-theme.cache

# automatic gtk icon cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %{buildroot}%{_var}/lib/rpm/filetriggers
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-mate-faenza.filter << EOF
^./usr/share/icons/matefaenza/
^./usr/share/icons/matefaenzagray/
^./usr/share/icons/matefaenzadark/
EOF
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-mate-faenza.script << EOF
#!/bin/sh
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/matefaenza
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/matefaenzagray
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/matefaenzadark
fi
EOF
chmod 0755 %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-mate-faenza.script

%post
%update_icon_cache matefaenza matefaenzagray matefaenzadark

%postun
%clean_icon_cache matefaenza matefaenzagray matefaenzadark

