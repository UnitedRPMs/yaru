#
# spec file for package yaru
#
# Copyright (c) 2020 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://goo.gl/zqFJft
#

%global debug_package %{nil}
%global gitdate 20200319
%global commit0 c083339f2d113cbe60da3bf505d78c4741fec466
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

# 
%define _legacy_common_support 1

Name:           yaru
Version:        20.04.3
Release:        3%{?dist}
Summary:        Ubuntu community theme "yaru" 

License:        LGPLv3 and CC-BY-SA
URL:            https://github.com/ubuntu/yaru
Source0:	https://github.com/ubuntu/yaru/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  meson 
BuildRequires:  gcc
BuildRequires:	sassc
BuildRequires:	glib2-devel
BuildRequires:  hicolor-icon-theme

Requires:	yaru-gnome-shell-theme 
Requires:	yaru-icon-theme 
Requires:	yaru-gtk2-theme 
Requires:	yaru-gtk3-theme 
Requires:	yaru-sound-theme
Provides:	communitheme = %{version}-%{release}
Provides:	yaru-theme = %{version}-%{release}

%description
Ubuntu community theme "yaru" formaly communitheme; the default theme for Ubuntu
The complete theme.

#--
%package gnome-shell-theme
Summary:        GNOME Shell Ubuntu community theme "yaru"
Requires:       %{name}-icon-theme = %{version}-%{release}
Provides:	gnome-shell-theme-yaru = %{version}

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
Requires:       %{name}-icon-theme = %{version}-%{release}

%description gtk2-theme
The GTK+ 2 parts of the Ubuntu community theme "yaru"

#--
%package gtk3-theme
Summary:        The GTK+ 3 parts of the Ubuntu community theme "yaru"
Requires:       %{name}-icon-theme = %{version}-%{release}

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

rm -f %{buildroot}/%{_datadir}/themes/Yaru/gnome-shell
cp -rf %{buildroot}%{_datadir}/gnome-shell/theme/Yaru %{buildroot}/%{_datadir}/themes/Yaru/gnome-shell


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
%license COPYING COPYING.LGPL-2.1 COPYING.LGPL-3.0 LICENSE_CCBYSA
%doc AUTHORS CONTRIBUTING.md README.md
%{_datadir}/glib-2.0/schemas/99_Yaru.gschema.override

%files gnome-shell-theme
%{_datadir}/gnome-shell/extensions/ubuntu-dock@ubuntu.com/yaru.css
%{_datadir}/gnome-shell/modes/yaru.json
%exclude %{_datadir}/gnome-shell/theme/Yaru/
%{_datadir}/wayland-sessions/Yaru-wayland.desktop
%{_datadir}/xsessions/Yaru.desktop
%{_datadir}/themes/Yaru/gnome-shell/
%{_datadir}/gnome-shell/theme/Yaru-dark/
%{_datadir}/themes/Yaru-dark/gnome-shell

%files icon-theme
%{_datadir}/icons/Yaru/
%{_datadir}/themes/Yaru/index.theme
%{_datadir}/themes/Yaru/unity/

%files gtk2-theme
%{_datadir}/themes/Yaru/gtk-2.0/
%{_datadir}/themes/Yaru-dark/gtk-2.0/
%{_datadir}/themes/Yaru-light/gtk-2.0/

%files gtk3-theme
%{_datadir}/themes/Yaru/gtk-3.0/
%{_datadir}/themes/Yaru-dark/gtk-3.0/gtk.gresource
%{_datadir}/themes/Yaru-dark/gtk-3.0/gtk.css
%{_datadir}/themes/Yaru-dark/index.theme
%{_datadir}/themes/Yaru-dark/gtk-3.20/
%{_datadir}/themes/Yaru/gtk-3.20/
%{_datadir}/themes/Yaru-light/gtk-*/
%{_datadir}/themes/Yaru-light/index.theme

%files sound-theme
%{_datadir}/sounds/Yaru/

%changelog

* Thu Mar 19 2020 David Va <davidva AT tuta DOT io> 20.04.3-3
- Updated to 20.04.3

* Wed Mar 11 2020 David Va <davidva AT tuta DOT io> 20.04.2-3
- Updated to 20.04.2

* Thu Feb 13 2020 David Va <davidva AT tuta DOT io> 20.04.1-3
- Updated to current commit

* Thu Feb 06 2020 David Va <davidva AT tuta DOT io> 20.04.1-3
- Updated to 20.04.1

* Tue Jan 28 2020 David Va <davidva AT tuta DOT io> 19.10.5-3
- Updated to current commit

* Sun Jan 19 2020 David Va <davidva AT tuta DOT io> 19.10.5-2
- Updated to 19.10.5

* Sun Dec 15 2019 David Va <davidva AT tuta DOT io> 19.10.4-4
- Deleted symlink

* Sat Dec 14 2019 David Va <davidva AT tuta DOT io> 19.10.4-3
- Updated to current commit

* Thu Oct 31 2019 David Va <davidva AT tuta DOT io> 19.10.4-2
- Updated to current commit

* Fri Oct 04 2019 David Va <davidva AT tuta DOT io> 19.10.4-1
- Updated to 19.10.4

* Tue Aug 20 2019 David Va <davidva AT tuta DOT io> 19.10.1-1
- Updated to 19.10.1

* Thu Aug 15 2019 David Va <davidva AT tuta DOT io> 19.04.3-1
- Updated to 19.04.3

* Sat Jun 01 2019 David Va <davidva AT tuta DOT io> 19.04.2-4
- Updated to current commit

* Sat May 11 2019 David Va <davidva AT tuta DOT io> 19.04.2-3
- Updated to current commit

* Sat Apr 06 2019 David Va <davidva AT tuta DOT io> 19.04.2-2
- Updated to 19.04.2

* Tue Feb 26 2019 David Va <davidva AT tuta DOT io> 19.04-2
- Updated to current commit

* Wed Jan 16 2019 David Va <davidva AT tuta DOT io> 19.04-1
- Updated to 19.04

* Fri Dec 28 2018 David Va <davidva AT tuta DOT io> 18.10.7-6
- Updated to current commit

* Wed Dec 19 2018 David Va <davidva AT tuta DOT io> 18.10.7-5
- Updated to current commit

* Wed Dec 12 2018 David Va <davidva AT tuta DOT io> 18.10.7-4
- Updated to current commit

* Thu Nov 15 2018 David Va <davidva AT tuta DOT io> 18.10.7-3
- Updated to current commit

* Mon Oct 29 2018 David Va <davidva AT tuta DOT io> 18.10.7-2
- Updated to current commit

* Mon Oct 22 2018 David Va <davidva AT tuta DOT io> 18.10.7-1
- Updated to 18.10.7

* Wed Oct 10 2018 David Va <davidva AT tuta DOT io> 18.10.6-1
- Updated to 18.10.6

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

