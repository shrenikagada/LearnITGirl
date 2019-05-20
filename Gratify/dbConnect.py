import sqlite3

#Open database
conn = sqlite3.connect('gratify.db')

#Create table
# conn.execute('''CREATE TABLE users
# 		(userId INTEGER PRIMARY KEY,
# 		password TEXT,
# 		email TEXT,
# 		firstName TEXT,
# 		lastName TEXT,
# 		address1 TEXT,
# 		address2 TEXT,
# 		zipcode TEXT,
# 		city TEXT,
# 		state TEXT,
# 		country TEXT,
# 		phone TEXT
# 		)''')
# conn.commit()
# conn.execute('''CREATE TABLE products
# 		(productId INTEGER PRIMARY KEY,
# 		name TEXT,
# 		price REAL,
# 		description TEXT,
# 		image TEXT,
# 		stock INTEGER,
# 		categoryId INTEGER,
# 		FOREIGN KEY(categoryId) REFERENCES categories(categoryId)
# 		)''')
# conn.commit()
# conn.execute('''CREATE TABLE kart
# 		(userId INTEGER,
# 		productId INTEGER,
# 		FOREIGN KEY(userId) REFERENCES users(userId),
# 		FOREIGN KEY(productId) REFERENCES products(productId)
# 		)''')
# conn.commit()
# conn.execute('''CREATE TABLE categories
#         (categoryId INTEGER PRIMARY KEY,
#         name TEXT)''')
# conn.commit()
# conn.execute('''CREATE TABLE cardInfo
#         (userId INTEGER,
#         cardNo INTEGER,
#         cardHolderName TEXT,
#         cvv TEXT,
#         validity TEXT,
#         FOREIGN KEY(userId) REFERENCES users(userId))''')
# conn.commit()
conn.execute('''INSERT INTO categories values(1,'Women'),(2,'Men'),(3,'Children')''')
conn.commit()
conn.close()