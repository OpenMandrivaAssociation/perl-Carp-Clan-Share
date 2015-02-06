%define upstream_name    Carp-Clan-Share
%define upstream_version 0.013

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Share your Carp::Clan settings with your whole Clan
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Carp/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp::Clan)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.13.0-2mdv2011.0
+ Revision: 654883
- rebuild for updated spec-helper

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.13.0-1mdv2011.0
+ Revision: 471069
- import perl-Carp-Clan-Share


* Sun Nov 29 2009 cpan2dist 0.013-1mdv
- initial mdv release, generated with cpan2dist
