#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%define		pdir	Crypt
%define		pnam	Camellia
Summary:	Crypt::Camellia - Crypt::CBC-compliant block cipher
Summary(pl.UTF-8):	Crypt::Camellia - szyfr blokowy kompatybilny z Crypt::CBC
Name:		perl-Crypt-Camellia
Version:	2.02
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/O/OY/OYAMA/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	47fd4ad377e5c4d45dbd29bf1e7d9f5c
URL:		http://search.cpan.org/dist/Crypt-Camellia/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Crypt-CBC
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Camellia is a variable-length key, 128-bit block cipher. It is the
NESSIE winner for 128-bit block ciphers. The default key length in
this implementation is 128 bits. This module supports the Crypt::CBC
interface.

%description -l pl.UTF-8
Camellia to 128-bitowy szyfr blokowy o zmiennej długości klucza. Jest
zwycięzcą NESSIE dla 128-bitowych szyfrów blokowych. Domyślny rozmiar
klucza w tej implementacji to 128 bitów. Moduł obsługuje interfejs
Crypt::CBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/Camellia.pm
%dir %{perl_vendorarch}/auto/Crypt/Camellia
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Camellia/Camellia.so
%{_mandir}/man3/*
