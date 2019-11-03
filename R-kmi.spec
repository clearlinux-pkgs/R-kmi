#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-kmi
Version  : 0.5.5
Release  : 14
URL      : https://cran.r-project.org/src/contrib/kmi_0.5.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/kmi_0.5.5.tar.gz
Summary  : Kaplan-Meier Multiple Imputation for the Analysis of Cumulative
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-mitools
BuildRequires : R-mitools
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
No detailed description available

%prep
%setup -q -c -n kmi

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571851096

%install
export SOURCE_DATE_EPOCH=1571851096
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library kmi
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library kmi
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library kmi
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc kmi || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/kmi/DESCRIPTION
/usr/lib64/R/library/kmi/INDEX
/usr/lib64/R/library/kmi/Meta/Rd.rds
/usr/lib64/R/library/kmi/Meta/data.rds
/usr/lib64/R/library/kmi/Meta/features.rds
/usr/lib64/R/library/kmi/Meta/hsearch.rds
/usr/lib64/R/library/kmi/Meta/links.rds
/usr/lib64/R/library/kmi/Meta/nsInfo.rds
/usr/lib64/R/library/kmi/Meta/package.rds
/usr/lib64/R/library/kmi/NAMESPACE
/usr/lib64/R/library/kmi/R/kmi
/usr/lib64/R/library/kmi/R/kmi.rdb
/usr/lib64/R/library/kmi/R/kmi.rdx
/usr/lib64/R/library/kmi/data/icu.pneu.rda
/usr/lib64/R/library/kmi/help/AnIndex
/usr/lib64/R/library/kmi/help/aliases.rds
/usr/lib64/R/library/kmi/help/kmi.rdb
/usr/lib64/R/library/kmi/help/kmi.rdx
/usr/lib64/R/library/kmi/help/paths.rds
/usr/lib64/R/library/kmi/html/00Index.html
/usr/lib64/R/library/kmi/html/R.css
/usr/lib64/R/library/kmi/tests/test.kmi.R
/usr/lib64/R/library/kmi/tests/test.kmi.Rout.save
