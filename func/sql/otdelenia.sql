SELECT distinct
     [nrPmuDepartName], [nrPmuDepartId]
  FROM [FRMR2].[dbo].[Cards]
  where oid = '__OID__'
  order by [nrPmuDepartId]
