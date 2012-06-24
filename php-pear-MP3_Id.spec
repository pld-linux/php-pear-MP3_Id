%include	/usr/lib/rpm/macros.php
%define         _class          MP3
%define		_subclass	Id
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Read/Write MP3-Tags
Summary(pl):	%{_pearname} - Odczyt/Zapis tag�w MP3
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The class offers methods for reading and writing information tags
(version 1) in MP3 files

This class has in PEAR status: %{_status}.

%description -l pl
Ta klasa udost�pnia mo�liwo�� odczytu i zapisu tag�w (wersja 1) w
plikach MP3.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
