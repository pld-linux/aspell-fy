Summary:	Frisian dictionary for aspell
Summary(pl.UTF-8):	Słownik fryzyjski dla aspella
Name:		aspell-fy
Version:	0.12
%define	subv	0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/fy/aspell6-fy-%{version}-%{subv}.tar.bz2
# Source0-md5:	7c356ab9a52e546bdf75af8774b6d9bf
URL:		http://aspell.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Frisian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik fryzyjski (lista słów) dla aspella.

%prep
%setup -q -n aspell6-fy-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
