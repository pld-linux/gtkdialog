#
Summary:	Utility for fast and easy GUI building
Summary(pl.UTF-8):	Narzędzie do szybkiego i łatwego budowania interfejsów graficznych
Name:		gtkdialog
Version:	0.7.9
Release:	2
License:	GPL
Group:		Applications
Source0:	ftp://linux.pte.hu/pub/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	e0eebb5a1d2301738c34c8b5b692cf7a
Patch0:		%{name}-name_conflict.patch
URL:		http://linux.pte.hu/~pipas/gtkdialog/
BuildRequires:	libglade2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gtkdialog is a small utility for fast and easy GUI building.
It can be used to create dialog boxes for almost any interpreted
and compiled programs which is a very attractive feature since
the developer does not have to learn various GUI languages for
the miscellaneous programming languages.

%description -l pl.UTF-8
Gtkdialog to drobne narzędzie do szybkiego i łatwego budowania
interfejsów graficznych. Pozwala konstruować okna dialogowe w
niemalże każdym języku interpretowanym bądź kompilowanym, oszczędzając
programiście konieczność poznawania różnorakich bibliotek do
budowy GUI.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(777,root,root) %{_bindir}/%{name}
%{_infodir}/%{name}.info*
