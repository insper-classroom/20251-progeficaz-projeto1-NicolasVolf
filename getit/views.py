from utils import load_data, load_template, add_note

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    notes = load_data('notes.json')
    notes.append({'titulo': titulo, 'detalhes': detalhes})
    add_note(notes, 'notes.json')
    return notes

def delete(note_id):
    notes = load_data('notes.json')
    notes.delete(note_id)
    return notes
    
