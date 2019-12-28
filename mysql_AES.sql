update mysql_AES set phone = HEX(AES_ENCRYPT('123','123')) where id=1;

select AES_DECRYPT(UNHEX(phone),'123') as phone from mysql_AES where id = 1;