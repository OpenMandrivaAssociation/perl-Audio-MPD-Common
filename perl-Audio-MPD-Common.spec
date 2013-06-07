%define upstream_name	 Audio-MPD-Common
%define upstream_version 1.120881
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.120881
Release:	1

Summary:	A bunch of common helper classes for mpd
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Audio/Audio-MPD-Common-1.120881.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Util::TypeConstraints)
BuildRequires:	perl(MooseX::Has::Sugar)
BuildRequires:	perl(MooseX::Types::Moose)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(String::Formatter)

BuildArch:	noarch

%description
Depending on whether you're using a POE-aware environment or not, people
wanting to tinker with mpd (Music Player Daemon) will use either
POE::Component::Client::MPD or Audio::MPD.

But even if the run-cores of those two modules differ completely, they are
using the exact same common classes to represent the various mpd states and
information.

Therefore, those common classes have been outsourced to Audio::MPD::Common.

This module does not export any methods, but the dist provides the following
classes that you can query with perldoc:

o Audio::MPD::Common::Item
o Audio::MPD::Common::Item::Directory
o Audio::MPD::Common::Item::Playlist
o Audio::MPD::Common::Item::Song
o Audio::MPD::Common::Stats
o Audio::MPD::Common::Status
o Audio::MPD::Common::Time

Note that those modules should not be of any use outside the two mpd modules
afore-mentioned.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc LICENSE README Changes
%{perl_vendorlib}/Audio
%{_mandir}/man3/*


%changelog
* Wed Mar 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.110.550-1mdv2011.0
+ Revision: 641316
- update to new version 1.110550

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.430-1mdv2011.0
+ Revision: 505265
- update to 1.100430

* Mon Nov 16 2009 Jérôme Quelin <jquelin@mandriva.org> 1.93.190-1mdv2010.1
+ Revision: 466464
- adding missing buildrequires
- update to 1.093190

* Fri Nov 13 2009 Jérôme Quelin <jquelin@mandriva.org> 1.93.170-1mdv2010.1
+ Revision: 465859
- update to 1.093170

* Sun Nov 08 2009 Jérôme Quelin <jquelin@mandriva.org> 1.93.120-1mdv2010.1
+ Revision: 462997
- update to 1.093120

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.92.910-1mdv2010.1
+ Revision: 461287
- adding missing buildrequires:
- update to 1.092910

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.1.4-2mdv2010.0
+ Revision: 440533
- rebuild

* Wed Jan 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.4-1mdv2009.1
+ Revision: 326532
- update to new version 0.1.4

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.3-1mdv2009.1
+ Revision: 292027
- update to new version 0.1.3

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.1.2-3mdv2009.0
+ Revision: 255348
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Nov 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.2-1mdv2008.1
+ Revision: 113404
- update to new version 0.1.2

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-1mdv2008.0
+ Revision: 46769
- import perl-Audio-MPD-Common



