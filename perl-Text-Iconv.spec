Name:           perl-Text-Iconv
Version:        1.7
Release:        6%{?dist}
Summary:        Perl interface to iconv() codeset conversion function

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Text-Iconv/
Source0:        http://www.cpan.org/authors/id/M/MP/MPIOTR/Text-Iconv-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Text::Iconv module provides a Perl interface to the iconv()
function as defined by the Single UNIX Specification. The convert()
method converts the encoding of characters in the input string from
the fromcode codeset to the tocode codeset, and returns the result.
Settings of fromcode and tocode and their permitted combinations are
implementation-dependent. Valid values are specified in the system
documentation.


%prep
%setup -q -n Text-Iconv-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/Text/
%{_mandir}/man3/Text::Iconv.3*


%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.7-4
- Rebuild for perl 5.10 (again)

* Tue Feb 12 2008 Andreas Thienemann <athienem@redhat.com> - 1.7-3
- Rebuilt against gcc-4.3

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.7-2
- rebuild for new perl

* Wed Nov  7 2007 Marcela Maslanova <mmaslano@redhat.com> - 1.7-1
- upgrade on 1.7
- Resolves: rhbz#331011

* Fri Aug 31 2007 Andreas Thienemann <andreas@bawue.net> - 1.5-1
- Updated to new upstream release

* Tue Apr 17 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.4-6
- BuildRequire perl(ExtUtils::MakeMaker).

* Wed Aug 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4-5
- Fix order of arguments to find(1).
- Drop version from perl build dependency.

* Thu Feb 16 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4-4
- Rebuild.

* Thu Jan 19 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4-3
- Specfile cleanup.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.4-2
- rebuilt

* Sun Jul 18 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.4-0.fdr.1
- Update to 1.4, INSTALLDIRS= fixed upstream.

* Tue Jun 29 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.3-0.fdr.1
- Update to 1.3, patch naughty upstream Makefile.PL so that INSTALLDIRS= works.
- Avoid RPATH on < FC2.

* Sun May  9 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.2-0.fdr.7
- BuildRequire perl >= 1:5.6.1-34.99.6 for support for vendor installdirs.
- Use pure_install to avoid perllocal.pod workarounds.

* Sun Apr 25 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.2-0.fdr.6
- Require perl(:MODULE_COMPAT_*).

* Mon Feb  2 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.2-0.fdr.5
- Reduce directory ownership bloat.

* Tue Dec  2 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.2-0.fdr.4
- Specfile cleanup.

* Sun Aug 31 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.2-0.fdr.3
- Install into vendor dirs.

* Fri Jul  4 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.2-0.fdr.2
- Fix dir ownerships and non-root strip during build.
- Update description.

* Wed May  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.2-0.fdr.1
- First Fedora release.
