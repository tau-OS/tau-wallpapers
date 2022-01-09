%bcond_with el

%global relnum 1
%global Bg_Name tauOS
%global bgname %(t="%{Bg_Name}";echo ${t,,})

Name:       tau-wallpapers
Version:    %{relnum}.0.0
%if %{with el}
Release:    2.el8
%else
Release:    2%{?dist}
%endif
Summary:    tauOS %{relnum} default desktop background

License:    CC-BY-SA-4.0
URL:        https://github.com/tauLinux/%{name}
Source0:    https://github.com/tauLinux/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz

BuildRoot:  %{_tmppath}/%{name}
BuildArch:  noarch

Requires:   %{name}-gnome

# for %%_kde4_* macros
BuildRequires:  kde-filesystem


%description
This package contains desktop backgrounds for the tauOS %{relnum} default
theme.  Pulls in themes for GNOME.

%package	base
Summary:    Base images for tauOS  %{relnum} default background
License:    CC-BY-SA

%description	base
This package contains base images for tauOS  %{relnum} default background.

%package	gnome
Summary:    tauOS  %{relnum} default wallpaper for Gnome and Cinnamon
Requires:   %{name}-base = %{version}-%{release}

%description	gnome
This package contains Gnome desktop wallpaper for the
tauOS  %{relnum} default theme.

%package	kde
Summary:    tauOS  %{relnum} default wallpaper for KDE
Requires:   %{name}-base = %{version}-%{release}
Requires:   kde-filesystem

%description	kde
This package contains KDE desktop wallpaper for the
tauOS  %{relnum} default theme.

%prep
%setup -q

%build


%install
%make_install

%files
%doc

%files base
%license COPYING Attribution
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
* Mon Feb 22 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 35.0.0-1
- Initial package
