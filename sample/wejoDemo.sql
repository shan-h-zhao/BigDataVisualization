/****** wejo example queries  ******/

-- r1. count DE records by postalCode
-- in seconds
SELECT [location.postalCode], count(*) as count
  FROM [Wejo].[dbo].[DE_NewData]
  group by [location.postalCode]
  order by [location.postalCode] ASC

-- r2. count VM records by postalCode
-- 5:15
SELECT [location.postalCode], count(*) as count
  FROM [Wejo].[dbo].[VM_NewData]
  group by [location.postalCode]
  order by [location.postalCode] ASC


-- r3. count VM records by postalCode join with DE records
-- 5:04
WITH 
countDEByPost AS
(SELECT [location.postalCode], count(*) as countDE
  FROM [Wejo].[dbo].[DE_NewData]
  group by [location.postalCode]), 
countVMByPost AS
(SELECT [location.postalCode], count(*) as countVM
  FROM [Wejo].[dbo].[VM_NewData]
  group by [location.postalCode])
SELECT *
FROM countDEByPost FULL OUTER JOIN
countVMByPost
ON countDEByPost.[location.postalCode] = countVMByPost.[location.postalCode]
 

-- r4. query DE in postalCode 
-- least 06160
SELECT *
FROM [Wejo].[dbo].[DE_NewData]
WHERE [location.postalCode] = '06160'

-- r5. query VM in postalCode 
-- least 06160
SELECT *
FROM [Wejo].[dbo].[VM_NewData]
WHERE [location.postalCode] = '06160'

-- r6. query DE in postalCode 
-- most 06010
-- 23 seconds
SELECT *
FROM [Wejo].[dbo].[DE_NewData]
WHERE [location.postalCode] = '06010'

-- r7. query VM in postalCode 
-- most 06010
-- 9:43, 70,574,758 records
SELECT *
FROM [Wejo].[dbo].[VM_NewData]
WHERE [location.postalCode] = '06010'

-- r8. query one day's DE
-- 2021-01-17
-- 11 seconds, 249,014 records
SELECT *
FROM [Wejo].[dbo].[DE_NewData]
WHERE capturedTimestamp like '2021-01-17%'

-- r9. query one day's VM
-- 2021-01-17
-- 7:03, 10,786,121 records
SELECT *
FROM [Wejo].[dbo].[VM_NewData]
WHERE capturedTimestamp like '2021-01-17%'