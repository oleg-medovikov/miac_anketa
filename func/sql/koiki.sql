SELECT 
	d.departName,
	b.bedProfile,
	'' as 'DateBegin',
	b.bedCount
FROM (
	SELECT *
	  FROM [FRMR2].[dbo].[DepartHospitalSubdivisionBeds]
	  where moOid = '__OID__' ) AS b
inner join [FRMR2].[dbo].[Departs] as d
	on (b.departOid = d.oid)
order by d.departName
