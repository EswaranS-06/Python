tasks = []
def add_task ( task ) :
    tasks.append ( task )
    print (" Task added successfully !")
def view_tasks () :
    count = 0
    for i in tasks :
        count +=1
        print ( f"{count}. {i}")
def delete_task ( index ) :
    tasks. pop ( index )
    print (" Task deleted !")
add_task ("Buy groceries ")
add_task ("Finish assignment ")
view_tasks ()
delete_task (1)
view_tasks ()
