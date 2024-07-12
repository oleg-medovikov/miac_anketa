select a.oid from (
select 1 as  id,  oid FROM [FRMR2].[dbo].[MedOrganizations] where oid = '__OID__'
union
select 2 as id, [nameShort] FROM [FRMR2].[dbo].[MedOrganizations] where oid = '__OID__'
union
select 3 as id, [nameFull] FROM [FRMR2].[dbo].[MedOrganizations] where oid = '__OID__'
union
SELECT 4 as id, region + ' ' + ' ' + prefixStreet + ' ' + streetName + ' дом ' + house FROM [FRMR2].[dbo].[MOAddressesFull] where moOid = '__OID__'
) a
