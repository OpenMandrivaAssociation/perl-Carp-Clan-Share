%define upstream_name    Carp-Clan-Share
%define upstream_version 0.013

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Share your Carp::Clan settings with your whole Clan
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Carp/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp::Clan)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is a very lightweight helper module (actually just an import method)
that will automagically create a __PACKAGE__::Carp module for you.

Any arguments passed to the import (e.g. via use) method are forwarded
along to Carp::Clan.

NOTE: If you use this from a package ending with ::Carp, then it will use
the parent of of that package as the target namespace

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


