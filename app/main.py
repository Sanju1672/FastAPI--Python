from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def root():
    return {
             {'Id': '1',
             'Title': 'Harry Potter' ,
             'Author': 'J.K Rowling', 
             'Year of publication': '2015'
             },
             {
             'Id': '2',
             'Title': 'The Lord of the Rings' ,
             'Author': 'J.R. Tolkien', 
             'Year of publication': '1954'
             },
             {
              'Id': '3',
             'Title': 'Master Your Emotions' ,
             'Author': 'Eric Robertson', 
             'Year of publication': '2022'
             },
             {
             'Id': '4',
             'Title': 'The Girl with no dreams' ,
             'Author': 'Deepak Gupta', 
             'Year of publication': '2022'
             },
             {
              'Id': '5',
             'Title': 'Better than Best Friends' ,
             'Author': 'Ahona Sadhu', 
             'Year of publication': '2023'
             }
    }