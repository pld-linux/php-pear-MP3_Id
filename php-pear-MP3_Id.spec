%include	/usr/lib/rpm/macros.php
%define		_class		MP3
%define		_subclass	Id
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - read/write MP3-Tags
Summary(pl):	%{_pearname} - odczyt/zapis tag�w MP3
Name:		php-pear-%{_pearname}
Version:	1.2.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	508a5a7e9bb0e2e66914b8e88ad6e80c
URL:		http://pear.php.net/package/MP3_Id/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Obsoletes:	php-pear-MP3_ID
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The class offers methods for reading and writing information tags
(version 1) in MP3 files

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa udost�pnia mo�liwo�� odczytu i zapisu tag�w (wersja 1) w
plikach MP3.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
