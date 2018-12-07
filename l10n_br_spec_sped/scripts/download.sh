#!/usr/bin/env bash

download() {
echo "downloading ECD pdf Abril 2018"
wget http://sped.rfb.gov.br/arquivo/download/2417 -O ../specs/ecd.pdf
mkdir -p "../specs/ecd"

echo "downloading ECF pdf Dezembro 2017"
wget http://sped.rfb.gov.br/arquivo/download/2422 -O ../specs/ecf.pdf
mkdir -p "../specs/ecf"

echo "downloading EFD pdf Janeiro 2018"
wget http://sped.rfb.gov.br/arquivo/download/2364 -O ../specs/efd_pis_cofins.pdf
mkdir -p "../specs/efd_pis_cofins"

echo "downloading EFD pdf Janeiro 2018"
wget http://sped.rfb.gov.br/arquivo/download/2322 -O ../specs/efd_icms_ipi.pdf
mkdir -p "../specs/efd_icms_ipi"

#FCI
# https://portal.fazenda.sp.gov.br/servicos/fci/Downloads/Manual_FCI_1.0.8.pdf
}

download
