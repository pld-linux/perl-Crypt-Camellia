#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	Camellia
Summary:	Crypt::Camellia - Crypt::CBC-compliant block cipher
Summary(pl):	Crypt::Camellia - szyfr blokowy kompatybilny z Crypt::CBC
Name:		perl-Crypt-Camellia
Version:	1.0.1
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	55dc7f13e5aeb0a954b95769dbb1a1bd
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Camellia is a variable-length key, 128-bit block cipher. It is the
NESSIE winner for 128-bit block ciphers. The default key length in
this implementation is 128 bits. This module supports the Crypt::CBC
interface.

%description -l pl
Camellia to 128-bitowy szyfr blokowy o zmiennej d³ugo¶ci klucza. Jest
zwyciêzc± NESSIE dla 128-bitowych szyfrów blokowych. Domy¶lny rozmiar
klucza w tej implementacji to 128 bitów. Modu³ obs³uguje interfejs
Crypt::CBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd examples
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
for f in * ; do
	sed -e "s@#!/usr/local/bin/perl@#!/usr/bin/perl@" $f \
		> $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/Camellia.pm
%dir %{perl_vendorarch}/auto/Crypt/Camellia
%{perl_vendorarch}/auto/Crypt/Camellia/Camellia.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Camellia/Camellia.so
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
