# Conditional build:
# --without	aa
# --without	lirc
# --with	directfb

Summary:	A Free Video Player
Summary(ko):	°ø°³ µ¿¿µ»ó ÇÃ·¹ÀÌ¾î
Summary(pl):	Odtwarzacz video
Summary(pt_BR):	Xine, um player de video
Name:		xine-ui
Version:	0.9.12
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://xine.sourceforge.net/files/%{name}-%{version}.tar.gz
Source1:	xine.desktop
Source2:	xine.png
Source3:	xine_logo.png
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-dfb.patch
Patch2:		%{name}-ac_am.patch
Patch3:		%{name}-no_corba.patch
URL:		http://xine.sourceforge.net
%{?_with_directfb:BuildRequires:	DirectFB-devel}
%{!?_without_aa:BuildRequires:		aalib-devel}
%{!?_without_aa:BuildRequires:		aalib-progs}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
%{!?_without_lirc:BuildRequires:	lirc-devel}
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	xine-lib-devel >= %{version}
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

%description -l pl
xine jest wolnodostêpnym odtwarzaczem filmów dla systemów uniksowych.
Obs³uguje strumienie MPEG-2 i MPEG-1 (przeplatany d¼wiêk i obraz),
mo¿e byæ dodana obs³uga MPEG-4 i innych formatów.

%description -l pt_BR
O xine é um video player GPL para sistemas unix. Lê arquivos MPEG-2 e
MPEG-1, além de AVIs MS MPEG4 / OpenDivX.

O xine lê o conteúdo vídeo e áudio e sincroniza-os em tempo-real. As
necessidades de processador dependem das propriedades de cada arquivo.

%package aa
Summary:	XINE - Ascii Art player
Summary(pl):	XINE - odtwarzacz Ascii Art
Summary(pt_BR):	XINE - Player em Ascii Art (aalib)
Group:		Applications/Graphics
Requires:	xine-lib-aa >= %{version}

%description aa
Video player using Ascii Art library.

%description aa -l pl
Odtwarzacz filmów u¿ywaj±cy biblioteki Ascii Art.

%description aa -l pt_BR
Interface para o xine utilizando aalib (Ascii Art Library).

%package dfb
Summary:	XINE - player for DirectFB
Summary(pl):	XINE - odtwarzacz dla DirectFB
Group:		Applications/Graphics
Requires:	xine-lib-directfb >= %{version}

%description dfb
Video player using DirectFB library.

%description dfb -l pl
Odtwarzacz filmów u¿ywaj±cy biblioteki DirectFB.

%prep
%setup -q -n xine-ui-%{version}
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
autoheader
%configure \
	--disable-orbit \
	--disable-corba \
%{?_without_lirc:	--disable-lirc} \
%{!?_without_lirc:	--enable-lirc}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Multimedia,%{_pixmapsdir},%{_datadir}/xine/skins}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=$RPM_BUILD_ROOT%{_datadir}/doc/xine

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/xine.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/xine/skins

%{!?_without_aa:install -d $RPM_BUILD_ROOT%{_abindir}}
%{!?_without_aa:install $RPM_BUILD_ROOT%{_bindir}/aaxine $RPM_BUILD_ROOT%{_abindir}}
%{?_with_directfb:install -d $RPM_BUILD_ROOT%{_abindir}}
%{?_with_directfb:install $RPM_BUILD_ROOT%{_bindir}/dfbxine $RPM_BUILD_ROOT%{_abindir}}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/{README_en,README.{config_en,divx4,dxr3,mrl,opengl,syncfb,tvmode},FAQ_en} ChangeLog 
%lang(pl) %doc doc/{README,README.dxr3,FAQ}_pl
%lang(it) %doc doc/{README,FAQ}_it
%lang(es) %doc doc/{README,FAQ}_es
%lang(fr) %doc doc/{README,FAQ}_fr
%lang(de) %doc doc/{README,FAQ}_de
%lang(it) %doc doc/{README,FAQ}_it
%lang(uk) %doc doc/{README,FAQ}_uk
%attr(755,root,root) %{_bindir}/xine
%attr(755,root,root) %{_bindir}/xine-bugreport
%attr(755,root,root) %{_bindir}/xine-check
%{_datadir}/xine/skins/*
%{_mandir}/man1/*.1*
%lang(de) %{_mandir}/de/man1/*.1*
%lang(fr) %{_mandir}/fr/man1/*.1*
%lang(es) %{_mandir}/es/man1/*.1*
%lang(pl) %{_mandir}/pl/man1/*.1*
%{_applnkdir}/Multimedia/xine.desktop
%{_pixmapsdir}/*
# CORBA files 
#%{_datadir}/idl/xine.idl
#%attr(755,root,root) %{_bindir}/xine-remote

%{!?_without_aa:%files aa}
%{!?_without_aa:%defattr(644,root,root,755)}
%{!?_without_aa:%attr(755,root,root) %{_abindir}/aaxine}

%{?_with_directfb:%files dfb}
%{?_with_directfb:%defattr(644,root,root,755)}
%{?_with_directfb:%attr(755,root,root) %{_abindir}/dfbxine}
