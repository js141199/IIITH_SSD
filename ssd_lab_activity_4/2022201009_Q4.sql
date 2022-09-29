USE CUSTOMER_DB;
DELIMITER &&

CREATE PROCEDURE `printData`()
BEGIN 
DECLARE is_done INTEGER DEFAULT 0;
DECLARE c_name varchar(100);
DECLARE c_area varchar(100);
DECLARE c_country varchar(100);
DECLARE c_grade varchar(100);
DECLARE printDetails CURSOR FOR 
SELECT CUST_NAME,CUST_CITY,CUST_COUNTRY,GRADE FROM customer where AGENT_CODE LIKE 'A00%';
DECLARE CONTINUE HANDLER FOR NOT FOUND SET is_done=1;
OPEN printDetails;
get_list: LOOP
FETCH printDetails INTO c_name,c_area,c_country,c_grade;
IF is_done = 1 THEN
	LEAVE get_list;
END IF;
SELECT c_name,c_area,c_country,c_grade;
END LOOP get_list;
CLOSE printDetails;

END&&
DELIMITER ;

CALL `printData`();


