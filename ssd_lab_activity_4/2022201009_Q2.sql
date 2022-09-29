USE CUSTOMER_DB;

DELIMITER $$
CREATE PROCEDURE `printcustomers`( IN `cityname` nvarchar(50))
BEGIN
select CUST_NAME from customer where WORKING_AREA = cityname;
END$$
DELIMITER ;

Call printcustomers('Bangalore');
