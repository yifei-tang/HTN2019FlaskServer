import mysql.connector
import collections

class my_database:
    def __init__(self):
        self.mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="WShuaren",
                database="testdb"
            )

        #set up cursor and clear  old table
        self.mycursor=self.mydb.cursor()
        self.clearDB()

        #set up table
        self.mycursor.execute("CREATE TABLE Food (Name VARCHAR(50), Type VARCHAR(255), Season VARCHAR(50), Exported VARCHAR(255))")
        
        #must print if you fetch show tables
        self.mycursor.execute("SHOW TABLES")
        for tb in self.mycursor:
            print('table number',tb)

        self.insertDB('Cheese','Dairy and Eggs','None','No') 
        self.insertDB('Cottage cheese','Dairy and Eggs','None','No')
        self.insertDB('Camembert cheese','Dairy and Eggs','None','No')
        self.insertDB('Feta cheese','Dairy and Eggs','None','No')
        self.insertDB('Mozzarella cheese','Dairy and Eggs','None','No')
        self.insertDB('Parmesan cheese','Dairy and Eggs','None','No')
        self.insertDB('Sour cream','Dairy and Eggs','None','No')
        self.insertDB('Low fat milk','Dairy and Eggs','None','No')
        self.insertDB('Eggnog','Dairy and Eggs','None','No')
        self.insertDB('Chocolate milk','Dairy and Eggs','None','No')
        self.insertDB('Chicken broth','Soups','None','No')
        self.insertDB('Black bean soup','Soups','None','No')
        self.insertDB('Cream of asparagus','Soups','None','No')
        self.insertDB('Beef Noodle','Soups','None','No')
        self.insertDB('Clam chowder','Soups','None','No')
        self.insertDB('Chili beef','Soups','None','No')
        self.insertDB('Minestrone soup','Soups','None','No')
        self.insertDB('Cream of onion','Soups','None','No')
        self.insertDB('Cream of potato','Soups','None','No')
        self.insertDB('Apples','Fruits','W,Sp,F','No')
        self.insertDB('Bananas','Fruits','None','Ecuador, Guatemala, Peru, Columbia')
        self.insertDB('Strawberries','Fruits','Su,F','No')
        self.insertDB('Raspberries','Fruits','Su,F','No')
        self.insertDB('Blackberries','Fruits','None','Guatemala')
        self.insertDB('Cherries','Fruits','Su','No')
        self.insertDB('Watermelon','Fruits','Su','No')
        self.insertDB('Avocados','Fruits','None','Mexico')
        self.insertDB('Figs','Fruits','None','Moroco')
        self.insertDB('Asparagus','Veggies','Su','No')
        self.insertDB('Broccoli','Veggies','Su,F','No')
        self.insertDB('Beans','Veggies','Su,F','No')
        self.insertDB('Cabbage','Veggies','W,Su,F,Sp','No')
        self.insertDB('Carrots','Veggies','W,Su,F,Sp','No')
        self.insertDB('Cauliflower','Veggies','Su,F','No')
        self.insertDB('Corn','Veggies','Su,F','No')
        self.insertDB('Mushrooms','Veggies','W,Su,F,Sp','No')
        self.insertDB('Asparagus','Veggies','Su,F','No')
        self.insertDB('Green tea','Beverages','None','No')
        self.insertDB('Coffee','Beverages','None','No')
        self.insertDB('Hot chocolate','Beverages','None','No')
        self.insertDB('Chamomile tea','Beverages','None','No')
        self.insertDB('Carbonated water','Beverages','None','No')
        self.insertDB('Lemonade','Beverages','None','No')
        self.insertDB('Orange juice','Beverages','None','No')
        self.insertDB('Distilled water','Beverages','None','No')

        #get Name as a list from db
        #compare the Name list using the method you wrote
            #if it matches, get the season and exported
            #if they are exported or wrong season, subtract one from the envScore

        
        self.mydb.commit()

    def getListNamesDB(self):
        sqlFormula="SELECT NAME FROM Food"
        self.mycursor.execute(sqlFormula)
        result=self.mycursor.fetchall()
        #print(result)
        return result

    def insertDB(self,name,myType,season,exported):
        #print('insert')
        #insert into Food
        sqlFormula="INSERT INTO Food (Name, Type, Season, Exported) VALUES (%s,%s,%s,%s)"
        foodItem=(name,myType,season,exported)
        self.mycursor.execute(sqlFormula,foodItem)
        #self.showTableDB()

    def showTableDB(self):
        self.mycursor.execute('SELECT * FROM Food')
        print('show',self.mycursor.fetchall())

    def getInfoFromName(self,name):
        self.mycursor.execute(("SELECT Season, Exported FROM Food WHERE Name=%s"),(name,))
        result=self.mycursor.fetchall()
        return result

        
    def clearDB(self):
        try:
            self.mycursor.execute("DROP TABLE testdb.Food")
        except:
            print('Table Cleared Already')