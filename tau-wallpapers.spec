%global relnum 1
%global Bg_Name tau-wallpapers
%global bgname %(t="%{Bg_Name}";echo ${t,,})

Name:       %{bgname}
Version:    %{relnum}.0.0
Release:    1%{?dist}
Summary:    tauOS %{relnum} default desktop background

License:    CC-BY-SA-4.0
URL:        https://github.com/tauLinux/%{name}
Source0:    https://github.com/tauLinux/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz

BuildRoot:  %{_tmppath}/%{name}
BuildArch:  noarch

Requires:   %{name}-gnome


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
%{_datadir}/backgrounds/%{bgname}/default/%{bgname}*.{png,xml}

%files gnome
%{_datadir}/gnome-background-properties/%{bgname}.xml
%dir %{_datadir}/gnome-background-properties/

%changelog
* Mon Feb 22 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 35.0.0-1
- Initial package
