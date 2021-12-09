-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: students
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `danhsach`
--

DROP TABLE IF EXISTS `danhsach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `danhsach` (
  `MaHS` text NOT NULL,
  `Ho` text,
  `Ten` text,
  `Phai` tinyint(1) DEFAULT NULL,
  `NgaySinh` date DEFAULT NULL,
  `MaTruong` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `danhsach`
--

LOCK TABLES `danhsach` WRITE;
/*!40000 ALTER TABLE `danhsach` DISABLE KEYS */;
INSERT INTO `danhsach` VALUES ('0001','Nguyen Viet','Hong',0,'1983-04-04','LHP'),('0002','Tran Van','Minh',0,'1984-04-17','LHP'),('0008','Tran Thanh','Phong',0,'1983-03-21','LHP'),('0013','Nguyen Minh','Quang',0,'1984-07-10','LHP'),('0014','Trang Phi','Hung',0,'1984-11-02','LHP'),('0019','Nguyen Kim','Toan',1,'1984-07-07','LHP'),('0026','Doan Duc','Chi',0,'1983-10-25','LHP'),('0037','Tran','Khiem',0,'1983-12-04','LHP'),('0038','Le Bich','Phuong',1,'1983-07-24','LHP'),('0043','Pham Hoai','Bong',0,'1982-10-11','LHP'),('0044','Vu Thi My','Linh',1,'1983-06-22','LHP'),('0049','Ma Thi Hong','Xuan',1,'1983-10-19','LHP'),('0053','Luong Khai','Truyen',0,'1983-12-10','NTH'),('0054','Do Van','Thanh',0,'1983-11-08','NTH'),('0059','Nguyen Thanh','Thu',0,'1984-05-09','NTH'),('0060','Nguyen Truong','Son',0,'1984-08-05','NTH'),('0136','Huynh Kim','Ngan',1,'1983-12-22','NTMK'),('0142','Nguyen Thu','Nga',1,'1984-03-02','NTMK'),('0149','Nguyen Chi','My',0,'1984-07-19','NTMK'),('0153','Ha Son','Tri',0,'1983-08-27','NTMK'),('0160','Dinh Minh','Hien',1,'1983-10-31','NTMK'),('0161','Nguyen Thi','Tam',1,'1984-02-19','NTMK'),('0183','Nguyen Thi','Tuyet',1,'1983-12-20','NTMK'),('0190','Tran My','Dung',1,'1984-01-12','NTMK'),('0191','Ngo Thi','Mai',1,'1983-08-29','NTMK'),('0198','Truong Minh','Thang',0,'1984-02-26','BTK'),('0203','Le Kim','Thoa',1,'1984-04-01','BTK'),('0204','Huynh Thanh','Danh',0,'1982-12-07','BTK'),('0209','Tran Thi','Loan',1,'1983-11-25','BTK'),('0210','Huynh Thi','Cua',1,'1983-09-02','BTK'),('0211','Nguyen Minh','Hanh',0,'1983-11-15','BTK'),('0215','Tran Thi','Nhi',1,'1984-11-18','BTK'),('0217','Pham Thi','Dao',1,'1983-12-08','BTK'),('0220','Truong Tuong','Lan',0,'1983-02-19','LQD'),('0221','Lam Ngoc','Quan',0,'1983-08-28','LQD'),('0222','Bui Thi','Phuong',1,'1984-02-09','LQD'),('0226','Nguyen Ngoc','Bich',1,'1983-08-26','LQD'),('0227','Vuong Kim','Anh',1,'1984-04-18','LQD'),('0232','NGuyen Thu','Van',1,'1984-09-16','LQD'),('0245','Nguyen Thi','Dung',1,'1984-11-25','LQD'),('0246','Doan Thuy','Trang',1,'1984-11-19','LQD'),('0247','Le Trung','Tinh',0,'1982-12-31','LQD'),('0252','Hoang Van','Hoa',0,'1984-01-10','LQD'),('0253','Ngo Van','Thanh',0,'1982-09-01','LQD'),('0257','Nguyen Van','Tien',0,'1983-10-07','LQD'),('0263','Nguyen Thanh','Van',1,'1983-07-29','LQD'),('0264','Vu Kieu','Oanh',1,'1984-03-09','LQD'),('0265','Ngo Van','Son',0,'1984-07-08','LQD'),('0270','Nguyen Trong','Nghiep',0,'1983-07-20','LQD'),('0271','Dong Van','Khanh',0,'1984-04-22','LQD'),('0358','Duong Thi','Tuoi',1,'1983-12-24','TV'),('0359','Nguyen Thi','Thuy',1,'1984-01-05','TV'),('0365','Nguyen Van','Toai',0,'1983-09-26','TV'),('0370','Nguyen Thi','Hanh',1,'1983-01-19','TV'),('0376','Nguyen Manh','Tien',0,'1983-12-15','LHP'),('0381','Nguyen Van','Tam',0,'1984-07-02','LHP'),('0382','Tran Thuy','Dao',1,'1983-11-17','LHP'),('0399','Phan Kim','Nga',1,'1984-08-24','LHP'),('0405','Chung Thanh','Kim',0,'1983-09-30','LHP'),('0411','Nguyen Van','Dung',0,'1983-12-17','LHP'),('0412','Vo Thanh','Giang',0,'1984-07-10','LHP'),('0417','Nguyen Hong','Nga',1,'1984-03-22','LHP'),('0429','Chau Viet','Luan',0,'1983-09-07','LHP'),('0435','Le Thanh','Tung',0,'1983-10-26','LHP'),('0436','Nguyen Quoc','Phong',0,'1983-01-04','LHP'),('0441','Tran Kieu','Au',0,'1982-12-22','LHP'),('0446','Dinh Thi','Hai',1,'1983-12-19','NTH'),('0451','Huynh My','Le',1,'1984-02-22','NTH'),('0452','Pham Van','Tuan',0,'1984-08-20','NTH'),('0458','Tran Ngoc','Han',1,'1984-08-22','NTH'),('0463','Nguyen Thanh','Hiep',0,'1984-04-11','NTH'),('0464','Nguyen Cong','Quan',0,'1984-10-28','NTH'),('0470','Nguyen Thanh','Tai',0,'1984-07-25','NTH'),('0476','Nguyen Hong','Phi',0,'1984-02-19','NTH'),('0481','Nguyen Tuyet','Mai',1,'1983-03-24','NTH'),('0482','Phu Tyet','Mai',1,'1984-09-15','NTH'),('0487','Le Kim','Loan',1,'1983-11-07','NTH'),('0488','Tran Hong','Yen',1,'1984-06-24','NTH'),('0495','Tran Thi Ngoc','Han',1,'1984-07-26','TV'),('0501','Nguyen T.Ngoc','Lieu',1,'1982-12-29','TV'),('0502','Vo Phong','Tran',0,'1984-06-12','TV'),('0507','Nguyen Cam','Huong',1,'1983-03-02','TV'),('0508','Tran Nhat','Phong',0,'1982-08-05','TV'),('0514','Vuong Quoc','Hoi',0,'1983-03-31','TV'),('0519','Nguyen Ngoc','Suong',1,'1983-09-11','TV'),('0526','Le Hiep','Dinh ',0,'1983-09-01','TV'),('0527','Do Thanh','Lap',0,'1982-12-28','TV'),('0529','Nguyen Van','Dinh ',0,'1983-11-07','NTH'),('0535','Bui Thanh','Tung',0,'1983-09-14','NTH'),('0536','Le Van','Viet',0,'1983-09-09','NTH'),('0541','Nguyen Ngoc','Dung',0,'1983-04-22','NTH'),('0542','Phan Thanh','Hong',0,'1984-10-15','NTH'),('0547','Le Thanh','Nhanh',1,'1983-07-07','NTH'),('0548','Nguyen Be','Nam',1,'1984-08-25','NTH'),('0554','Phan Thi','Thin',0,'1984-11-13','NTH'),('0559','Le Thi Van','Anh',1,'1984-08-21','NTH'),('0560','Nguyen Truc','Ly',1,'1983-11-28','NTH'),('0566','Vo Giai','Phong',0,'1984-04-16','NTH'),('0571','Ho Van','Cau',0,'1984-03-26','NTH'),('0572','Nguyen Thanh','Son',0,'1983-05-12','NTH'),('0577','Le Hung','Vi',0,'1982-05-02','NTH'),('0578','Tran Hoang','Dang',0,'1984-06-12','NTH'),('0682','Dang Minh','Quan',0,'1984-02-17','BTK'),('0683','Le Thanh','Khoa',0,'1983-07-28','BTK'),('0688','Quach Thanh','Hong',0,'1983-06-24','BTK'),('0689','Nguyen Tan','Tai',0,'1983-08-22','BTK'),('0694','Nguyen Hoang','Dam',0,'1982-11-26','BTK'),('0695','Do Thi','Thuy',1,'1984-08-17','BTK'),('0696','Nguyen Van','Son',0,'1983-09-12','BTK'),('0706','Nguyen Thi','Hoa',1,'1983-11-28','BTK'),('0712','Nguyen Van','Thanh',0,'1983-11-13','BTK'),('0713','Bui Van','Thanh',0,'1984-08-12','BTK'),('0718','Dinh Hai','Nam',0,'1982-12-25','BTK'),('0719','Pham Thi','Thom',1,'1984-07-02','BTK'),('0725','Huynh Van','On',0,'1984-04-16','BTK'),('0736','Do Phuong','Nam',0,'1984-01-01','BTK'),('0743','Huynh Phan','Khoi',0,'1983-05-22','BTK'),('0754','Pham Van','Hoang',0,'1984-10-27','BTK'),('0755','Nguyen Thi','Nhung',1,'1983-10-31','BTK'),('0762','Lu Ngoc','Da',0,'1983-12-29','NTMK'),('0763','Nguyen Thi','Lan',1,'1982-11-12','NTMK'),('0764','Nguyen Phuoc','Hai',0,'1983-10-04','NTMK'),('0768','Thang Thi','Sang',1,'1984-02-05','NTMK'),('0769','Nguyen Thi','Dinh ',1,'1983-05-18','NTMK'),('0770','Nguyen Thi','Hong',1,'1983-08-28','NTMK'),('0774','Nguyen Hong','Hoa',1,'1983-12-14','NTMK'),('0780','Tran Van','Minh',0,'1984-07-11','NTMK'),('0798','Nguyen Thanh','Trung',0,'1984-12-07','NTMK'),('0799','Pham Van','Sum',0,'1983-11-02','NTMK'),('0800','Lam Thi Cam','Van',1,'1983-05-02','NTMK'),('0810','Tran Thu','Oanh',1,'1984-02-04','NTMK'),('0818','Vo Thanh','Binh',0,'1984-06-13','NTMK'),('0822','Nguyen Thi','Thao',1,'1983-01-30','NTMK'),('0823','Vo Kim','Yen',1,'1983-12-16','NTMK'),('0829','Tran Van','Son',0,'1983-07-20','NTMK'),('0830','Hua Thanh','Cong',0,'1984-01-31','NTMK'),('0835','Nguyen Van','Hai',0,'1983-05-09','NTMK'),('0836','Tran Van','Chieu',0,'1984-07-02','NTMK'),('0839','Nguyen Thanh','Lam',0,'1984-03-24','LQD'),('0840','Pham Van','Cam',0,'1983-10-06','LQD'),('0841','Nguyen Quang','Dung',0,'1984-05-21','LQD'),('0845','Nguyen Van','Doan',0,'1983-10-15','LQD'),('0846','Le Hong','Phuong',0,'1983-12-16','LQD'),('0852','Pham Hong','Chung',0,'1983-05-19','LQD'),('0865','Cao Van','Trung',0,'1984-12-02','LQD'),('0870','Nguyen Thi','Ha',1,'1984-10-27','LQD'),('0871','Tran Van','Tuan',0,'1983-12-20','LQD'),('0877','Le Phuoc','Hoa',0,'1983-08-11','LQD'),('0881','Dinh Phu','Hung',0,'1983-01-31','LQD'),('0882','Tran Van','Toan',0,'1982-06-30','LQD'),('0887','Tran Le','Nga',1,'1982-11-27','LQD'),('0893','Vo Hong','Tuyet',1,'1983-01-23','TV'),('0898','Nguyen Thi','Huong',1,'1983-04-04','TV'),('0899','Hoang Thi','Loan',1,'1983-02-23','TV'),('0904','Phan My','Thien',0,'1983-12-16','TV'),('0905','Nguyen Thi Thuy','Tien',1,'1983-07-09','TV'),('0911','Tang Thi','Tinh',1,'1983-11-03','TV'),('0917','La Tu','Thanh',0,'1984-07-17','TV'),('0922','Nguyen Duc','Hien',0,'1984-04-19','TV'),('0923','Nguyen Duc','Hong',0,'1984-04-22','TV'),('0928','Nguyen Minh','Nhut',0,'1982-08-09','TV'),('0929','Pham Hung','Phuoc',0,'1983-12-22','TV'),('0936','Nguyen Thi','Diep',1,'1983-06-26','TV');
/*!40000 ALTER TABLE `danhsach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diem`
--

DROP TABLE IF EXISTS `diem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diem` (
  `MaHS` text NOT NULL,
  `Mon` text,
  `Diem` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diem`
--

LOCK TABLES `diem` WRITE;
/*!40000 ALTER TABLE `diem` DISABLE KEYS */;
INSERT INTO `diem` VALUES ('0001','Toan',8.5),('0001','Van',6),('0002','Toan',9),('0002','Van',7.5),('0008','Toan',4),('0008','Van',5),('0013','Toan',8),('0013','Van',5),('0014','Toan',8.5),('0014','Van',6),('0019','Toan',4.5),('0019','Van',4.5),('0020','Toan',10),('0020','Van',8.5),('0026','Toan',4),('0026','Van',6),('0037','Toan',7),('0037','Van',6.5),('0038','Toan',10),('0038','Van',9.5),('0043','Toan',9),('0043','Van',8),('0044','Toan',6),('0044','Van',8),('0049','Toan',4),('0049','Van',4.5),('0053','Toan',4.5),('0053','Van',6),('0054','Toan',4.5),('0054','Van',4.5),('0059','Toan',4.5),('0059','Van',8),('0060','Toan',2.5),('0060','Van',6),('0136','Toan',10),('0136','Van',10),('0142','Toan',5),('0142','Van',9.5),('0149','Toan',4.5),('0149','Van',7.5),('0153','Toan',10),('0153','Van',9),('0160','Toan',1.5),('0160','Van',4),('0161','Toan',6.5),('0161','Van',4),('0183','Toan',8.5),('0183','Van',5),('0190','Toan',6),('0190','Van',4.5),('0191','Toan',6),('0191','Van',7.5),('0198','Toan',4.5),('0198','Van',5.5),('0203','Toan',6.5),('0203','Van',9),('0204','Toan',7.5),('0204','Van',4.5),('0209','Toan',4.5),('0209','Van',4),('0210','Toan',10),('0210','Van',10),('0211','Toan',6),('0211','Van',9),('0215','Toan',5.5),('0215','Van',7),('0217','Toan',7.5),('0217','Van',8.5),('0220','Toan',7),('0220','Van',7.5),('0221','Toan',5.5),('0221','Van',9.5),('0222','Toan',6.5),('0222','Van',8),('0226','Toan',4),('0226','Van',6.5),('0227','Toan',9.5),('0227','Van',7),('0232','Toan',10),('0232','Van',10),('0245','Toan',10),('0245','Van',6),('0246','Toan',8.5),('0246','Van',10),('0247','Toan',4),('0247','Van',5.5),('0252','Toan',7),('0252','Van',6),('0253','Toan',4),('0253','Van',9),('0257','Toan',7.5),('0257','Van',4.5),('0263','Toan',5.5),('0263','Van',10),('0264','Toan',7),('0264','Van',4.5),('0265','Toan',5.5),('0265','Van',4.5),('0270','Toan',4),('0270','Van',9),('0271','Toan',10),('0271','Van',5),('0358','Toan',6.5),('0358','Van',6),('0359','Toan',3),('0359','Van',5.5),('0365','Toan',7.5),('0365','Van',6),('0370','Toan',7),('0370','Van',8.5),('0376','Toan',7.5),('0376','Van',8),('0381','Toan',6.5),('0381','Van',8.5),('0382','Toan',6.5),('0382','Van',8.5),('0399','Toan',6.5),('0399','Van',7),('0405','Toan',7),('0405','Van',7),('0411','Toan',5.5),('0411','Van',5),('0412','Toan',8.5),('0412','Van',7.5),('0417','Toan',7),('0417','Van',6.5),('0429','Toan',7),('0429','Van',7.5),('0435','Toan',6.5),('0435','Van',7.5),('0436','Toan',7.5),('0436','Van',7),('0441','Toan',7.5),('0441','Van',6),('0446','Toan',7.5),('0446','Van',8.5),('0451','Toan',5),('0451','Van',6.5),('0452','Toan',6.5),('0452','Van',6.5),('0458','Toan',9.5),('0458','Van',8),('0463','Toan',6),('0463','Van',5.5),('0464','Toan',6.5),('0464','Van',6.5),('0470','Toan',6),('0470','Van',6),('0476','Toan',8.5),('0476','Van',6),('0481','Toan',8),('0481','Van',6.5),('0482','Toan',6),('0482','Van',5.5),('0487','Toan',10),('0487','Van',9),('0488','Toan',7),('0488','Van',6.5),('0495','Toan',7.5),('0495','Van',9.5),('0501','Toan',6),('0501','Van',5.5),('0502','Toan',7),('0502','Van',7),('0507','Toan',8.5),('0507','Van',5),('0508','Toan',8),('0508','Van',8),('0514','Toan',5.5),('0514','Van',9.5),('0519','Toan',5.5),('0519','Van',5),('0526','Toan',7.5),('0526','Van',6),('0527','Toan',8),('0527','Van',8.5),('0529','Toan',9),('0529','Van',8.5),('0535','Toan',6),('0535','Van',8),('0536','Toan',9),('0536','Van',9),('0541','Toan',7),('0541','Van',9.5),('0542','Toan',6.5),('0542','Van',6.5),('0547','Toan',5),('0547','Van',7.5),('0548','Toan',5.5),('0548','Van',9),('0554','Toan',8),('0554','Van',8),('0559','Toan',8),('0559','Van',6),('0560','Toan',6),('0560','Van',7.5),('0566','Toan',7),('0566','Van',9),('0571','Toan',5.5),('0571','Van',9.5),('0572','Toan',6.5),('0572','Van',9),('0577','Toan',9),('0577','Van',7),('0578','Toan',8),('0578','Van',8.5),('0682','Toan',10),('0682','Van',10),('0683','Toan',6.5),('0683','Van',8),('0688','Toan',9),('0688','Van',9),('0689','Toan',8.5),('0689','Van',9),('0694','Toan',7.5),('0694','Van',8.5),('0695','Toan',9),('0695','Van',5),('0696','Toan',8),('0696','Van',6),('0706','Toan',6.5),('0706','Van',6.5),('0712','Toan',8),('0712','Van',9),('0713','Toan',8.5),('0713','Van',9.5),('0718','Toan',6),('0718','Van',9.5),('0719','Toan',6.5),('0719','Van',5),('0725','Toan',6.5),('0725','Van',7.5),('0736','Toan',8.5),('0736','Van',5),('0743','Toan',5.5),('0743','Van',5),('0754','Toan',9.5),('0754','Van',6),('0755','Toan',6),('0755','Van',8.5),('0762','Toan',8),('0762','Van',8.5),('0763','Toan',8),('0763','Van',7),('0764','Toan',9.5),('0764','Van',9.5),('0768','Toan',5.5),('0768','Van',9),('0769','Toan',6.5),('0769','Van',6.5),('0770','Toan',9.5),('0770','Van',5),('0774','Toan',7.5),('0774','Van',6),('0780','Toan',6),('0780','Van',6.5),('0798','Toan',5.5),('0798','Van',9),('0799','Toan',7),('0799','Van',9.5),('0800','Toan',9),('0800','Van',6.5),('0810','Toan',6),('0810','Van',7),('0818','Toan',9),('0818','Van',9),('0822','Toan',7.5),('0822','Van',7),('0823','Toan',6.5),('0823','Van',5),('0829','Toan',7.5),('0829','Van',8.5),('0830','Toan',8.5),('0830','Van',6.5),('0835','Toan',8.5),('0835','Van',5),('0836','Toan',7),('0836','Van',8),('0839','Toan',8.5),('0839','Van',5),('0840','Toan',8),('0840','Van',8),('0841','Toan',8),('0841','Van',8.5),('0845','Toan',8.5),('0845','Van',6),('0846','Toan',8.5),('0846','Van',9.5),('0852','Toan',9.5),('0852','Van',7.5),('0865','Toan',6),('0865','Van',5),('0870','Toan',8),('0870','Van',7.5),('0871','Toan',5.5),('0871','Van',5.5),('0877','Toan',6),('0877','Van',9),('0881','Toan',6.5),('0881','Van',5.5),('0882','Toan',9.5),('0882','Van',9.5),('0887','Toan',6.5),('0887','Van',5.5),('0893','Toan',9.5),('0893','Van',5.5),('0898','Toan',5.5),('0898','Van',9.5),('0899','Toan',8.5),('0899','Van',9),('0904','Toan',7),('0904','Van',5),('0905','Toan',8),('0905','Van',5.5),('0911','Toan',6),('0911','Van',8),('0917','Toan',7),('0917','Van',6),('0922','Toan',6.5),('0922','Van',9),('0923','Toan',8.5),('0923','Van',6.5),('0928','Toan',7),('0928','Van',7.5),('0929','Toan',7),('0929','Van',5.5),('0936','Toan',7),('0936','Van',5);
/*!40000 ALTER TABLE `diem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `truong`
--

DROP TABLE IF EXISTS `truong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `truong` (
  `MaTruong` text NOT NULL,
  `TenTruong` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `truong`
--

LOCK TABLES `truong` WRITE;
/*!40000 ALTER TABLE `truong` DISABLE KEYS */;
INSERT INTO `truong` VALUES ('LHP','Truong PTTH Chuyen Le Hong Phong'),('LQD','Truong PTTH Le Quy Don'),('NTH','Truong PTTH Nguyen Thuong Hien'),('NTMK','Truong PTTH Nguyen Thi Minh Khai'),('TV','Truong PTTH Truong Vuong');
/*!40000 ALTER TABLE `truong` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-04 22:55:04
