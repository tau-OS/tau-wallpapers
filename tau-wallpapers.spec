%global Bg_Name tauOS
%global bgname tauos

Name:       tau-wallpapers
Version:    1.1
Release:    5%{?dist}
Summary:    tauOS %{VERSION} default desktop background

License:    CC-BY-SA-4.0
URL:        https://tauos.co
Source0:    https://github.com/tau-OS/%{NAME}/releases/download/v%{VERSION}/%{NAME}-%{VERSION}.tar.gz

BuildRoot:  %{_tmppath}/%{name}
BuildArch:  noarch

Requires:   %{name}-gnome

BuildRequires:  meson

%description
This package contains desktop backgrounds for the tauOS %{VERSION} default
theme.  Pulls in themes for GNOME.

%package	base
Summary:    Base images for tauOS  %{VERSION} default background
License:    CC-BY-SA

%description	base
This package contains base images for tauOS  %{VERSION} default background.

%package	gnome
Summary:    tauOS  %{VERSION} default wallpaper for Gnome and Cinnamon
Requires:   %{name}-base = %{version}-%{release}

%description	gnome
This package contains Gnome desktop wallpaper for the
tauOS  %{VERSION} default theme.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md

%files base
%license Attribution
%dir %{_datadir}/backgrounds/%{bgname}
%{_datadir}/backgrounds/%{bgname}/*.{png,jpg,xml}

%files gnome
%dir %{_datadir}/gnome-background-properties/
%{_datadir}/gnome-background-properties/*.xml

%changelog
* Thu Apr 28 2022 Lains <lainsce@airmail.cc> - 1.1-5
- Make MORE Light/Dark pairs

* Thu Apr 28 2022 Lains <lainsce@airmail.cc> - 1.1-4
- Make more Light/Dark pairs

* Mon Apr 25 2022 Lains <lainsce@airmail.cc> - 1.1-3
- Remove the default wallpapers (tau-light and tau-dark) from slideshow XML

* Mon Apr 25 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-2
- Dark Mode Wallpapers
- Switch to Meson

* Sat Apr 23 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1
- Update for CI

* Wed Mar 23 2022 Jamie Lee <jamie@innatical.com> - 1.1-0
- Update for Fedora 36

* Mon Feb 22 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 35.0.0-1
- Initial package
