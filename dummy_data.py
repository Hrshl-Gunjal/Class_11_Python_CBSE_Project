# importing the required modules
import mysql.connector

# connecting to MySql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin"
)

# making the cursor object
cursor = mydb.cursor()

# creating the database
cursor.execute("CREATE DATABASE IF NOT EXISTS project")
cursor.execute("USE project")

# creating the table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS students"
    "(adm_no INT(4) PRIMARY KEY UNIQUE NOT NULL, "
    "class INT(3) NOT NULL, "
    "roll_no INT(3) NOT NULL, "
    "student_name VARCHAR(30) NOT NULL, "
    "math_marks DOUBLE(40,1) NOT NULL, "
    "phy_marks DOUBLE(40,1) NOT NULL, "
    "chem_marks DOUBLE(40,1) NOT NULL, "
    "eng_marks DOUBLE(40,1) NOT NULL, "
    "comp_marks DOUBLE(40,1) NOT NULL, "
    "total DOUBLE(40,2), "
    "CGPA DOUBLE(40,2))")

# inserting the dummy data 
sql = "INSERT /*! IGNORE */ students (adm_no, class, " \
      "roll_no, student_name, math_marks, phy_marks, " \
      "chem_marks, eng_marks, comp_marks, total, CGPA) " \
      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

val = [(503, 12, 2, 'Oma Lawler', 78.2, 71.7, 54.7, 78.9, 80.0, 363.50, 9.09),
       (504, 10, 9, 'Jerome Gipson', 67.5, 68.9, 50.7, 71.2, 77.4, 335.70, 8.39),
       (505, 10, 14, 'Tamica Goins', 55.8, 66.3, 67.3, 71.7, 73.2, 334.30, 8.36),
       (506, 12, 18, 'Calvin Looney', 56.6, 55.3, 60.1, 70.5, 76.8, 319.30, 7.98),
       (507, 11, 20, 'Adan Pulido', 63.4, 75.2, 54.3, 79.5, 77.2, 349.60, 8.74),
       (508, 12, 24, 'Logan Flannery', 50.1, 66.9, 74.8, 70.5, 74.7, 337.00, 8.43),
       (509, 12, 27, 'Abram Swank', 76.8, 76.1, 67.8, 56.0, 70.8, 347.50, 8.69),
       (510, 11, 30, 'Selina Pfeiffer', 52.6, 66.9, 54.9, 73.4, 70.7, 318.50, 7.96),
       (511, 10, 34, 'Bradford Broderick', 69.3, 50.4, 70.2, 69.4, 79.5, 338.80, 8.47),
       (523, 11, 2, 'Adolph Francisco', 60.9, 67.1, 70.5, 66.6, 71.2, 336.30, 8.41),
       (524, 12, 7, 'Delcie Abney', 56.3, 64.3, 79.1, 63.0, 72.0, 334.70, 8.37),
       (525, 12, 13, 'Newton Graves', 70.3, 70.6, 71.8, 72.0, 75.6, 360.30, 9.01),
       (526, 10, 18, 'Alejandro Espinal', 52.6, 77.3, 52.6, 67.5, 72.2, 322.20, 8.05),
       (527, 12, 19, 'Calvin Abrams', 73.9, 68.0, 61.8, 60.4, 79.5, 343.60, 8.59),
       (528, 12, 21, 'Ronnie Roby', 78.6, 68.5, 53.8, 79.8, 78.9, 359.60, 8.99),
       (529, 11, 26, 'Owen Alston', 58.9, 74.3, 66.8, 56.9, 80.0, 336.90, 8.42),
       (530, 10, 28, 'Elaina Gruber', 53.0, 71.5, 66.8, 71.2, 74.9, 337.40, 8.43),
       (531, 10, 31, 'Hosea Spears', 56.6, 68.4, 77.9, 62.8, 71.3, 337.00, 8.43),
       (552, 12, 3, 'Denisha Mcginnis', 60.2, 53.3, 54.9, 61.3, 78.3, 308.00, 7.70),
       (553, 10, 5, 'Adah Jameson', 60.3, 65.5, 72.0, 69.4, 70.3, 337.50, 8.44),
       (554, 11, 9, 'Lilla Perez', 76.7, 68.4, 62.9, 70.9, 72.0, 350.90, 8.77),
       (555, 11, 10, 'Curtis Hutson', 60.3, 76.8, 50.2, 51.9, 77.7, 316.90, 7.92),
       (556, 11, 17, 'Sonia Ackerman', 77.7, 60.7, 78.6, 74.4, 70.8, 362.20, 9.05),
       (557, 11, 21, 'Alice Gonzales', 58.2, 52.9, 58.1, 66.7, 73.8, 309.70, 7.74),
       (558, 11, 24, 'Harry Styles', 80.0, 80.0, 80.0, 80.0, 80.0, 400.00, 10.00),
       (559, 10, 27, 'Benito Agee', 68.3, 66.4, 63.2, 53.4, 80.0, 331.30, 8.28),
       (573, 10, 4, 'Stanford Sullivan', 57.2, 63.8, 69.9, 76.3, 71.2, 338.40, 8.46),
       (574, 11, 5, 'Adam Geer', 61.6, 53.2, 51.5, 71.7, 73.9, 311.90, 7.80),
       (575, 10, 10, 'Elli Robertson', 53.9, 72.9, 71.4, 66.8, 70.5, 335.50, 8.39),
       (576, 10, 15, 'Carley Valdez', 52.3, 79.0, 70.7, 77.7, 80.0, 359.70, 8.99),
       (577, 11, 19, 'Burt Hughes', 50.1, 80.0, 70.3, 58.9, 74.8, 334.10, 8.35),
       (578, 12, 23, 'Milton Gay', 75.2, 74.2, 59.8, 56.8, 70.8, 336.80, 8.42),
       (579, 12, 26, 'Bradford Alfaro', 78.5, 67.1, 70.0, 55.0, 74.5, 345.10, 8.63),
       (583, 11, 1, 'Taylor Swift', 73.5, 77.8, 69.4, 76.6, 73.3, 370.60, 9.27),
       (584, 12, 4, 'Burton Bunnell', 62.4, 64.9, 73.6, 67.2, 73.4, 341.50, 8.54),
       (585, 11, 7, 'Imagine Dragins', 76.8, 74.5, 69.2, 76.2, 72.6, 369.30, 9.23),
       (586, 12, 10, 'Melia Gates', 51.5, 64.8, 77.0, 62.0, 73.3, 328.60, 8.21),
       (587, 12, 12, 'Oliva Coble', 66.9, 74.3, 52.4, 60.9, 70.7, 325.20, 8.13),
       (588, 10, 16, 'Ariana Grande', 80.0, 80.0, 80.0, 80.0, 80.0, 400.00, 10.00),
       (589, 12, 17, 'Derrick Ruiz', 53.2, 57.1, 75.9, 53.4, 71.5, 311.10, 7.78),
       (590, 11, 22, 'Abram Fenton', 59.6, 77.6, 53.5, 66.7, 74.7, 332.10, 8.30),
       (591, 11, 23, 'Bryce Estrada', 71.9, 59.6, 54.9, 75.2, 80.0, 341.60, 8.54),
       (592, 12, 25, 'Sonya Tinsley', 72.6, 62.3, 51.0, 70.6, 70.7, 327.20, 8.18),
       (593, 11, 29, 'Rivka Caron', 78.3, 58.9, 79.3, 65.5, 79.5, 361.50, 9.04),
       (604, 12, 1, 'Marcos Abraham', 74.5, 60.0, 73.5, 57.4, 70.0, 335.40, 8.38),
       (605, 12, 6, 'Adam Maddox', 64.6, 58.7, 63.5, 61.6, 72.2, 320.60, 8.02),
       (606, 10, 8, 'Kasey Furr', 71.5, 51.7, 53.4, 51.2, 78.8, 306.60, 7.67),
       (607, 11, 12, 'Jarod Bourgeois', 79.6, 56.3, 52.5, 80.0, 80.0, 348.40, 8.71),
       (608, 11, 13, 'Bud Grubbs', 80.0, 78.1, 58.3, 51.8, 73.2, 341.40, 8.54),
       (609, 10, 17, 'Zayn Malik', 75.8, 71.7, 73.0, 74.0, 74.7, 369.20, 9.23),
       (610, 11, 18, 'Myrtis Thornhill', 66.7, 67.7, 59.5, 69.6, 80.0, 343.50, 8.59),
       (611, 10, 23, 'Alexa Saucedo', 77.7, 69.7, 79.6, 53.5, 76.4, 356.90, 8.92),
       (612, 10, 25, 'Armando Alvarez', 69.6, 72.4, 67.5, 69.2, 76.1, 354.80, 8.87),
       (613, 11, 27, 'Alan Judd', 77.2, 68.5, 51.1, 61.1, 75.7, 333.60, 8.34),
       (614, 10, 30, 'Janis Gonsalves', 57.4, 55.8, 59.2, 51.2, 75.3, 298.90, 7.47),
       (623, 12, 16, 'Martin Garrix', 71.4, 80.0, 73.6, 75.5, 72.2, 372.70, 9.32),
       (624, 10, 20, 'Hobert Adam', 71.6, 57.9, 71.1, 55.4, 70.5, 326.50, 8.16),
       (625, 12, 22, 'Carlton Beaudoin', 63.3, 78.0, 76.2, 73.7, 71.2, 362.40, 9.06),
       (626, 10, 26, 'Machelle Andersen', 75.6, 52.2, 79.2, 68.9, 76.3, 352.20, 8.80),
       (627, 12, 30, 'Johnathan Magana', 60.3, 56.8, 65.2, 72.2, 78.0, 332.50, 8.31),
       (628, 10, 32, 'Sanjuanita Conners', 76.5, 64.5, 63.7, 52.9, 79.0, 336.60, 8.42),
       (639, 10, 3, 'Felix Alba', 59.0, 60.5, 75.0, 73.6, 75.5, 343.60, 8.59),
       (640, 11, 4, 'Nathan Salisbury', 73.2, 71.1, 58.1, 74.4, 78.8, 355.60, 8.89),
       (641, 11, 6, 'Ariel Hermann', 63.6, 52.3, 68.6, 75.5, 73.2, 333.20, 8.33),
       (642, 10, 11, 'Marc Pickering', 54.6, 71.7, 75.9, 55.9, 80.0, 338.10, 8.45),
       (643, 12, 14, 'Malcolm Coward', 59.6, 53.4, 51.5, 70.0, 74.5, 309.00, 7.72),
       (644, 10, 19, 'Deedee Strange', 55.8, 53.6, 64.7, 77.3, 72.1, 323.50, 8.09),
       (645, 10, 21, 'Jeanna Maxwell', 59.6, 61.6, 75.5, 76.9, 75.5, 349.10, 8.73),
       (646, 11, 25, 'Glynis Redman', 76.8, 64.7, 68.7, 75.9, 73.1, 359.20, 8.98),
       (647, 11, 28, 'Debbra Packer', 54.2, 65.7, 79.8, 72.4, 72.0, 344.10, 8.60),
       (648, 11, 31, 'Graham Alger', 64.1, 51.5, 79.3, 70.1, 76.0, 341.00, 8.53),
       (649, 10, 33, 'Abdul Freed', 76.8, 76.6, 72.2, 60.1, 72.9, 358.60, 8.96),
       (660, 11, 3, 'Eusebia Noland', 63.5, 51.5, 59.0, 74.4, 78.7, 327.10, 8.18),
       (661, 12, 5, 'Chris Brown', 51.7, 59.1, 70.3, 72.5, 75.8, 329.40, 8.23),
       (662, 11, 8, 'Gertie Abel', 64.4, 62.9, 63.9, 56.4, 77.5, 325.10, 8.13),
       (663, 10, 13, 'Corey Musgrove', 69.8, 60.3, 66.6, 68.7, 80.0, 345.40, 8.63),
       (665, 10, 1, 'Letha Bolt', 66.6, 72.5, 62.9, 60.8, 76.8, 339.60, 8.49),
       (666, 10, 6, 'Laura Barger', 61.5, 57.5, 57.8, 76.6, 74.4, 327.80, 8.20),
       (667, 12, 8, 'Myles Angel', 76.3, 75.4, 58.7, 80.0, 71.1, 361.50, 9.04),
       (668, 11, 11, 'Alida Jobe', 67.0, 74.7, 73.5, 55.4, 77.0, 347.60, 8.69),
       (669, 10, 12, 'Dua Lipa', 67.1, 60.0, 78.5, 79.0, 75.2, 359.80, 9.00),
       (670, 11, 15, 'Lizzie Krueger', 67.0, 80.0, 53.2, 80.0, 73.0, 353.20, 8.83),
       (671, 11, 16, 'Hubert Waldrop', 64.9, 52.8, 77.0, 56.1, 78.8, 329.60, 8.24),
       (672, 10, 22, 'Mervin Lyon', 69.8, 60.4, 63.2, 60.3, 70.4, 324.10, 8.10),
       (673, 12, 28, 'Chris Brown', 80.0, 80.0, 65.7, 70.2, 75.0, 370.90, 9.27),
       (674, 12, 29, 'Justin Bieber', 80.0, 80.0, 80.0, 80.0, 80.0, 400.00, 10.00),
       (675, 11, 32, 'Tanner Van', 69.8, 77.1, 73.7, 71.1, 70.3, 362.00, 9.05),
       (676, 11, 33, 'Ora Dorris', 51.6, 52.4, 69.3, 57.1, 72.0, 302.40, 7.56),
       (684, 10, 2, 'Miyoko Mckinney', 59.0, 59.6, 54.4, 73.1, 74.4, 320.50, 8.01),
       (685, 10, 7, 'Winnifred Brantley', 56.3, 64.9, 66.5, 67.2, 71.6, 326.50, 8.16),
       (686, 12, 9, 'Josephine Norwood', 69.8, 68.1, 70.2, 52.6, 74.7, 335.40, 8.38),
       (687, 12, 11, 'Cordelia Key', 50.1, 78.6, 56.9, 57.5, 79.0, 322.10, 8.05),
       (688, 11, 14, 'Bertram Herzog', 78.6, 77.8, 50.4, 70.4, 70.0, 347.20, 8.68),
       (689, 12, 15, 'Celestine Hong', 51.8, 72.9, 80.0, 76.7, 71.2, 352.60, 8.82),
       (690, 12, 20, 'Abel Christian', 58.9, 55.3, 56.5, 75.0, 76.5, 322.20, 8.05),
       (691, 10, 24, 'Halley Bostic', 54.8, 68.2, 61.2, 73.7, 80.0, 337.90, 8.45),
       (692, 10, 29, 'Drew Burt', 71.1, 63.9, 50.0, 80.0, 71.6, 336.60, 8.42),
       (693, 12, 31, 'Kizzy Hightower', 73.4, 60.5, 51.2, 80.0, 79.3, 344.40, 8.61),
       (694, 12, 32, 'Abel Paulson', 52.1, 50.2, 54.1, 62.3, 79.3, 298.00, 7.45),
       (695, 12, 33, 'Abbie Gurley', 52.2, 73.3, 66.1, 62.5, 75.6, 329.70, 8.24)]

cursor.executemany(sql, val)
mydb.commit()