Summary:	binary vi
Summary(pl):	binarny vi
Name:		bvi
Version:	1.3.1
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.src.tar.gz
URL:		http://bvi.sf.net/
#BuildRequires:
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

bvi is a simple binary file editor which user interface is based on vi editor.

%description -l pl

bvi to prosty edytor plików binarnych z interfejsem wzorowanym na edytorze vi.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --with-ncurses=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README CHANGES COPYING CREDITS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz html/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/bmore.help
%doc %{_mandir}/man1/*
