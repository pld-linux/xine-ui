#
# Conditional build:
%bcond_without	aalib		# without aaxine UI
%bcond_without	caca		# without cacaxine UI
%bcond_without	lirc		# without lirc support
%bcond_without	nvtv		# without nvtv support
%bcond_with	directfb	# with dfbxine UI [disabled in sources at the moment]
%bcond_with	vdr		# with vdr support
#
%ifnarch alpha arm %{ix86} ia64 sh %{x8664}
%undefine	with_nvtv
%endif
%define	xine_ver 1:1.1.0
Summary:	A Free Video Player
Summary(ko.UTF-8):	공개 동영상 플레이어
Summary(pl.UTF-8):	Odtwarzacz video
Summary(pt_BR.UTF-8):	Xine, um player de video
Summary(zh_CN.UTF-8):	一个免费的视频播放器(界面)
Name:		xine-ui
Version:	0.99.5
Release:	4
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/xine/%{name}-%{version}.tar.gz
# Source0-md5:	e643cd1fcad4d98a5ae4eb877ce5087b
Source1:	xine.desktop
Source2:	xine.png
Source3:	xine_logo.png
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-nolibs.patch
Patch2:		%{name}-pl.po.patch
Patch3:		%{name}-curl.patch
Patch4:		install_once.patch
#PatchX:		%{name}-vdr.patch
URL:		http://xine.sourceforge.net/
%{?with_directfb:BuildRequires:	DirectFB-devel >= 0.9.10}
%{?with_aalib:BuildRequires:	aalib-devel >= 1.2.0}
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.8.1
BuildRequires:	bison
BuildRequires:	curl-devel >= 7.10.2
BuildRequires:	gettext-devel
%{?with_caca:BuildRequires:	libcaca-devel >= 0.9}
%{?with_nvtv:BuildRequires:	libnvtvsimple-devel >= 0.4.6}
BuildRequires:	libpng-devel	>= 2:1.4.0
BuildRequires:	libtool
%{?with_lirc:BuildRequires:	lirc-devel}
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel >= 4.2a
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	xine-lib-devel >= %{xine_ver}
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXt-devel
%{!?with_nvtv:BuildConflicts:	libnvtvsimple-devel}
Requires:	xine-lib >= %{xine_ver}
Requires:	xine-plugin-audio >= %{xine_ver}
Obsoletes:	xine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xine is a free gpl-licensed video player for Unix-like systems. We
support mpeg-2 and mpeg-1 system (audio + video multiplexed) streams,
eventually mpeg-4 and other formats might be added.

xine plays the video and audio data of mpeg-2 videos and synchronizes
the playback of both. Depending on the properties of the mpeg stream,
playback will need more or less processor power, 100% frame rate has
been seen on a 400 MHz P II system.

%description -l fr.UTF-8
xine est un lecteur vidéo libre sous license GPL pour les systèmes de
type Unix. Nous supportons les flux mpeg-2 et mpeg-1 (audio + vidéo
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

%description -l pt_BR.UTF-8
O xine é um video player GPL para sistemas unix. Lê arquivos MPEG-2 e
MPEG-1, além de AVIs MS MPEG4 / OpenDivX.

O xine lê o conteúdo vídeo e áudio e sincroniza-os em tempo-real. As
necessidades de processador dependem das propriedades de cada arquivo.

%package aa
Summary:	XINE - Ascii Art player
Summary(pl.UTF-8):	XINE - odtwarzacz Ascii Art
Summary(pt_BR.UTF-8):	XINE - Player em Ascii Art (aalib)
Group:		Applications/Multimedia
Requires:	xine-lib >= %{xine_ver}
Requires:	xine-output-video-aa >= %{xine_ver}
Requires:	xine-plugin-audio >= %{xine_ver}

%description aa
Video player using ASCII Art library.

%description aa -l pl.UTF-8
Odtwarzacz filmów używający biblioteki ASCII Art.

%description aa -l pt_BR.UTF-8
Interface para o xine utilizando aalib (ASCII Art Library).

%package caca
Summary:	XINE - Color ASCII Art player
Summary(pl.UTF-8):	XINE - odtwarzacz kolorowy ASCII Art
Group:		Applications/Multimedia
Requires:	xine-lib >= %{xine_ver}
Requires:	xine-output-video-caca >= %{xine_ver}
Requires:	xine-plugin-audio >= %{xine_ver}

%description caca
Video player using Colour ASCII Art library.

%description caca -l pl.UTF-8
Odtwarzacz filmów używający biblioteki CACA.

%package dfb
Summary:	XINE - player for DirectFB
Summary(pl.UTF-8):	XINE - odtwarzacz dla DirectFB
Group:		Applications/Multimedia
Requires:	xine-lib >= %{xine_ver}
Requires:	xine-output-video-directfb >= %{xine_ver}
Requires:	xine-plugin-audio >= %{xine_ver}

%description dfb
Video player using DirectFB library.

%description dfb -l pl.UTF-8
Odtwarzacz filmów używający biblioteki DirectFB.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%{?with_vdr:%patchX -p1}

%{__sed} -i -e 's/return (int)png_check_sig(buf, 8);/return (int)!png_sig_cmp(buf, 0, 8);/g' src/xitk/Imlib-light/load.c

rm -f po/stamp-po

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%{__autoheader}
%configure \
	--with-ncurses \
%{!?with_lirc:	--disable-lirc} \
%{?with_lirc:	--enable-lirc} \
%{?with_vdr:	--enable-vdr-keys} \
	--with%{!?with_aalib:out}-aalib

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

cp src/xitk/xine-toolkit/README doc/README.xitk
rm -rf $RPM_BUILD_ROOT%{_docdir}/{xine-ui,xitk}

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
%{_datadir}/xine/desktop
%{_datadir}/xine/oxine
%{_datadir}/xine/skins
%{_datadir}/xine/visuals
%{_mandir}/man1/xine*.1*
%lang(de) %{_mandir}/de/man1/xine*.1*
%lang(es) %{_mandir}/es/man1/xine*.1*
%lang(fr) %{_mandir}/fr/man1/xine*.1*
%lang(pl) %{_mandir}/pl/man1/xine*.1*
%{_desktopdir}/xine.desktop
%{_pixmapsdir}/*

%if %{with aalib}
%files aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aaxine
%{_mandir}/man1/aaxine.1*
%lang(de) %{_mandir}/de/man1/aaxine.1*
%lang(pl) %{_mandir}/pl/man1/aaxine.1*
%endif

%if %{with caca}
%files caca
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cacaxine
%endif

%if %{with directfb}
%files dfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dfbxine
%endif
