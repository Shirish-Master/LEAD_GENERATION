SELECT 
ROID_number, Item_number,Sales_Org_Structure_2021 as branch, L2L_OTHERS,
Finalvertical_Structure_2021 as vertical,
[BU],[INVENTORY],[Pub_Cen],Calendar_Date,CLIENT_GROUP_NAME,BCC,[rate_code],[rate_code_desc] as package,
Size_of_Ad,ISSUE_COMPONENT_DESC,PCC2,
SUM([ZMIC_VAL])/100000 'Rev Internal Allocation-Lacs',
sum([BCCLVALUE_ACTUAL])/100000 'Rev-Lac',
sum([BCCLVOLUME_ACTUAL])/1000 'Vol-Kscm'
FROM [TOI_DASHBOARD_DELTA].[dbo].[DRR_SCHEDULE_FINAL_NEW]
WHERE
(CONVERT(DATETIME, Calendar_Date, 104) >= DATEADD(MONTH, -12, GETDATE())
        AND CONVERT(DATETIME, Calendar_Date, 104) <= GETDATE())
        AND [bu_status] IN ('NOT_STOPPED_BU') 
        AND [print_nonprint] IN ('Print')
        AND [BCCLVOLUME_ACTUAL] > 0.005
        AND [BCCLVALUE_ACTUAL] > 0.00005 
        AND [CLIENT_GROUP_NAME] = '?'

GROUP BY ROID_number, Item_number, Sales_Org_Structure_2021 , L2L_OTHERS,
Finalvertical_Structure_2021,
[BU],[INVENTORY],[Pub_Cen],Calendar_Date,CLIENT_GROUP_NAME,BCC,[rate_code],[rate_code_desc],
Size_of_Ad,ISSUE_COMPONENT_DESC,PCC2
