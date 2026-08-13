%global tl_name antt
%global tl_revision 77682
%global tl_version 2.08

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Antykwa Torunska: a Type 1 family of a Polish traditional type
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/antt
License:	gfsl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/antt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/antt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Antykwa Torunska is a serif font designed by the late Polish typographer
Zygfryd Gardzielewski, reconstructed and digitized as Type 1.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from antt:
Map antt.map
TL_DROPIN_EOF
