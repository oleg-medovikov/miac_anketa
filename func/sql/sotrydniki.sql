SELECT DISTINCT
	p.oid,
    UPPER(LEFT(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(p.lastName, '5', 'о'), '6', 'г'), '7', 'в'), '8', 'б'), '9', 'а'), 1)) 
    + LOWER(SUBSTRING(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(p.lastName, '5', 'о'), '6', 'г'), '7', 'в'), '8', 'б'), '9', 'а'), 2, 8000)) 
    + ' ' 
    + UPPER(LEFT(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(p.firstName, '5', 'о'), '6', 'г'), '7', 'в'), '8', 'б'), '9', 'а'), 1)) 
    + LOWER(SUBSTRING(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(p.firstName, '5', 'о'), '6', 'г'), '7', 'в'), '8', 'б'), '9', 'а'), 2, 8000)) 
    + ' ' 
    + UPPER(LEFT(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(p.patronymic, '5', 'о'), '6', 'г'), '7', 'в'), '8', 'б'), '9', 'а'), 1)) 
    + LOWER(SUBSTRING(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(p.patronymic, '5', 'о'), '6', 'г'), '7', 'в'), '8', 'б'), '9', 'а'), 2, 8000)) AS fio,
	CONVERT(varchar, p.birthdate, 104) AS birthDate,
	p.snils,
    c.nrPmuDepartName,
    c.fedPosition,
	c.fedPositionId,
    CONVERT(VARCHAR, c.beginDate, 104) AS beginDate,
    CONVERT(VARCHAR, c.endDate, 104) AS endDate,
    STUFF((
        SELECT DISTINCT ', ' + cert.specName 
        FROM FRMR2.dbo.Certs cert 
        WHERE cert.mrOid = c.mrOid 
        FOR XML PATH('')
    ), 1, 2, '') AS specNames,
    c.nrPmuDepartId,
    nsi.Id
FROM FRMR2.dbo.Cards c
INNER JOIN FRMR2.dbo.Persons p ON p.oid = c.mrOid
LEFT JOIN NsiBase.Regiz.MedOrganizations nsi ON c.nrPmuDepartId = nsi.DepartOid
WHERE c.oid = '__OID__'
    AND (c.endDate IS NULL OR c.endDate > GETDATE())
ORDER BY c.nrPmuDepartName, c.fedPosition;
