USE CUSTOMER_DB;

DELIMITER $$
CREATE PROCEDURE `ADDTWONUBERS`( IN `n1` INT, IN `n2` INT, OUT `res` INT)
BEGIN
Set res = n1 + n2;
END$$
DELIMITER ;

Call ADDTWONUBERS(2,3,@result);
SELECT @result;