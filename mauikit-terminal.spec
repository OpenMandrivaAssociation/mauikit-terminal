%define major 4

#define snapshot 20220106
%define libname %mklibname MauiKitTerminal
%define devname %mklibname -d MauiKitTerminal

Name:		mauikit-terminal
Version:	4.0.1
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Terminal support components for Maui applications
Url:		https://mauikit.org/
Source0:	https://invent.kde.org/maui/mauikit-terminal/-/archive/%{?snapshot:master/mauikit-terminal-master.tar.bz2#/mauikit-terminal-%{snapshot}.tar.bz2}%{!?snapshot:v%{version}/mauikit-terminal-v%{version}.tar.bz2}

License:	LGPL-2.1-or-later, CC0 1.0, BSD-2-Clause
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit4)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Network)
BuildRequires:  cmake(KF6Pty)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KDecoration2)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(KF6Attica)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6WebEngineCore)

%description
Library for developing MAUI Terminal applications

%package -n %{libname}
Summary:	Library files for Maui Terminal

%description -n %{libname}
Library files for mauikit-terminal


%package -n %{devname}
Summary:	Development files for mauikit-terminal
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for mauikit-terminal

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang mauikitterminal

%files -n %{libname} -f mauikitterminal.lang
%{_libdir}/libMauiKitTerminal4.so.%{major}*
%{_libdir}/qt6/qml/org/mauikit/

%files -n %{devname}
%{_includedir}/MauiKit4/Terminal/
%{_libdir}/cmake/MauiKitTerminal4/
%{_libdir}/libMauiKitTerminal4.so
