SELECT distinct p.fio, c.nrPmuDepartName, c.fedPosition, c.postId,
    CONVERT(VARCHAR, c.beginDate, 104) AS beginDate, 
    CONVERT(VARCHAR, c.endDate, 104) AS endDate, 
    s.specNames
  from (select * FROM [FRMR2].[dbo].[Cards]   WHERE oid = '__OID__') as  c
  inner join (SELECT 
      UPPER(LEFT(ISNULL(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE([lastName], '5', 'о'), '6', 'г'), '7', 'в'), '8', 'б'), '9', 'а'), ''), 1)) + 
      LOWER(SUBSTRING(ISNULL(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE([lastName], '5', 'о'), '6', 'г'), '7', 'в'), '8', 'б'), '9', 'а'), ''), 2, LEN(ISNULL([lastName], ''))))
      + ' ' + 
      UPPER(LEFT(ISNULL(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE([firstName], '5', 'о'), '6', 'г'), '7', 'в'), '8', 'б'), '9', 'а'), ''), 1)) + 
      LOWER(SUBSTRING(ISNULL(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE([firstName], '5', 'о'), '6', 'г'), '7', 'в'), '8', 'б'), '9', 'а'), ''), 2, LEN(ISNULL([firstName], ''))))
      + ' ' +
      UPPER(LEFT(ISNULL(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE([patronymic], '5', 'о'), '6', 'г'), '7', 'в'), '8', 'б'), '9', 'а'), ''), 1)) + 
      LOWER(SUBSTRING(ISNULL(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE([patronymic], '5', 'о'), '6', 'г'), '7', 'в'), '8', 'б'), '9', 'а'), ''), 2, LEN(ISNULL([patronymic], '')))) AS fio
	  ,oid
		FROM [FRMR2].[dbo].[Persons]) as p
		on (p.oid = c.mrOid)
	left join(SELECT mrOid, 
					STUFF((SELECT DISTINCT ', ' + specName FROM [FRMR2].[dbo].[Certs] AS innerCerts
						WHERE innerCerts.mrOid = outerCerts.mrOid
						FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 2, '') AS specNames
				FROM [FRMR2].[dbo].[Certs] AS outerCerts
				--WHERE endDate <= getdate()  -- это чтобы отсеять устаревшую специализацию
 				GROUP BY  mrOid
				) as s
		on (c.mrOid = s.mrOid)
  order by c.nrPmuDepartName, c.fedPosition
