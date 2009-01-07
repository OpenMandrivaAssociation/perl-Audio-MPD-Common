%define module	Audio-MPD-Common
%define name	perl-%{module}
%define version 0.1.4
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A bunch of common helper classes for mpd
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Audio/%{module}-%{version}.tar.bz2
Buildrequires:	perl(Module::Build)
Buildrequires:	perl(Class::Accessor::Fast)
Buildrequires:	perl(Readonly)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
%{__rm} -rf %{buildroot} 
./Build install destdir=%{buildroot}

%clean 
%{__rm} -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc LICENSE README Changes
%{perl_vendorlib}/Audio
%{_mandir}/man3/*
