# Conditional build:
# --without	aa
# --without	lirc

Summary:	A Free Video Player
Summary(pl.UTF-8):   Odtwarzacz video
Summary(ko.UTF-8):   공개 동영상 플레이어
Name:		xine-ui
Version:	0.9.8
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://xine.sourceforge.net/files/%{name}-%{version}.tar.gz
Source1:	xine.desktop
Source2:	xine_logo.png
Patch0:		%{name}-DESTDIR.patch
URL:		http://xine.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	sed
BuildRequires:	xine-lib-devel >= %{version}
%{!?_without_aa:BuildRequires:		aalib-devel}
%{!?_without_aa:BuildRequires:		aalib-progs}
%{!?_without_aa:BuildRequires:		slang-devel}
%{!?_without_aa:BuildRequires:		gpm-devel}
%{!?_without_lirc:BuildRequires:	lirc-devel}
BuildRequires:	libpng-devel
Obsoletes:	xine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_abindir	/usr/bin

%description
xine is a free gpl-licensed video player for unix-like systems. We
support mpeg-2 and mpeg-1 system (audio + video multiplexed) streams,
eventually mpeg-4 and other formats might be added.

xine plays the video and audio data of mpeg-2 videos and synchronizes
the playback of both. Depending on the properties of the mpeg stream,
playback will need more or less processor power, 100% frame rate has
been seen on a 400 MHz P II system.

%description -l fr.UTF-8
xine est un lecteur vidéo libre sous license GPL pour les systèmes de
type unix. Nous supportons les flux mpeg-2 et mpeg-1 (audio + vidéo
multiplexés), éventuellement le mpeg-4 et d'autres formats peuvent
êtres ajoutés.

xine joue les données vidéo et audio de vidéo mpeg-2 et synchronise la
lecture des deux. En fonction des propriétes du flux mpeg, la lecture
aura besoin de plus ou moins de puissance du processeur, 100% de
restitution de trame a été vus sur un système PII 400MHz.

%description -l ko.UTF-8
xine 는 GPL라이선스를 따르는 UNIX용 공개 동영상 플레이어입니다. 이
플레이어는 mpeg-2 와 mpeg 1 스트림을 지원하며, 현재는 지원하지 않지만
나중에는 mpeg-4 와 다른 형식의 동영상도 지원할 예정입니다.

%description -l pl.UTF-8
xine jest wolnodostępnym odtwarzaczem filmów dla systemów uniksowych.
Obsługuje strumienie MPEG-2 i MPEG-1 (przeplatany dźwięk i obraz),
może być dodana obsługa MPEG-4 i innych formatów.

%package aa
Summary:	XINE - Ascii Art player
Summary(pl.UTF-8):   XINE - odtwarzacz Ascii Art
Group:		Applications/Graphics
Requires:	xine-lib-aa >= %{version}

%description aa
Video player using Ascii Art library.

%description aa -l pl.UTF-8
Odtwarzacz filmów używający biblioteki Ascii Art.

%prep
%setup -q -n xine-ui-%{version}
%patch0 -p1

%build
aclocal
autoconf
automake -a -c
autoheader
%configure \
	--disable-orbit \
%{?_without_lirc:	--disable-lirc} \
%{!?_without_lirc:	--enable-lirc}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_applnkdir}/Multimedia,%{_datadir}/xine/skins}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=$RPM_BUILD_ROOT%{_datadir}/doc/xine

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/xine.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xine/skins

%{!?_without_aa:install -d $RPM_BUILD_ROOT%{_abindir}}
%{!?_without_aa:install $RPM_BUILD_ROOT%{_bindir}/aaxine $RPM_BUILD_ROOT%{_abindir}}

gzip -9nf doc/{FAQ,README}* ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{README_en,README.{dxr3,divx4,syncfb,xinerc},FAQ_en}.gz *.gz
%lang(pl) %doc doc/{README,README.dxr3,FAQ}_pl.gz
%lang(it) %doc doc/{README,FAQ}_it.gz
%lang(es) %doc doc/{README,FAQ}_es.gz
%lang(fr) %doc doc/FAQ_fr.gz
%attr(755,root,root) %{_bindir}/xine
%{_datadir}/idl/xine.idl
%{_datadir}/xine/skins
%{_mandir}/man1/*.1*
%lang(fr) %{_mandir}/fr/man1/*.1*
%lang(es) %{_mandir}/es/man1/*.1*
%lang(pl) %{_mandir}/pl/man1/*.1*
%{_applnkdir}/Multimedia/xine.desktop

%{!?_without_aa:%files aa}
%{!?_without_aa:%defattr(644,root,root,755)}
%{!?_without_aa:%attr(755,root,root) %{_abindir}/aaxine}
