# Conditional build:
# --without	aa

Summary:	A Free Video Player.
Summary(pl):	Odtwarzacz video
Summary(ko):	°ø°³ µ¿¿µ»ó ÇÃ·¹ÀÌ¾î
Name:		xine-ui
Version:	0.5.0
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://xine.sourceforge.net/files/%{name}-%{version}.tar.gz
Source1:	xine.desktop
Source2:	xine_logo.png
URL:		http://xine.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xine-lib-devel >= 0.5.0
%{!?_without_aa:BuildRequires: aalib-devel}
%{!?_without_aa:BuildRequires: aalib-progs}
BuildRequires:	ORBit-devel
BuildRequires:	libpng-devel
Obsoletes:	xine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man


%description
xine is a free gpl-licensed video player for unix-like systems. We
support mpeg-2 and mpeg-1 system (audio + video multiplexed) streams,
eventually mpeg-4 and other formats might be added.

xine plays the video and audio data of mpeg-2 videos and synchronizes
the playback of both. Depending on the properties of the mpeg stream,
playback will need more or less processor power, 100% frame rate has
been seen on a 400 MHz P II system.

%description -l fr
xine est un lecteur vidéo libre sous license GPL pour les systèmes de
type unix. Nous supportons les flux mpeg-2 et mpeg-1 (audio + vidéo
multiplexés), éventuellement le mpeg-4 et d'autres formats peuvent
êtres ajoutés.

xine joue les données vidéo et audio de vidéo mpeg-2 et synchronise la
lecture des deux. En fonction des propriétes du flux mpeg, la lecture
aura besoin de plus ou moins de puissance du processeur, 100% de
restitution de trame a été vus sur un système PII 400MHz.

%description -l ko
xine ´Â GPL¶óÀÌ¼±½º¸¦ µû¸£´Â UNIX¿ë °ø°³ µ¿¿µ»ó ÇÃ·¹ÀÌ¾îÀÔ´Ï´Ù. ÀÌ
ÇÃ·¹ÀÌ¾î´Â mpeg-2 ¿Í mpeg 1 ½ºÆ®¸²À» Áö¿øÇÏ¸ç, ÇöÀç´Â Áö¿øÇÏÁö ¾ÊÁö¸¸
³ªÁß¿¡´Â mpeg-4 ¿Í ´Ù¸¥ Çü½ÄÀÇ µ¿¿µ»óµµ Áö¿øÇÒ ¿¹Á¤ÀÔ´Ï´Ù.


%package aa
Summary:	XINE - Ascii Art player.
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Group(pt):	Aplicações/Gráficos
Requires:	xine-lib-aa

%description aa
Video player using Ascii Art library.


%prep
%setup -q -n xine-ui-0.5.0

%build
#cp ./configure ./configure.orig
#sed 's/xine_skin_dir=/xine_skin_dir=$RPM_BUILD_ROOT/' configure.orig > ./configure

%configure2_13 \
	--prefix=%{_prefix}
#	--disable-xinetest 
#	--disable-orbittest
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

%{__make} DESTDIR=$RPM_BUILD_ROOT \
          docdir=$RPM_BUILD_ROOT/%{_datadir}/doc/xine \
	  install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/xine.desktop
#cp doc/*.xpm $RPM_BUILD_ROOT/usr/include/X11/pixmaps
install %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/xine/skins

%post
#/sbin/ldconfig
#if test -d /usr/local/share/xine/skins/default; then rm -rf /usr/local/share/xine/skins/default && ln -s /usr/local/share/xine/skins/xinetic /usr/local/share/xine/skins/default; fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# binaries
%attr(755,root,root) %{_bindir}/xine
%{_datadir}/idl/xine.idl
# skins
%{_datadir}/xine/skins/*/*
%{_datadir}/xine/skins/*.png
#/usr/local/share/xine/skins/metal/*
#/usr/local/share/xine/skins/pitt/*
#/usr/local/share/xine/skins/xinetic/*
# documentation
%{_mandir}/fr/man1/xine.1*
%{_mandir}/man1/xine.1*
%{_datadir}/doc/xine/*
%{_applnkdir}/Multimedia/xine.desktop

%{!?_without_aa:%files aa}
%{!?_without_aa:%defattr(644,root,root,755)}
%{!?_without_aa:%attr(755,root,root) %{_bindir}/aaxine}
