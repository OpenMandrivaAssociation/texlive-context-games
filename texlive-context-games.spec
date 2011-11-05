# revision 23167
# category ConTeXt
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-context-games
Version:	20111103
Release:	1
Summary:	TeXLive context-games package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-games.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-games.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context
Requires:	texlive-skaknew
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive context-games package.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post
    %_texmf_mtxrun_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
	%_texmf_mtxrun_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/games/games-go.lua
%{_texmfdistdir}/tex/context/third/games/games-go.tex
%{_texmfdistdir}/tex/context/third/games/games-hex.lua
%{_texmfdistdir}/tex/context/third/games/games-hex.tex
%{_texmfdistdir}/tex/context/third/games/holz280.jpg
%{_texmfdistdir}/tex/context/third/games/t-games.tex
%doc %{_texmfdistdir}/doc/context/third/games/README
%doc %{_texmfdistdir}/doc/context/third/games/games-doc.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
