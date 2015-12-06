Summary:	Binary vi
Summary(pl.UTF-8):	Binarny vi
Name:		bvi
Version:	1.4.0
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	http://downloads.sourceforge.net/bvi/%{name}-%{version}.src.tar.gz
# Source0-md5:	aa83eb8b2b6b0bb6cdd8e6beef12b775
Patch0:		%{name}-home_etc.patch
URL:		http://bvi.sourceforge.net/
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bvi is a simple binary file editor which user interface is based on vi
editor.

%description -l pl.UTF-8
bvi to prosty edytor plików binarnych z interfejsem wzorowanym na
edytorze vi.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--with-ncurses=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES CREDITS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
