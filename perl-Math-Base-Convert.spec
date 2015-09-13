#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Math
%define		pnam	Base-Convert
%include	/usr/lib/rpm/macros.perl
Summary:	Math::Base::Convert - very fast base to base conversion
Summary(pl.UTF-8):	Math::Base::Convert - bardzo szybka konwersja podstawy systemu liczenia
Name:		perl-Math-Base-Convert
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b892b20f5dd028264b1934179dc91ae0
URL:		http://search.cpan.org/dist/Math-Base-Convert/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
# diagnostics module requires perldiag.pod
BuildRequires:	perl-perldoc
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides fast functions and methods to convert between
arbitrary number bases from 2 (binary) thru 65535.

This module is pure Perl, has no external dependencies, and is
backward compatible with old versions of Perl 5.

%description -l pl.UTF-8
Ten moduł udostępnia szybkie funkcje i metody do konwersji między
dowolnymi podstawami systemu liczenia od 2 (binarnego) do 65535.

Ten moduł jest napisany w czystym Perlu i jest zgodny ze starszymi
wersjami Perla 5.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Math/Base
%{perl_vendorlib}/Math/Base/Convert.pm
%{perl_vendorlib}/Math/Base/Convert
%{_mandir}/man3/Math::Base::Convert*.3pm*
