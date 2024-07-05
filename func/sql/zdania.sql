SELECT
  ROW_NUMBER() OVER (ORDER BY b.buildName) AS RowNum,
	b.buildName,
	a.region + ' ' + a.prefixArea  + ' ' + a.areaName 
	+ ' ' + a.prefixStreet + ' ' + a.streetName 
	+ ' дом ' + a.house + ' ' + a.building as 'adress'
from (select buildName, id
  FROM [FRMR2].dbo.Buildings 
  where moOid = '__OID__') as b
  left join [FRMR2].[dbo].[BuildingAddresses] as a
	on (b.id = a.buildingId)
