%global debug_package %{nil}
%global gitdate 20181001
%global commit0 0120ead4d6add47e4d84b5453f8f1e6bf0c25eda
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           yaru
Version:        18.10.5
Release:        1%{?dist}
Summary:        Ubuntu community theme "yaru" 

License:        LGPLv3
URL:            https://github.com/ubuntu/yaru
Source0:	https://github.com/ubuntu/yaru/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:	sassc

Requires:	yaru-gnome-shell-theme 
Requires:	yaru-icon-theme 
Requires:	yaru-gtk2-theme 
Requires:	yaru-gtk3-theme 
Requires:	yaru-sound-theme
Provides:	communitheme = %{version}-%{release}

%description
Ubuntu community theme "yaru" formaly communitheme; the default theme for Ubuntu

#--
%package gnome-shell-theme
Summary:        GNOME Shell Ubuntu community theme "yaru"
Requires:       %{name}-icon-theme = %{version}-%{release}

%description gnome-shell-theme
GNOME Shell Ubuntu community theme "yaru"

#--
%package icon-theme
Summary:        Icon theme Ubuntu community theme "yaru"

%description icon-theme
Icon theme Ubuntu community theme "yaru"

#--
%package gtk2-theme
Summary:        The GTK+ 2 parts of the Ubuntu community theme "yaru"

%description gtk2-theme
The GTK+ 2 parts of the Ubuntu community theme "yaru"

#--
%package gtk3-theme
Summary:        The GTK+ 3 parts of the Ubuntu community theme "yaru"

%description gtk3-theme
The GTK+ 3 parts of the Ubuntu community theme "yaru"

#--
%package sound-theme
Summary:        Sound theme Ubuntu community theme "yaru"

%description sound-theme
Sound theme Ubuntu community theme "yaru"

%prep
%autosetup -n %{name}-%{commit0} 

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%post icon-theme
/bin/touch --no-create %{_datadir}/icons/%{name} &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :

%postun icon-theme
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/%{name} &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :
fi

%posttrans icon-theme
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :

%files
%{_datadir}/glib-2.0/schemas/99_Yaru.gschema.override

%files gnome-shell-theme
%{_datadir}/gnome-shell/
%{_datadir}/wayland-sessions/Yaru-wayland.desktop
%{_datadir}/xsessions/Yaru.desktop

%files icon-theme
%{_datadir}/icons/Yaru/
%{_datadir}/themes/Yaru/index.theme

%files gtk2-theme
%{_datadir}/themes/Yaru/gtk-2.0/

%files gtk3-theme
%{_datadir}/themes/Yaru/gtk-3.0/
%{_datadir}/themes/Yaru-dark/gtk-3.0/assets
%{_datadir}/themes/Yaru-dark/gtk-3.0/gtk.css
%{_datadir}/themes/Yaru-dark/index.theme


%files sound-theme
%{_datadir}/sounds/Yaru/

%changelog

* Mon Oct 01 2018 David Va <davidva AT tuta DOT io> 18.10.5-1
- Updated to 18.10.5

* Mon Sep 17 2018 David Va <davidva AT tuta DOT io> 18.10.4-1
- Updated to 18.10.4

* Fri Sep 14 2018 David Va <davidva AT tuta DOT io> 18.10.3-1
- Updated to 18.10.3

* Sun Aug 05 2018 David Va <davidva AT tuta DOT io> 18.10.1-2
- Updated to current commit

* Sun Aug 05 2018 David Va <davidva AT tuta DOT io> 18.10.1-1
- Updated to 18.10.1

* Thu Jul 26 2018 David Va <davidva AT tuta DOT io> 18.10-1
- Initial build

