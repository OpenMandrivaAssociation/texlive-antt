%global tl_name antt
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.08
Release:	%{tl_revision}.1
Summary:	Antykwa Torunska: a Type 1 family of a Polish traditional type
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/antt
License:	gfsl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/antt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/antt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Antykwa Torunska is a serif font designed by the late Polish typographer
Zygfryd Gardzielewski, reconstructed and digitized as Type 1.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/opentype
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/tex/plain
%dir %{_datadir}/texmf-dist/doc/fonts/antt
%dir %{_datadir}/texmf-dist/doc/latex/antt
%dir %{_datadir}/texmf-dist/fonts/afm/public
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/opentype/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/tex/latex/antt
%dir %{_datadir}/texmf-dist/tex/plain/antt
%dir %{_datadir}/texmf-dist/fonts/afm/public/antt
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/antt
%dir %{_datadir}/texmf-dist/fonts/map/dvips/antt
%dir %{_datadir}/texmf-dist/fonts/opentype/public/antt
%dir %{_datadir}/texmf-dist/fonts/tfm/public/antt
%dir %{_datadir}/texmf-dist/fonts/type1/public/antt
%doc %{_datadir}/texmf-dist/doc/fonts/antt/AntykwaTorunska-doc-en-2_03.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/antt/AntykwaTorunska-doc-pl-2_03.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/antt/AntykwaTorunska-doc-src-2_03.zip
%doc %{_datadir}/texmf-dist/doc/fonts/antt/GUST-FONT-NOSOURCE-LICENSE.txt
%doc %{_datadir}/texmf-dist/doc/fonts/antt/MANIFEST.txt
%doc %{_datadir}/texmf-dist/doc/fonts/antt/README
%doc %{_datadir}/texmf-dist/doc/fonts/antt/antt-latex-cyr.tex
%doc %{_datadir}/texmf-dist/doc/fonts/antt/antt-latex-math.tex
%doc %{_datadir}/texmf-dist/doc/fonts/antt/antt-latex-pl.tex
%doc %{_datadir}/texmf-dist/doc/fonts/antt/antt-latex-t2a.tex
%doc %{_datadir}/texmf-dist/doc/fonts/antt/antt-latex-t5.tex
%doc %{_datadir}/texmf-dist/doc/fonts/antt/antt-mathtest.tex
%doc %{_datadir}/texmf-dist/doc/fonts/antt/antt-table.tex
%doc %{_datadir}/texmf-dist/doc/latex/antt/README
%{_datadir}/texmf-dist/fonts/afm/public/antt/anttb.afm
%{_datadir}/texmf-dist/fonts/afm/public/antt/anttbi.afm
%{_datadir}/texmf-dist/fonts/afm/public/antt/anttcb.afm
%{_datadir}/texmf-dist/fonts/afm/public/antt/anttcbi.afm
%{_datadir}/texmf-dist/fonts/afm/public/antt/anttcl.afm
%{_datadir}/texmf-dist/fonts/afm/public/antt/anttcli.afm
%{_datadir}/texmf-dist/fonts/afm/public/antt/anttcm.afm
%{_datadir}/texmf-dist/fonts/afm/public/antt/anttcmi.afm
%{_datadir}/texmf-dist/fonts/afm/public/antt/anttcr.afm
%{_datadir}/texmf-dist/fonts/afm/public/antt/anttcri.afm
%{_datadir}/texmf-dist/fonts/afm/public/antt/anttl.afm
%{_datadir}/texmf-dist/fonts/afm/public/antt/anttli.afm
%{_datadir}/texmf-dist/fonts/afm/public/antt/anttm.afm
%{_datadir}/texmf-dist/fonts/afm/public/antt/anttmi.afm
%{_datadir}/texmf-dist/fonts/afm/public/antt/anttr.afm
%{_datadir}/texmf-dist/fonts/afm/public/antt/anttri.afm
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-cs.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-ec.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-el.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-ex.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-exp.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-greek.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-mi.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-qx.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-rm.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-sy.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-t2a.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-t2b.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-t2c.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-t5.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-texnansi.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-ts1.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/antt-wncy.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/anttcap-cs.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/anttcap-ec.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/anttcap-qx.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/anttcap-t5.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/antt/anttcap-texnansi.enc
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-cs.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-ec.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-el.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-ex.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-exp.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-greek.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-mi.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-qx.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-rm.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-sy.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-t2a.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-t2b.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-t2c.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-t5.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-texnansi.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-ts1.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt-wncy.map
%{_datadir}/texmf-dist/fonts/map/dvips/antt/antt.map
%{_datadir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunska-Bold.otf
%{_datadir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunska-BoldItalic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunska-Italic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunska-Regular.otf
%{_datadir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCond-Bold.otf
%{_datadir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCond-BoldItalic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCond-Italic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCond-Regular.otf
%{_datadir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCondLight-Italic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCondLight-Regular.otf
%{_datadir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCondMed-Italic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCondMed-Regular.otf
%{_datadir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaLight-Italic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaLight-Regular.otf
%{_datadir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaMed-Italic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaMed-Regular.otf
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttbcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttbicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttcb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttcbcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttcbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttcbicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttcl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttclcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttcli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttclicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttcm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttcmcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttcmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttcmicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttcr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttcrcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttcri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttcricap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttlcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttlicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttmcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttmicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttrcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/cs-anttricap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttbcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttbicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttcb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttcbcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttcbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttcbicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttcl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttclcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttcli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttclicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttcm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttcmcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttcmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttcmicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttcr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttcrcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttcri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttcricap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttlcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttlicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttmcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttmicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttrcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ec-anttricap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/el-anttb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/el-anttbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/el-anttcb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/el-anttcbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/el-anttcl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/el-anttcli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/el-anttcm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/el-anttcmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/el-anttcr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/el-anttcri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/el-anttl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/el-anttli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/el-anttm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/el-anttmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/el-anttr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/el-anttri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ex-anttb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ex-anttcb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ex-anttcl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ex-anttcm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ex-anttcr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ex-anttl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ex-anttm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ex-anttr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/exp-anttb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/exp-anttbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/exp-anttcb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/exp-anttcbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/exp-anttcl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/exp-anttcli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/exp-anttcm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/exp-anttcmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/exp-anttcr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/exp-anttcri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/exp-anttl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/exp-anttli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/exp-anttm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/exp-anttmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/exp-anttr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/exp-anttri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/greek-anttb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/greek-anttbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/greek-anttcb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/greek-anttcbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/greek-anttcl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/greek-anttcli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/greek-anttcm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/greek-anttcmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/greek-anttcr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/greek-anttcri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/greek-anttl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/greek-anttli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/greek-anttm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/greek-anttmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/greek-anttr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/greek-anttri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/mi-anttbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/mi-anttcbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/mi-anttcli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/mi-anttcmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/mi-anttcri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/mi-anttli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/mi-anttmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/mi-anttri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttbcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttbicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttcb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttcbcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttcbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttcbicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttcl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttclcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttcli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttclicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttcm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttcmcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttcmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttcmicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttcr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttcrcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttcri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttcricap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttlcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttlicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttmcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttmicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttrcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/qx-anttricap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/rm-anttb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/rm-anttbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/rm-anttcb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/rm-anttcbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/rm-anttcl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/rm-anttcli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/rm-anttcm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/rm-anttcmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/rm-anttcr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/rm-anttcri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/rm-anttl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/rm-anttli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/rm-anttm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/rm-anttmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/rm-anttr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/rm-anttri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/sy-anttbz.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/sy-anttcbz.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/sy-anttclz.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/sy-anttcmz.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/sy-anttcrz.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/sy-anttlz.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/sy-anttmz.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/sy-anttrz.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2a-anttb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2a-anttbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2a-anttcb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2a-anttcbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2a-anttcl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2a-anttcli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2a-anttcm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2a-anttcmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2a-anttcr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2a-anttcri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2a-anttl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2a-anttli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2a-anttm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2a-anttmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2a-anttr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2a-anttri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2b-anttb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2b-anttbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2b-anttcb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2b-anttcbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2b-anttcl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2b-anttcli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2b-anttcm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2b-anttcmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2b-anttcr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2b-anttcri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2b-anttl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2b-anttli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2b-anttm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2b-anttmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2b-anttr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2b-anttri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2c-anttb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2c-anttbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2c-anttcb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2c-anttcbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2c-anttcl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2c-anttcli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2c-anttcm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2c-anttcmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2c-anttcr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2c-anttcri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2c-anttl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2c-anttli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2c-anttm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2c-anttmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2c-anttr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t2c-anttri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttbcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttbicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttcb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttcbcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttcbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttcbicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttcl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttclcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttcli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttclicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttcm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttcmcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttcmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttcmicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttcr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttcrcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttcri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttcricap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttlcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttlicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttmcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttmicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttrcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/t5-anttricap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttbcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttbicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcbcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcbicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttclcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttclicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcmcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcmicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcrcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcricap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttlcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttlicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttmcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttmicap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttrcap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttricap.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ts1-anttb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ts1-anttbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ts1-anttcb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ts1-anttcbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ts1-anttcl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ts1-anttcli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ts1-anttcm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ts1-anttcmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ts1-anttcr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ts1-anttcri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ts1-anttl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ts1-anttli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ts1-anttm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ts1-anttmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ts1-anttr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/ts1-anttri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/wncy-anttb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/wncy-anttbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/wncy-anttcb.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/wncy-anttcbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/wncy-anttcl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/wncy-anttcli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/wncy-anttcm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/wncy-anttcmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/wncy-anttcr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/wncy-anttcri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/wncy-anttl.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/wncy-anttli.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/wncy-anttm.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/wncy-anttmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/wncy-anttr.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/antt/wncy-anttri.tfm
%{_datadir}/texmf-dist/fonts/type1/public/antt/anttb.pfb
%{_datadir}/texmf-dist/fonts/type1/public/antt/anttbi.pfb
%{_datadir}/texmf-dist/fonts/type1/public/antt/anttcb.pfb
%{_datadir}/texmf-dist/fonts/type1/public/antt/anttcbi.pfb
%{_datadir}/texmf-dist/fonts/type1/public/antt/anttcl.pfb
%{_datadir}/texmf-dist/fonts/type1/public/antt/anttcli.pfb
%{_datadir}/texmf-dist/fonts/type1/public/antt/anttcm.pfb
%{_datadir}/texmf-dist/fonts/type1/public/antt/anttcmi.pfb
%{_datadir}/texmf-dist/fonts/type1/public/antt/anttcr.pfb
%{_datadir}/texmf-dist/fonts/type1/public/antt/anttcri.pfb
%{_datadir}/texmf-dist/fonts/type1/public/antt/anttl.pfb
%{_datadir}/texmf-dist/fonts/type1/public/antt/anttli.pfb
%{_datadir}/texmf-dist/fonts/type1/public/antt/anttm.pfb
%{_datadir}/texmf-dist/fonts/type1/public/antt/anttmi.pfb
%{_datadir}/texmf-dist/fonts/type1/public/antt/anttr.pfb
%{_datadir}/texmf-dist/fonts/type1/public/antt/anttri.pfb
%{_datadir}/texmf-dist/tex/latex/antt/anttor.sty
%{_datadir}/texmf-dist/tex/latex/antt/antyktor.sty
%{_datadir}/texmf-dist/tex/latex/antt/il2antt.fd
%{_datadir}/texmf-dist/tex/latex/antt/il2anttc.fd
%{_datadir}/texmf-dist/tex/latex/antt/il2anttl.fd
%{_datadir}/texmf-dist/tex/latex/antt/il2anttlc.fd
%{_datadir}/texmf-dist/tex/latex/antt/ly1antt.fd
%{_datadir}/texmf-dist/tex/latex/antt/ly1anttc.fd
%{_datadir}/texmf-dist/tex/latex/antt/ly1anttl.fd
%{_datadir}/texmf-dist/tex/latex/antt/ly1anttlc.fd
%{_datadir}/texmf-dist/tex/latex/antt/omlantt.fd
%{_datadir}/texmf-dist/tex/latex/antt/omlanttc.fd
%{_datadir}/texmf-dist/tex/latex/antt/omlanttl.fd
%{_datadir}/texmf-dist/tex/latex/antt/omlanttlc.fd
%{_datadir}/texmf-dist/tex/latex/antt/omsantt.fd
%{_datadir}/texmf-dist/tex/latex/antt/omsanttc.fd
%{_datadir}/texmf-dist/tex/latex/antt/omsanttl.fd
%{_datadir}/texmf-dist/tex/latex/antt/omsanttlc.fd
%{_datadir}/texmf-dist/tex/latex/antt/omxantt.fd
%{_datadir}/texmf-dist/tex/latex/antt/omxanttc.fd
%{_datadir}/texmf-dist/tex/latex/antt/omxanttl.fd
%{_datadir}/texmf-dist/tex/latex/antt/omxanttlc.fd
%{_datadir}/texmf-dist/tex/latex/antt/ot1antt.fd
%{_datadir}/texmf-dist/tex/latex/antt/ot1anttc.fd
%{_datadir}/texmf-dist/tex/latex/antt/ot1anttcm.fd
%{_datadir}/texmf-dist/tex/latex/antt/ot1anttl.fd
%{_datadir}/texmf-dist/tex/latex/antt/ot1anttlc.fd
%{_datadir}/texmf-dist/tex/latex/antt/ot1anttlcm.fd
%{_datadir}/texmf-dist/tex/latex/antt/ot1anttlm.fd
%{_datadir}/texmf-dist/tex/latex/antt/ot1anttm.fd
%{_datadir}/texmf-dist/tex/latex/antt/ot2antt.fd
%{_datadir}/texmf-dist/tex/latex/antt/ot2anttc.fd
%{_datadir}/texmf-dist/tex/latex/antt/ot2anttl.fd
%{_datadir}/texmf-dist/tex/latex/antt/ot2anttlc.fd
%{_datadir}/texmf-dist/tex/latex/antt/ot4antt.fd
%{_datadir}/texmf-dist/tex/latex/antt/ot4anttc.fd
%{_datadir}/texmf-dist/tex/latex/antt/ot4anttl.fd
%{_datadir}/texmf-dist/tex/latex/antt/ot4anttlc.fd
%{_datadir}/texmf-dist/tex/latex/antt/qxantt.fd
%{_datadir}/texmf-dist/tex/latex/antt/qxanttc.fd
%{_datadir}/texmf-dist/tex/latex/antt/qxanttl.fd
%{_datadir}/texmf-dist/tex/latex/antt/qxanttlc.fd
%{_datadir}/texmf-dist/tex/latex/antt/t1antt.fd
%{_datadir}/texmf-dist/tex/latex/antt/t1anttc.fd
%{_datadir}/texmf-dist/tex/latex/antt/t1anttl.fd
%{_datadir}/texmf-dist/tex/latex/antt/t1anttlc.fd
%{_datadir}/texmf-dist/tex/latex/antt/t2aantt.fd
%{_datadir}/texmf-dist/tex/latex/antt/t2aanttc.fd
%{_datadir}/texmf-dist/tex/latex/antt/t2aanttl.fd
%{_datadir}/texmf-dist/tex/latex/antt/t2aanttlc.fd
%{_datadir}/texmf-dist/tex/latex/antt/t2bantt.fd
%{_datadir}/texmf-dist/tex/latex/antt/t2banttc.fd
%{_datadir}/texmf-dist/tex/latex/antt/t2banttl.fd
%{_datadir}/texmf-dist/tex/latex/antt/t2banttlc.fd
%{_datadir}/texmf-dist/tex/latex/antt/t2cantt.fd
%{_datadir}/texmf-dist/tex/latex/antt/t2canttc.fd
%{_datadir}/texmf-dist/tex/latex/antt/t2canttl.fd
%{_datadir}/texmf-dist/tex/latex/antt/t2canttlc.fd
%{_datadir}/texmf-dist/tex/latex/antt/t5antt.fd
%{_datadir}/texmf-dist/tex/latex/antt/t5anttc.fd
%{_datadir}/texmf-dist/tex/latex/antt/t5anttl.fd
%{_datadir}/texmf-dist/tex/latex/antt/t5anttlc.fd
%{_datadir}/texmf-dist/tex/latex/antt/ts1antt.fd
%{_datadir}/texmf-dist/tex/latex/antt/ts1anttc.fd
%{_datadir}/texmf-dist/tex/latex/antt/ts1anttl.fd
%{_datadir}/texmf-dist/tex/latex/antt/ts1anttlc.fd
%{_datadir}/texmf-dist/tex/plain/antt/antt-math.tex
