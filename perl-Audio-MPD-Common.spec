%define upstream_name	 Audio-MPD-Common
%define upstream_version 2.002
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A bunch of common helper classes for mpd

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Audio/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(namespace::autoclean)
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
