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

%description -l pl

%prep
%setup -q -n %{name}-%{version}.orig -a 1
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%preun

%post

%postun

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
