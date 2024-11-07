from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from Models import Note
from Schemas import Note as NoteSchema

from Database import SessionLocal

#app initilization
app=FastAPI()

#daatabase dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#post request to create a new note
@app.post("/Notes")
def create_note(note: NoteSchema,db:Session=Depends(get_db)):
    #create a new note object with the title and content from Note(schemas)
    new_note=Note(title=note.title,content=note.content)
    db.add(new_note)#Add the new note to the session
    db.commit()#commit to save to database
    db.refresh(new_note)#refresh to get the latest version of the database
    return new_note

#get request to retrieve all notes
@app.get("/Notes")
#Excecutes a query to retrieve all notes and return as a list
def get_all_notes(db:Session=Depends(get_db)):
    Notes=db.execute(select(Note)).scalars().all()
    return Notes

#get request to retrieve a specific note
@app.get("/Notes/{note_id}")
#query the database for a note with the given note_id
def get_note(note_id:int ,db:Session=Depends(get_db)):
    note=db.execute(select(Note).where(Note.id==note_id)).scalar_one_or_none()
    if note is None:
        #raise a 404 error if the note is not found
        raise HTTPException(status_code=404, detail="Note not found")
    return note


#delete request to delete a specific note
@app.delete("/Notes/{note_id}")
def del_note(note_id:int,db:Session=Depends(get_db)):
    #retrieve the note to delete by its id
    note=db.get(Note,note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)#delete the note from the session
    db.commit()#sve changes made to the session
    return {"message":"Note deleted sucessfully"}