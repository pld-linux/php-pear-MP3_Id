%include	/usr/lib/rpm/macros.php
%define		_class		MP3
%define		_subclass	Id
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - read/write MP3-Tags
Summary(pl):	%{_pearname} - odczyt/zapis tagów MP3
Name:		php-pear-%{_pearname}
Version:	1.1.4
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b715512310ee7744ef62ab9ca2300cc0
URL:		http://pear.php.net/package/MP3_Id/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The class offers methods for reading and writing information tags
(version 1) in MP3 files

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa udostêpnia mo¿liwo¶æ odczytu i zapisu tagów (wersja 1) w
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
