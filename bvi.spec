Summary:	Binary vi
Summary(pl):	Binarny vi
Name:		bvi
Version:	1.3.2
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/bvi/%{name}-%{version}.src.tar.gz
# Source0-md5:	4257305ffb27177a6d5208b2df4ca92d
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-paths.patch
URL:		http://bvi.sf.net/
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bvi is a simple binary file editor which user interface is based on vi
editor.

%description -l pl
bvi to prosty edytor plików binarnych z interfejsem wzorowanym na
edytorze vi.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
%doc README CHANGES CREDITS html/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
