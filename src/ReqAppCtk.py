from ReqDb import ReqDb
from ReqGuiCtk import ReqGuiCtk

def main():
    db = ReqDb(dbName='ReqDb.csv')
    app = ReqGuiCtk(dataBase=db)
    app.mainloop()

if __name__ == "__main__":
    main()