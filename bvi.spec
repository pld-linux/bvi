Summary:	Binary vi
Summary(pl):	Binarny vi
Name:		bvi
Version:	1.3.1
Release:	2
License:	GPL
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.src.tar.gz
# Source0-md5:	b9d77c57bda2e019207a1874d9bb4dea
Patch0:		%{name}-etc_dir.patch
URL:		http://bvi.sf.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bvi is a simple binary file editor which user interface is based on vi
editor.

%description -l pl
bvi to prosty edytor plik�w binarnych z interfejsem wzorowanym na
edytorze vi.

%prep
%setup -q
%patch0 -p1

%build
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
%{_datadir}/bmore.help
%doc %{_mandir}/man1/*
