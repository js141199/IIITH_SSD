USE COMPANY;
SELECT DISTINCT D.MGR_SSN,D.DNUMBER,COUNT(DEP.RELATIONSHIP) FROM DEPARTMENT D,DEPENDENT DEP WHERE D.MGR_SSN=DEP.ESSN AND D.DNUMBER IN 
(SELECT DNUMBER FROM DEPT_LOCATIONS GROUP BY DNUMBER HAVING COUNT(DLOCATION) >= 2) GROUP BY D.DNUMBER;
