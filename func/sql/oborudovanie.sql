SELECT
	e.equipmentName,
	e.model,
	'' as 'cabinet',
	d.departName,
	e.productDate,
	'' as 'текущие состояние',
	e.inventoryNumber,
	e.serialNumber,
	e.lifeTime,
	e.vendor,
	'' as 'модальность',
	'' as 'тип оборудования',
	'' as 'расходный материал'
FROM (select * FROM [FRMR2].[dbo].[Equipment] 
		where
			moOid = '__OID__'
			and [type] = 'Медицинское оборудование' ) as e
inner join [FRMR2].[dbo].[Departs] as d
	on (e.departId = d.oid)
