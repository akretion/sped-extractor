#!/usr/bin/env bash

download() {
echo "downloading ECD pdf Dezembro 2019"
wget http://sped.rfb.gov.br/estatico/2A/D6DD917199D4DE9B01C0D406778DA7A8E2E05D/Manual_de_Orienta%c3%a7%c3%a3o_da_ECD_2019_Dezembro_Leiaute_8.pdf -O ../specs/ecd.pdf
mkdir -p "../specs/ecd"

echo "downloading ECF pdf Dezembro 2019"
wget http://sped.rfb.gov.br/estatico/06/0372A38AD8F1D2AAEA6B65FF02E2BE7624A30C/Manual_de_Orienta%c3%a7%c3%a3o_da_ECF_Dezembro_2019.pdf -O ../specs/ecf.pdf
mkdir -p "../specs/ecf"

echo "downloading EFD Contribuições pdf Dezembro 2019"
wget http://sped.rfb.gov.br/estatico/21/752D4028C877B5B71F3B1A850C32317A36B5AC/Guia_Pratico_EFD_Contribuicoes_Versao_1_33%20-%2016_12_2019.pdf -O ../specs/efd_pis_cofins.pdf
mkdir -p "../specs/efd_pis_cofins"

echo "downloading EFD ICMS IPI pdf Outubro 2019"
# Link found at http://sped.rfb.gov.br/pasta/show/1573
wget http://sped.rfb.gov.br/estatico/0D/434EFF065B893AB70D59AD102A946DC9237680/2019.05.21_GUIA%20PR%c3%81TICO%20DA%20EFD%20-%20Vers%c3%a3o%203.0.3%20-%20v3%20para%20publica%c3%a7%c3%a3o.pdf -O ../specs/efd_icms_ipi.pdf
mkdir -p "../specs/efd_icms_ipi"

#FCI
# https://portal.fazenda.sp.gov.br/servicos/fci/Downloads/Manual_FCI_1.0.8.pdf
}

download
