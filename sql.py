sql = """
SELECT 
	PEI.EMPRESA,
	PEI.REVENDA,
	TO_CHAR(PEI.ANO)||(CASE 
		WHEN PEI.MES <=9 THEN '0'||TO_CHAR(PEI.MES)
		ELSE TO_CHAR(PEI.MES)
	END)ANOMES,
	TO_DATE(('01'||'/'||(CASE WHEN PEI.MES <=9 THEN '0'||TO_CHAR(PEI.MES) ELSE TO_CHAR(PEI.MES)END)||'/'||TO_CHAR(PEI.ANO)),'dd/mm/yyyy')DAATA,
	PEI.ITEM_ESTOQUE,
	PIE.ITEM_ESTOQUE_PUB,
	PIE.DES_ITEM_ESTOQUE,
	PIE.MARCA,
	PIE.GRUPO,
	PIE.CATEGORIA,
	PC.DES_CATEGORIA,
	PC.IDENTIFICACAO,
	PIE.UTILIZACAO_ITEM,
	PIRE.DIAS_S_MOV AS DIAS_SEM_MOVIMENTO,
	PIRE.DIAS_MOVIMENTO_INICIAL,
	PIRE.DTA_ULT_ENTRADA,
	PEI.VAL_ESTOQUE,
	PEI.QTD_CONTABIL,
	(CASE WHEN PEI.QTD_CONTABIL > 0 THEN CAST((PEI.VAL_ESTOQUE/PEI.QTD_CONTABIL)AS NUMERIC (13,2)) ELSE 0 END)CUSTO_MEDIO,
	PEI.QTD_PEDIDA,
	PEI.QTD_RES_OFICINA,
	PEI.QTD_NEGOCIACAO,
	PEI.QTD_ALOCADA,
	PEI.QTD_ORCADA,
	PEI.QTD_LITIGIO, 
	PEI.QTD_TRANSITO,
	PEI.QTD_TERCEIROS, 
	PEI.ORDEM_TRANSACAO,
	PEI.BASE_ICMS_RETIDO,
	PEI.QTD_CONFERENCIA, 
	PEI.QTD_COMPROMETIDA,
	PEI.PRECO_CUSTO,
	PEI.PRECO_PUBLICO,
	PEI.VAL_ESTOQUE_SEM_ICMSRET, --VAL ESTOQUE SEM ICMS RETIDO 
	PEI.VAL_ICMS_RETIDO,
	PDH.DEMANDABALCAO,
	PDH.DEMANDAOFICINA,
	PDH.DEMANDATELEMARK,
	PDH.OCORRENCIAVENDAS,
	PDH.CLASS_ABC,
	PDH.CLASS_XYZ,
	PDH.TAXA_ESGOTAMENTO 
FROM PEC_ESTOQUEINICIAL PEI
LEFT JOIN PEC_DEMANDA_HISTORICA PDH ON
	PDH.EMPRESA = PEI.EMPRESA AND PDH.REVENDA = PEI.REVENDA 
    AND PDH.ANO = PEI.ANO
    AND PDH.MES = PEI.MES
    AND PDH.ITEM_ESTOQUE = PEI.ITEM_ESTOQUE 
LEFT JOIN PEC_ITEM_ESTOQUE PIE
	ON PIE.EMPRESA = PEI.EMPRESA
    AND PIE.ITEM_ESTOQUE = PEI.ITEM_ESTOQUE  
LEFT JOIN PEC_CATEGORIA PC
	ON PC.EMPRESA = PIE.EMPRESA
    AND PC.CATEGORIA = PIE.CATEGORIA 
LEFT JOIN (
    SELECT PIR.EMPRESA,
    PIR.REVENDA,
    PIR.ITEM_ESTOQUE,
    PIR.DTA_SAIDA,
    PIR.DTA_ULT_ENTRADA,
    CAST(
        ( SYSDATE - PIR.DTA_SAIDA )AS NUMERIC(10)
    )dias_s_mov
	, CAST(( SYSDATE - PIR.DTA_ULT_ENTRADA )AS NUMERIC(10))DIAS_MOVIMENTO_INICIAL
	from PEC_ITEM_REVENDA PIR WHERE PIR.EMPRESA = 2
)PIRE
	ON PIRE.EMPRESA = PEI.EMPRESA
    AND PIRE.REVENDA = PEI.REVENDA 
	AND PIRE.ITEM_ESTOQUE = PEI.ITEM_ESTOQUE 
WHERE PEI.EMPRESA = 2
AND PEI.ANO >=2023
AND rownum <= 10
"""
