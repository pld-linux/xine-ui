#
# Conditional build:
%bcond_without	aalib		# without aaxine UI
%bcond_without	lirc		# without lirc support
%bcond_with	directfb	# with dfbxine UI [disabled in sources at the moment]
#
%define	xine_ver 1:1.0
Summary:	A Free Video Player
Summary(ko):	°ø°³ µ¿¿µ»ó ÇÃ·¹ÀÌ¾î
Summary(pl):	Odtwarzacz video
Summary(pt_BR):	Xine, um player de video
Summary(zh_CN):	Ò»¸öÃâ·ÑµÄÊÓÆµ²¥·ÅÆ÷(½çÃæ)
Name:		xine-ui
Version:	0.9.23
Release:	4
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/xine/%{name}-%{version}.tar.gz
# Source0-md5:	526c96a7c08d2913e6f328e347fe615f
Source1:	xine.desktop
Source2:	xine.png
Source3:	xine_logo.png
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-nolibs.patch
Patch2:		%{name}-system-readline.patch
Patch3:		%{name}-pl.po.patch
Patch4:		%{name}-curl.patch
URL:		http://xine.sourceforge.net/
%{?with_directfb:BuildRequires:	DirectFB-devel >= 0.9.10}
%{?with_aalib:BuildRequires:	aalib-devel >= 1.2.0}
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.8.1
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	libcurl-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
%{?with_lirc:BuildRequires:	lirc-devel}
BuildRequires:	ncurses-devel
#BuildRequires:	nvtv-devel >= 0.4.6	# not released yet
BuildRequires:	pkgconfig
BuildRequires:	readline-devel >= 4.2a
BuildRequires:	xine-lib-devel >= %{xine_ver}
Requires:	xine-lib >= %{xine_ver}
Requires:	xine-plugin-audio >= %{xine_ver}
Obsoletes:	xine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Group:		Applications/Multimedia
Requires:	xine-lib >= %{xine_ver}
Requires:	xine-output-video-aa >= %{xine_ver}
Requires:	xine-plugin-audio >= %{xine_ver}

%description aa
Video player using Ascii Art library.

%description aa -l pl
Odtwarzacz filmów u¿ywaj±cy biblioteki Ascii Art.

%description aa -l pt_BR
Interface para o xine utilizando aalib (Ascii Art Library).

%package dfb
Summary:	XINE - player for DirectFB
Summary(pl):	XINE - odtwarzacz dla DirectFB
Group:		Applications/Multimedia
Requires:	xine-lib >= %{xine_ver}
Requires:	xine-output-video-directfb >= %{xine_ver}
Requires:	xine-plugin-audio >= %{xine_ver}

%description dfb
Video player using DirectFB library.

%description dfb -l pl
Odtwarzacz filmów u¿ywaj±cy biblioteki DirectFB.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%{__autoheader}
%configure \
	--disable-orbit \
	--disable-corba \
%{!?with_lirc:	--disable-lirc} \
%{?with_lirc:	--enable-lirc}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_datadir}/xine/skins}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=$RPM_BUILD_ROOT%{_datadir}/doc/xine

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/xine/skins

mv $RPM_BUILD_ROOT%{_datadir}/locale/{pl_PL,pl}

cp src/xitk/xine-toolkit/README doc/README.xitk

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/{README_en,README.*} ChangeLog
%lang(cs) %doc doc/README_cs
%lang(de) %doc doc/README_de
%lang(es) %doc doc/README_es
%lang(fi) %doc doc/README_fi
%lang(fr) %doc doc/README_fr
%lang(it) %doc doc/README_it
%lang(pl) %doc doc/README_pl
%lang(uk) %doc doc/README_uk
%attr(755,root,root) %{_bindir}/fbxine
%attr(755,root,root) %{_bindir}/xine
%attr(755,root,root) %{_bindir}/xine-bugreport
%attr(755,root,root) %{_bindir}/xine-check
%attr(755,root,root) %{_bindir}/xine-remote
%{_datadir}/xine/skins
%{_datadir}/xine/desktop
%{_datadir}/xine/visuals
%{_mandir}/man1/xine*.1*
%lang(de) %{_mandir}/de/man1/xine*.1*
%lang(es) %{_mandir}/es/man1/xine*.1*
%lang(fr) %{_mandir}/fr/man1/xine*.1*
%lang(pl) %{_mandir}/pl/man1/xine*.1*
%{_desktopdir}/xine.desktop
%{_pixmapsdir}/*
# CORBA files
#%%{_datadir}/idl/xine.idl
#%attr(755,root,root) %{_bindir}/xine-remote

%if %{with aalib}
%files aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aaxine
%{_mandir}/man1/aaxine.1*
%lang(de) %{_mandir}/de/man1/aaxine.1*
%lang(pl) %{_mandir}/pl/man1/aaxine.1*
%endif

%if %{with directfb}
%files dfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dfbxine
%endif
