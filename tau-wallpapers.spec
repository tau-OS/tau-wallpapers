%global Bg_Name tauOS
%global bgname tauos

Name:       tau-wallpapers
Version:    1.1
Release:    1%{?dist}
Summary:    tauOS %{VERSION} default desktop background

License:    CC-BY-SA-4.0
URL:        https://tauos.co
Source0:    https://github.com/tau-OS/%{NAME}/releases/download/v%{VERSION}/%{NAME}-%{VERSION}.tar.gz

BuildRoot:  %{_tmppath}/%{name}
BuildArch:  noarch

Requires:   %{name}-gnome

# for %%_kde4_* macros
BuildRequires:  kde-filesystem
BuildRequires:  make

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

%package	kde
Summary:    tauOS  %{VERSION} default wallpaper for KDE
Requires:   %{name}-base = %{version}-%{release}
Requires:   kde-filesystem

%description	kde
This package contains KDE desktop wallpaper for the
tauOS  %{VERSION} default theme.

%prep
%setup -q

%build


%install
%make_install

%files
%doc README.md
%license COPYING

%files base
%license Attribution
%dir %{_datadir}/backgrounds/%{bgname}
%dir %{_datadir}/backgrounds/%{bgname}/default
%{_datadir}/backgrounds/%{bgname}/default/*.{png,jpg,xml}

%files gnome
%{_datadir}/gnome-background-properties/tau.xml
%dir %{_datadir}/gnome-background-properties/

%files kde
%{_kde4_datadir}/wallpapers/tauos/
%dir %{_datadir}/plasma/
%dir %{_datadir}/plasma/desktoptheme/
%{_datadir}/plasma/desktoptheme/tauos/

%changelog
* Sun Apr 10 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1
- Update Build Process

* Wed Mar 23 2022 Jamie Lee <jamie@innatical.com> - 1.1-0
- Update for Fedora 36

* Mon Feb 22 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 35.0.0-1
- Initial package
